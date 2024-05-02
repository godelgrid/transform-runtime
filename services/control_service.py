from protocol.transform.v1 import control_pb2, control_pb2_grpc
from services.transformer_factory import TRANSFORM_FACTORY


class ControlService(control_pb2_grpc.Control):

    @staticmethod
    def LoadInlineModule(request: control_pb2.LoadInlineModuleRequest,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        transformer_id = request.transformer_id
        script = request.script
        response = control_pb2.LoadInlineModuleResponse()
        if not script:
            response.success = False
            response.error = 'Script cannot be blank'
            return response

        success, error = TRANSFORM_FACTORY.load_inline_module(transformer_id, script)
        if success:
            response.success = True
            return response
        else:
            response.success = False
            response.error = error
            return response

    @staticmethod
    def HealthCheck(request_iterator,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        response = control_pb2.HeartbeatResponse()
        response.healthy = True
        return response

    @staticmethod
    def VerifyInlineModule(request,
                           target,
                           options=(),
                           channel_credentials=None,
                           call_credentials=None,
                           insecure=False,
                           compression=None,
                           wait_for_ready=None,
                           timeout=None,
                           metadata=None):
        response = control_pb2.VerifyInlineModuleResponse()
        script = request.script
        if not script:
            response.success = False
            response.error = 'Script cannot be blank'
            return response

        success, error = TRANSFORM_FACTORY.verify_inline_module(script)
        response.success = success
        response.error = error
        return response
