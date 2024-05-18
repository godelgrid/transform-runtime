from .external_repo_service import ExternalRepoService


class ExternalRepoServiceFactory:

    def __init__(self):
        self._service_map = dict()

    def add_service(self, repo_type, repo_service: ExternalRepoService):
        self._service_map[repo_type] = repo_service

    def get_service(self, repo_type) -> ExternalRepoService:
        if repo_type not in self._service_map:
            raise Exception(f'{repo_type} not supported/initialized')

        return self._service_map[repo_type]
