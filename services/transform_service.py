import json
import logging

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

        transformed_data = []
        for data in data_list:
            try:
                parsed_data = json.loads(data)
            except Exception:
                logger.exception("error occurred while loading json data")
                transformed_data.append(data)
                continue

            for transformation in transformations:
                try:
                    transformation.process(parsed_data)
                except Exception:
                    logger.exception(
                        f"error occurred while processing data with transformation: {transformation.get_transformation_id()}")
                    # break at this point because next set of transformations might depend of correct processing
                    # by this transformation
                    break
            try:
                json_data = json.dumps(parsed_data)
                transformed_data.append(json_data)
                del parsed_data
            except Exception:
                logger.exception("error occurred while converting data to json")
                transformed_data.append(data)
                continue

        response.data.extend(transformed_data)
        return response
