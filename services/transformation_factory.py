import os
from types import CodeType
from typing import List, Optional, Tuple

from objects.repo_data import RepositoryData
from objects.transformation_executable import EXECUTABLE_TYPE_CALLABLE, EXECUTABLE_TYPE_INLINE, TransformationExecutable
from services.script_writer import compile_script


class TransformationFactory:

    def __init__(self):
        self._transformation_map = dict()

    def verify_inline_module(self, script: str) -> [bool, Optional[str]]:
        script_object: CodeType
        try:
            script_object = compile_script(script)
            del script_object
        except Exception as e:
            return False, str(e)

        return True, None

    def load_inline_module(self, transformation_id: str, script: str) -> [bool, str]:
        if transformation_id in self._transformation_map:
            transformer = self._transformation_map.pop(transformation_id)
            del transformer

        script_object: CodeType
        try:
            script_object = compile_script(script)
        except Exception as e:
            return False, str(e)

        self._transformation_map[transformation_id] = (script_object, EXECUTABLE_TYPE_INLINE,)
        return True, None

    def verify_external_module(self, repo_data: RepositoryData) -> [bool, str]:
        from services.service_factory import SERVICE_FACTORY
        repo_service_factory = SERVICE_FACTORY.get_external_repo_service_factory()
        try:
            repo_service = repo_service_factory.get_service(repo_data.get_repo_type())
        except Exception as e:
            return False, repr(e)

        repo_path = repo_service.fetch_repository(repo_data)
        external_module_service = SERVICE_FACTORY.get_external_module_service()

        if repo_data.get_requirements_path():
            requirements_path = os.path.join(repo_path, repo_data.get_requirements_path())
            requirements_path = os.path.normpath(requirements_path)
            success, error = external_module_service.install_requirements(requirements_path)
            if not success:
                return False, f'Error occurred while installing requirements: {error}'

        module_path = os.path.join(repo_path, repo_data.get_module_path())
        module_path = os.path.normpath(module_path)
        success, error, module = external_module_service.import_module(repo_data.get_module_path(), module_path)
        if not success:
            return False, f'Error occurred while importing module: {error}'

        success, error, _ = external_module_service.load_transformation(module, repo_data.get_transformation_name())
        if not success:
            return False, f'Error occurred while loading transformation: {error}'

        try:
            repo_service.clean_up_repository(repo_path)
        except Exception:
            pass
        return True, None

    def load_external_module(self, transformation_id: str, repo_data: RepositoryData) -> [bool, str]:
        from services.service_factory import SERVICE_FACTORY
        repo_service_factory = SERVICE_FACTORY.get_external_repo_service_factory()
        try:
            repo_service = repo_service_factory.get_service(repo_data.get_repo_type())
        except Exception as e:
            return False, repr(e)

        repo_path = repo_service.fetch_repository(repo_data)
        external_module_service = SERVICE_FACTORY.get_external_module_service()

        if repo_data.get_requirements_path():
            requirements_path = os.path.join(repo_path, repo_data.get_requirements_path())
            requirements_path = os.path.normpath(requirements_path)
            success, error = external_module_service.install_requirements(requirements_path)
            if not success:
                return False, f'Error occurred while installing requirements: {error}'

        module_path = os.path.join(repo_path, repo_data.get_module_path())
        module_path = os.path.normpath(module_path)
        success, error, module = external_module_service.import_module(module_path)
        if not success:
            return False, f'Error occurred while importing module: {error}'

        success, error, transformation = \
            external_module_service.load_transformation(module, repo_data.get_transformation_name())
        if not success:
            return False, f'Error occurred while loading transformation: {error}'

        self._transformation_map[transformation_id] = (transformation, EXECUTABLE_TYPE_CALLABLE,)
        return True, None

    def get_transformations(self, transformation_ids: List[str]) -> Tuple[List[TransformationExecutable], List[str]]:
        transformations = []
        missing_ids = []
        for transformation_id in transformation_ids:
            if transformation_id not in self._transformation_map:
                missing_ids.append(transformation_id)
            else:
                transformation, exec_type = self._transformation_map.get(transformation_id)
                transformations.append(TransformationExecutable(transformation_id, transformation, exec_type))

        return transformations, missing_ids
