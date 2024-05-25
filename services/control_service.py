import os

from objects.repo_data import RepositoryData
from protocol.transform.v1 import control_pb2, control_pb2_grpc
from protocol.transform.v1.control_pb2 import LoadExternalModuleResponse, VerifyExternalModuleResponse


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
        transformation_id = request.transformationId
        script = request.script
        response = control_pb2.LoadInlineModuleResponse()
        if not script:
            response.success = False
            response.error = 'Script cannot be blank'
            return response

        from services.service_factory import SERVICE_FACTORY
        success, error = SERVICE_FACTORY.get_transformation_factory().load_inline_module(transformation_id, script)
        if success:
            response.success = True
            return response
        else:
            response.success = False
            response.error = error if error else 'Unknown Error occurred while loading inline module'
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
        from services.service_factory import SERVICE_FACTORY
        for request in request_iterator:
            SERVICE_FACTORY.get_process_monitor_service().update_health_check()
            response = control_pb2.HeartbeatResponse()
            response.healthy = True
            yield response

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

        from services.service_factory import SERVICE_FACTORY
        success, error = SERVICE_FACTORY.get_transformation_factory().verify_inline_module(script)
        response.success = True if success else False
        if error:
            response.error = error
        return response

    @staticmethod
    def ServerDetails(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        process_id = os.getpid()
        response = control_pb2.ServerDetailsResponse()
        response.serverPid = str(process_id)
        return response

    @staticmethod
    def VerifyExternalModule(request,
                             target,
                             options=(),
                             channel_credentials=None,
                             call_credentials=None,
                             insecure=False,
                             compression=None,
                             wait_for_ready=None,
                             timeout=None,
                             metadata=None):
        repo_data = RepositoryData(transformation_id=request.transformationId,
                                   repo_type=control_pb2.ExternalRepoType.Name(request.repoType),
                                   repo_path=request.repoPath,
                                   repo_ref=request.repoRef,
                                   access_token=request.accessToken,
                                   module_path=request.modulePath,
                                   requirements_path=request.requirementsPath,
                                   transformation_name=request.transformationName)
        response = VerifyExternalModuleResponse()
        from services.service_factory import SERVICE_FACTORY
        success, error = SERVICE_FACTORY.get_transformation_factory().verify_external_module(repo_data)
        response.success = True if success else False
        if error:
            response.error = error
        return response

    @staticmethod
    def LoadExternalModule(request,
                           target,
                           options=(),
                           channel_credentials=None,
                           call_credentials=None,
                           insecure=False,
                           compression=None,
                           wait_for_ready=None,
                           timeout=None,
                           metadata=None):
        transformation_id = request.transformationId
        repo_data = RepositoryData(transformation_id=transformation_id,
                                   repo_type=control_pb2.ExternalRepoType.Name(request.repoType),
                                   repo_path=request.repoPath,
                                   repo_ref=request.repoRef,
                                   access_token=request.accessToken,
                                   module_path=request.modulePath,
                                   requirements_path=request.requirementsPath,
                                   transformation_name=request.transformationName)
        response = LoadExternalModuleResponse()
        from services.service_factory import SERVICE_FACTORY
        success, error = SERVICE_FACTORY.get_transformation_factory().load_external_module(transformation_id, repo_data)
        response.success = True if success else False
        if error:
            response.error = error
        return response
