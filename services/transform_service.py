import json
import logging
import time
from typing import Any, Dict, Iterable, List, Optional, Tuple

from objects.transformation_executable import TransformationExecutable
from protocol.transform.v1 import transform_pb2, transform_pb2_grpc

logger = logging.getLogger(__name__)


class TransformService(transform_pb2_grpc.Transform):

    @staticmethod
    def TransformData(request: transform_pb2.TransformRequest,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        response = transform_pb2.TransformResponse()
        if not request.transformationIds:
            response.data.extend(request.data)
            return response
        transformation_ids = [tid for tid in request.transformationIds]
        from services.service_factory import SERVICE_FACTORY
        transformations, missing_transformation_ids = \
            SERVICE_FACTORY.get_transformation_factory().get_transformations(transformation_ids)
        if missing_transformation_ids:
            response.transformationMissing = True
            response.missingTransformations.extend(missing_transformation_ids)
            return response
        data_list = request.data
        if not data_list:
            response.data.extend([])
            return response

        parsed_data_list = TransformService.load_json_data(data_list)

        for transformation in transformations:
            if transformation.is_batch_transformation():
                TransformService.process_batch_transformation(transformation, parsed_data_list)
            else:
                TransformService.process_singleton_transformation(transformation, parsed_data_list)

        transformed_data = TransformService.build_json_data(parsed_data_list)

        response.data.extend(transformed_data)
        return response

    @staticmethod
    def load_json_data(data_list: Iterable[str]) -> List[Tuple[Optional[Dict[str, Any]], str, bool]]:
        parsed_data_list = []
        for data in data_list:
            try:
                parsed_data = json.loads(data)
                parsed_data_list.append((parsed_data, data, True,))
            except Exception:
                logger.exception("error occurred while loading json data")
                parsed_data_list.append((None, data, False,))

        return parsed_data_list

    @staticmethod
    def process_singleton_transformation(transformation: TransformationExecutable,
                                         parsed_data_list: List[Tuple[Optional[Dict[str, Any]], str, bool]]) -> None:
        for data_index in range(len(parsed_data_list)):
            parsed_data, data, next_step = parsed_data_list[data_index]
            if not next_step:
                continue
            try:
                transformation.process(parsed_data)
            except Exception:
                logger.exception(
                    f"error occurred while processing data with transformation: {transformation.get_transformation_id()}")
                # do not process this data row again
                parsed_data_list[data_index] = (parsed_data, data, False,)

    @staticmethod
    def process_batch_transformation(transformation: TransformationExecutable,
                                     parsed_data_list: List[Tuple[Optional[Dict[str, Any]], str, bool]]) -> None:
        to_process_batch = [processed_data for processed_data, _, next_step in parsed_data_list if next_step]
        try:
            transformation.process(to_process_batch)
        except Exception:
            logger.exception(
                f"error occurred while processing data with batch transformation: {transformation.get_transformation_id()}")
            for data_index in range(len(parsed_data_list)):
                parsed_data_list[data_index] = (
                    parsed_data_list[data_index][0], parsed_data_list[data_index][1], False,)

    @staticmethod
    def build_json_data(parsed_data_list: List[Tuple[Optional[Dict[str, Any]], str, bool]]) -> List[str]:
        transformed_data = []
        for parsed_data, data, _ in parsed_data_list:
            if not parsed_data:
                transformed_data.append(data)
                continue
            try:
                json_data = json.dumps(parsed_data)
                transformed_data.append(json_data)
            except Exception:
                logger.exception("error occurred while converting data to json")
                transformed_data.append(data)

        return transformed_data
