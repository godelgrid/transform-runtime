import uuid
from types import CodeType

INLINE_TRANSFORMER = """def transform(data):
__SCRIPT__

transform(data)
"""


def compile_script(script: str) -> CodeType:
    script_id: str = str(uuid.uuid4()).replace("-", "")
    script = '\n'.join(['\t' + line for line in script.splitlines()])
    transformer_script = INLINE_TRANSFORMER.replace("__SCRIPT__", script)
    return compile(transformer_script, f"script{script_id}", 'exec')
