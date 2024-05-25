from types import CodeType
from typing import Any, Callable, Dict, List, Union

from gdtransform.introspect import is_batch_transformation as check_batch_transformation

EXECUTABLE_TYPE_INLINE = 'inline'
EXECUTABLE_TYPE_CALLABLE = 'callable'


class TransformationExecutable:

    def __init__(self, transformation_id: str, transformation: Union[CodeType, Callable], exec_type: str):
        self._transformation_id = transformation_id
        self._transformation = transformation
        self._type = exec_type

    def get_transformation_id(self):
        return self._transformation_id

    def process(self, data: Union[Dict[str, Any], List[Dict[str, Any]]]):
        if self._type == EXECUTABLE_TYPE_INLINE:
            context = {'data': data}
            exec(self._transformation, context)
        else:  # callable
            self._transformation(data)

    def is_batch_transformation(self):
        return self._type == EXECUTABLE_TYPE_CALLABLE and check_batch_transformation(self._transformation)
