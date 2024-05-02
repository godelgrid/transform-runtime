from types import CodeType
from typing import Optional

from services.script_writer import compile_script


class TransformerFactory:

    def __init__(self):
        self._transformer_map = dict()

    def verify_inline_module(self, script: str) -> [bool, Optional[str]]:
        script_object: CodeType
        try:
            script_object = compile_script(script)
            del script_object
        except Exception as e:
            return False, str(e)

        return True, None

    def load_inline_module(self, transformer_id: str, script: str) -> [bool, str]:
        if transformer_id in self._transformer_map:
            transformer = self._transformer_map.pop(transformer_id)
            del transformer

        script_object: CodeType
        try:
            script_object = compile_script(script)
        except Exception as e:
            return False, str(e)

        self._transformer_map[transformer_id] = script_object
        return True, None

    def get_transformer(self, transformer_id) -> Optional[CodeType]:
        if transformer_id not in self._transformer_map:
            return None

        return self._transformer_map.get(transformer_id)


TRANSFORM_FACTORY: TransformerFactory = TransformerFactory()
