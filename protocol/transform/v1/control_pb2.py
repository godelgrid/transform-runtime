# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transform/v1/control.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1atransform/v1/control.proto\x12\x14transform.v1.control\"\x16\n\x14ServerDetailsRequest\"*\n\x15ServerDetailsResponse\x12\x11\n\tserverPid\x18\x01 \x01(\t\"\x12\n\x10HeartbeatRequest\"$\n\x11HeartbeatResponse\x12\x0f\n\x07healthy\x18\x01 \x01(\x08\"A\n\x17LoadInlineModuleRequest\x12\x16\n\x0etransformer_id\x18\x01 \x01(\t\x12\x0e\n\x06script\x18\x02 \x01(\t\":\n\x18LoadInlineModuleResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"+\n\x19VerifyInlineModuleRequest\x12\x0e\n\x06script\x18\x01 \x01(\t\"<\n\x1aVerifyInlineModuleResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t2\xc1\x03\n\x07\x43ontrol\x12h\n\rServerDetails\x12*.transform.v1.control.ServerDetailsRequest\x1a+.transform.v1.control.ServerDetailsResponse\x12`\n\x0bHealthCheck\x12&.transform.v1.control.HeartbeatRequest\x1a\'.transform.v1.control.HeartbeatResponse(\x01\x12q\n\x10LoadInlineModule\x12-.transform.v1.control.LoadInlineModuleRequest\x1a..transform.v1.control.LoadInlineModuleResponse\x12w\n\x12VerifyInlineModule\x12/.transform.v1.control.VerifyInlineModuleRequest\x1a\x30.transform.v1.control.VerifyInlineModuleResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transform.v1.control_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SERVERDETAILSREQUEST']._serialized_start=52
  _globals['_SERVERDETAILSREQUEST']._serialized_end=74
  _globals['_SERVERDETAILSRESPONSE']._serialized_start=76
  _globals['_SERVERDETAILSRESPONSE']._serialized_end=118
  _globals['_HEARTBEATREQUEST']._serialized_start=120
  _globals['_HEARTBEATREQUEST']._serialized_end=138
  _globals['_HEARTBEATRESPONSE']._serialized_start=140
  _globals['_HEARTBEATRESPONSE']._serialized_end=176
  _globals['_LOADINLINEMODULEREQUEST']._serialized_start=178
  _globals['_LOADINLINEMODULEREQUEST']._serialized_end=243
  _globals['_LOADINLINEMODULERESPONSE']._serialized_start=245
  _globals['_LOADINLINEMODULERESPONSE']._serialized_end=303
  _globals['_VERIFYINLINEMODULEREQUEST']._serialized_start=305
  _globals['_VERIFYINLINEMODULEREQUEST']._serialized_end=348
  _globals['_VERIFYINLINEMODULERESPONSE']._serialized_start=350
  _globals['_VERIFYINLINEMODULERESPONSE']._serialized_end=410
  _globals['_CONTROL']._serialized_start=413
  _globals['_CONTROL']._serialized_end=862
# @@protoc_insertion_point(module_scope)
