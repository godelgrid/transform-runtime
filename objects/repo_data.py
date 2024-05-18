from typing import Optional


class RepositoryData:

    def __init__(self, transformation_id: str,
                 repo_type: str,
                 repo_path: str,
                 repo_ref: str,
                 access_token: Optional[str],
                 module_path: str,
                 requirements_path: Optional[str],
                 transformation_name: str):
        self._transformation_id = transformation_id
        self._repo_type = repo_type
        self._repo_path = repo_path
        self._repo_ref = repo_ref
        self._access_token = access_token
        self._module_path = module_path
        self._requirements_path = requirements_path
        self._transformation_name = transformation_name

    def get_transformation_id(self) -> str:
        return self._transformation_id

    def get_repo_type(self) -> str:
        return self._repo_type

    def get_repo_path(self) -> str:
        return self._repo_path

    def get_repo_ref(self) -> str:
        return self._repo_ref

    def get_access_token(self) -> str:
        return self._access_token

    def get_module_path(self) -> str:
        return self._module_path

    def get_requirements_path(self) -> str:
        return self._requirements_path

    def get_transformation_name(self) -> str:
        return self._transformation_name
