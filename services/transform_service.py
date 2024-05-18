import json

from objects.transformation_executable import TransformationExecutable
from protocol.transform.v1 import transform_pb2, transform_pb2_grpc


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
        transformation_id = request.transformationId
        if not transformation_id:
            response.data.extend(request.data)
            return response
        from services.service_factory import SERVICE_FACTORY
        transformation: TransformationExecutable = SERVICE_FACTORY.get_transformation_factory().get_transformation(
            transformation_id)
        if not transformation:
            response.transformationMissing = True
            response.data.extend(request.data)
            return response
        data_list = request.data
        if not data_list:
            response.data.extend([])
            return response

        transformed_data = []
        for data in data_list:
            try:
                parsed_data = json.loads(data)
            except Exception as e:
                print(repr(e))
                transformed_data.append(data)
                continue

            try:
                transformation.process(parsed_data)
                json_data = json.dumps(parsed_data)
                transformed_data.append(json_data)
                del parsed_data
            except Exception as e:
                print(repr(e))
                transformed_data.append(data)
                continue

        response.data.extend(transformed_data)
        return response
