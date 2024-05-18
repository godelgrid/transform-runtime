import importlib.util
import os.path
import subprocess
import sys
from types import ModuleType
from typing import Callable, Optional, Tuple

from gdtransform import introspect


class ExternalModuleService:

    def __init__(self):
        pass

    def install_requirements(self, requirements_path: str) -> Tuple[bool, Optional[str]]:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
            return True, None
        except Exception as e:
            message = repr(e)
            return False, message

    def import_module(self, relative_path: str, module_path: str) -> Tuple[bool, Optional[str], Optional[ModuleType]]:
        try:
            module_name = os.path.splitext(relative_path)[0]
            module_name = module_name.replace(os.sep, '.')
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            transformation_module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = transformation_module
            spec.loader.exec_module(transformation_module)
            return True, None, transformation_module
        except Exception as e:
            message = repr(e)
            return False, message, None

    def load_transformation(self, transformation_module: ModuleType, name: str) -> \
            Tuple[bool, Optional[str], Optional[Callable]]:
        try:
            transformation = introspect.get_module_transformation(transformation_module, name)
            if not transformation:
                return False, f'Transformation with name {name} not found in specified module', None
            return True, None, transformation
        except Exception as e:
            message = repr(e)
            return False, message, None
