from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalRepoType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_REPO: _ClassVar[ExternalRepoType]
    GITHUB: _ClassVar[ExternalRepoType]
    GITLAB: _ClassVar[ExternalRepoType]
    BIT_BUCKET: _ClassVar[ExternalRepoType]
UNKNOWN_REPO: ExternalRepoType
GITHUB: ExternalRepoType
GITLAB: ExternalRepoType
BIT_BUCKET: ExternalRepoType

class ServerDetailsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ServerDetailsResponse(_message.Message):
    __slots__ = ("serverPid",)
    SERVERPID_FIELD_NUMBER: _ClassVar[int]
    serverPid: str
    def __init__(self, serverPid: _Optional[str] = ...) -> None: ...

class HeartbeatRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HeartbeatResponse(_message.Message):
    __slots__ = ("healthy",)
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    healthy: bool
    def __init__(self, healthy: bool = ...) -> None: ...

class LoadInlineModuleRequest(_message.Message):
    __slots__ = ("transformationId", "script")
    TRANSFORMATIONID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    transformationId: str
    script: str
    def __init__(self, transformationId: _Optional[str] = ..., script: _Optional[str] = ...) -> None: ...

class LoadInlineModuleResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class VerifyInlineModuleRequest(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: str
    def __init__(self, script: _Optional[str] = ...) -> None: ...

class VerifyInlineModuleResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class VerifyExternalModuleRequest(_message.Message):
    __slots__ = ("transformationId", "repoType", "repoPath", "repoRef", "accessToken", "modulePath", "requirementsPath", "transformationName", "transformationArgs", "transformationKwargs")
    TRANSFORMATIONID_FIELD_NUMBER: _ClassVar[int]
    REPOTYPE_FIELD_NUMBER: _ClassVar[int]
    REPOPATH_FIELD_NUMBER: _ClassVar[int]
    REPOREF_FIELD_NUMBER: _ClassVar[int]
    ACCESSTOKEN_FIELD_NUMBER: _ClassVar[int]
    MODULEPATH_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTSPATH_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONNAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONARGS_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONKWARGS_FIELD_NUMBER: _ClassVar[int]
    transformationId: str
    repoType: ExternalRepoType
    repoPath: str
    repoRef: str
    accessToken: str
    modulePath: str
    requirementsPath: str
    transformationName: str
    transformationArgs: str
    transformationKwargs: str
    def __init__(self, transformationId: _Optional[str] = ..., repoType: _Optional[_Union[ExternalRepoType, str]] = ..., repoPath: _Optional[str] = ..., repoRef: _Optional[str] = ..., accessToken: _Optional[str] = ..., modulePath: _Optional[str] = ..., requirementsPath: _Optional[str] = ..., transformationName: _Optional[str] = ..., transformationArgs: _Optional[str] = ..., transformationKwargs: _Optional[str] = ...) -> None: ...

class VerifyExternalModuleResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class LoadExternalModuleRequest(_message.Message):
    __slots__ = ("transformationId", "repoType", "repoPath", "repoRef", "accessToken", "modulePath", "requirementsPath", "transformationName", "transformationArgs", "transformationKwargs")
    TRANSFORMATIONID_FIELD_NUMBER: _ClassVar[int]
    REPOTYPE_FIELD_NUMBER: _ClassVar[int]
    REPOPATH_FIELD_NUMBER: _ClassVar[int]
    REPOREF_FIELD_NUMBER: _ClassVar[int]
    ACCESSTOKEN_FIELD_NUMBER: _ClassVar[int]
    MODULEPATH_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTSPATH_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONNAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONARGS_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONKWARGS_FIELD_NUMBER: _ClassVar[int]
    transformationId: str
    repoType: ExternalRepoType
    repoPath: str
    repoRef: str
    accessToken: str
    modulePath: str
    requirementsPath: str
    transformationName: str
    transformationArgs: str
    transformationKwargs: str
    def __init__(self, transformationId: _Optional[str] = ..., repoType: _Optional[_Union[ExternalRepoType, str]] = ..., repoPath: _Optional[str] = ..., repoRef: _Optional[str] = ..., accessToken: _Optional[str] = ..., modulePath: _Optional[str] = ..., requirementsPath: _Optional[str] = ..., transformationName: _Optional[str] = ..., transformationArgs: _Optional[str] = ..., transformationKwargs: _Optional[str] = ...) -> None: ...

class LoadExternalModuleResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...
