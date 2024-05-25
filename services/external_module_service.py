import importlib.util
import logging
import os.path
import subprocess
import sys
import traceback
from types import ModuleType
from typing import Callable, Optional, Tuple

from gdtransform import introspect

logger = logging.getLogger(__name__)


class ExternalModuleService:

    def __init__(self):
        pass

    def install_requirements(self, requirements_path: str) -> Tuple[bool, Optional[str]]:
        try:
            command = [sys.executable, "-m", "pip", "install", "-r", requirements_path]
            process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            if process.returncode != 0:
                logger.error(f"error occurred while installing requirements: \n\n{process.stdout} \n\n{process.stderr}")
                raise subprocess.CalledProcessError(process.returncode, process.args,
                                                    output=process.stdout, stderr=process.stderr)
            return True, None
        except Exception as e:
            message = traceback.format_exc()
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
            message = traceback.format_exc()
            return False, message, None

    def load_transformation(self, transformation_module: ModuleType, name: str) -> \
            Tuple[bool, Optional[str], Optional[Callable]]:
        try:
            transformation = introspect.get_module_transformation(transformation_module, name)
            if not transformation:
                return False, f'Transformation with name {name} not found in specified module', None
            return True, None, transformation
        except Exception as e:
            message = traceback.format_exc()
            return False, message, None
