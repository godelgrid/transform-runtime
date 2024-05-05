import json

from protocol.transform.v1 import transform_pb2, transform_pb2_grpc
from services.transformer_factory import TRANSFORM_FACTORY


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
        transformer_id = request.transformer_id
        if not transformer_id:
            response.data.extend(request.data)
            return response
        transformer = TRANSFORM_FACTORY.get_transformer(transformer_id)
        if not transformer:
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
                print(str(e))
                transformed_data.append(data)
                continue
            context = {'data': parsed_data}
            exec(transformer, context)
            try:
                json_data = json.dumps(parsed_data)
                transformed_data.append(json_data)
                del parsed_data
            except Exception as e:
                print(str(e))
                transformed_data.append(data)
                continue

        response.data.extend(transformed_data)
        return response
