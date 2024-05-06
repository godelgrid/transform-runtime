from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TransformRequest(_message.Message):
    __slots__ = ("transformer_id", "data")
    TRANSFORMER_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    transformer_id: str
    data: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, transformer_id: _Optional[str] = ..., data: _Optional[_Iterable[str]] = ...) -> None: ...

class TransformResponse(_message.Message):
    __slots__ = ("transformer_missing", "data")
    TRANSFORMER_MISSING_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    transformer_missing: bool
    data: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, transformer_missing: bool = ..., data: _Optional[_Iterable[str]] = ...) -> None: ...
