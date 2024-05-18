from types import CodeType
from typing import Any, Callable, Dict, Union

EXECUTABLE_TYPE_INLINE = 'inline'
EXECUTABLE_TYPE_CALLABLE = 'callable'


class TransformationExecutable:

    def __init__(self, transformation: Union[CodeType, Callable], exec_type: str):
        self._transformation = transformation
        self._type = exec_type

    def process(self, data: Dict[str, Any]):
        if self._type == EXECUTABLE_TYPE_INLINE:
            context = {'data': data}
            exec(self._transformation, context)
        else:  # callable
            self._transformation(data)
