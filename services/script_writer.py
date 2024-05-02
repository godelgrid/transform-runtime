import uuid
from types import CodeType

INLINE_TRANSFORMER = """
def transform(self, data):
    __SCRIPT__
"""


def compile_script(script: str) -> CodeType:
    script_id: str = str(uuid.UUID()).replace("-", "")
    transformer_script = INLINE_TRANSFORMER.replace("__SCRIPT__", script)
    return compile(transformer_script, f"script{script_id}", 'exec')
