from abc import ABC

from objects.repo_data import RepositoryData


class ExternalRepoService(ABC):

    def fetch_repository(self, repo_data: RepositoryData) -> str:
        pass

    def clean_up_repository(self, repo_path) -> None:
        pass
