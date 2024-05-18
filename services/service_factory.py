import constants
from services.control_service import ControlService
from services.external_module_service import ExternalModuleService
from services.externalrepo.external_repo_service_factory import ExternalRepoServiceFactory
from services.externalrepo.github_service import GitHubService
from services.process_monitor_service import ProcessMonitorService
from services.transform_service import TransformService
from services.transformation_factory import TransformationFactory


class ServiceFactory:

    def load_services(self):
        self._process_monitor_service = ProcessMonitorService()
        self._transformation_factory = TransformationFactory()
        self._control_service = ControlService()
        self._transform_service = TransformService()
        github_service = GitHubService()
        self._external_repo_service_factory = ExternalRepoServiceFactory()
        self._external_repo_service_factory.add_service(constants.GITHUB_REPO_TYPE, github_service)
        self._external_module_service = ExternalModuleService()

    def get_control_service(self) -> ControlService:
        return self._control_service

    def get_transform_service(self) -> TransformService:
        return self._transform_service

    def get_process_monitor_service(self) -> ProcessMonitorService:
        return self._process_monitor_service

    def get_transformation_factory(self) -> TransformationFactory:
        return self._transformation_factory

    def get_external_repo_service_factory(self) -> ExternalRepoServiceFactory:
        return self._external_repo_service_factory

    def get_external_module_service(self) -> ExternalModuleService:
        return self._external_module_service


SERVICE_FACTORY: ServiceFactory = ServiceFactory()
