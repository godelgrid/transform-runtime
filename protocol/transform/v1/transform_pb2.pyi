from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TransformRequest(_message.Message):
    __slots__ = ("transformationId", "data")
    TRANSFORMATIONID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    transformationId: str
    data: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, transformationId: _Optional[str] = ..., data: _Optional[_Iterable[str]] = ...) -> None: ...

class TransformResponse(_message.Message):
    __slots__ = ("transformationMissing", "data")
    TRANSFORMATIONMISSING_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    transformationMissing: bool
    data: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, transformationMissing: bool = ..., data: _Optional[_Iterable[str]] = ...) -> None: ...
