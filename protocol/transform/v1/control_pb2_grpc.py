# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from transform.v1 import control_pb2 as transform_dot_v1_dot_control__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in transform/v1/control_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ServerDetails = channel.unary_unary(
                '/transform.v1.control.Control/ServerDetails',
                request_serializer=transform_dot_v1_dot_control__pb2.ServerDetailsRequest.SerializeToString,
                response_deserializer=transform_dot_v1_dot_control__pb2.ServerDetailsResponse.FromString,
                _registered_method=True)
        self.HealthCheck = channel.stream_stream(
                '/transform.v1.control.Control/HealthCheck',
                request_serializer=transform_dot_v1_dot_control__pb2.HeartbeatRequest.SerializeToString,
                response_deserializer=transform_dot_v1_dot_control__pb2.HeartbeatResponse.FromString,
                _registered_method=True)
        self.LoadInlineModule = channel.unary_unary(
                '/transform.v1.control.Control/LoadInlineModule',
                request_serializer=transform_dot_v1_dot_control__pb2.LoadInlineModuleRequest.SerializeToString,
                response_deserializer=transform_dot_v1_dot_control__pb2.LoadInlineModuleResponse.FromString,
                _registered_method=True)
        self.VerifyInlineModule = channel.unary_unary(
                '/transform.v1.control.Control/VerifyInlineModule',
                request_serializer=transform_dot_v1_dot_control__pb2.VerifyInlineModuleRequest.SerializeToString,
                response_deserializer=transform_dot_v1_dot_control__pb2.VerifyInlineModuleResponse.FromString,
                _registered_method=True)
        self.VerifyExternalModule = channel.unary_unary(
                '/transform.v1.control.Control/VerifyExternalModule',
                request_serializer=transform_dot_v1_dot_control__pb2.VerifyExternalModuleRequest.SerializeToString,
                response_deserializer=transform_dot_v1_dot_control__pb2.VerifyExternalModuleResponse.FromString,
                _registered_method=True)
        self.LoadExternalModule = channel.unary_unary(
                '/transform.v1.control.Control/LoadExternalModule',
                request_serializer=transform_dot_v1_dot_control__pb2.LoadExternalModuleRequest.SerializeToString,
                response_deserializer=transform_dot_v1_dot_control__pb2.LoadExternalModuleResponse.FromString,
                _registered_method=True)


class ControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ServerDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HealthCheck(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadInlineModule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyInlineModule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyExternalModule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadExternalModule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ServerDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.ServerDetails,
                    request_deserializer=transform_dot_v1_dot_control__pb2.ServerDetailsRequest.FromString,
                    response_serializer=transform_dot_v1_dot_control__pb2.ServerDetailsResponse.SerializeToString,
            ),
            'HealthCheck': grpc.stream_stream_rpc_method_handler(
                    servicer.HealthCheck,
                    request_deserializer=transform_dot_v1_dot_control__pb2.HeartbeatRequest.FromString,
                    response_serializer=transform_dot_v1_dot_control__pb2.HeartbeatResponse.SerializeToString,
            ),
            'LoadInlineModule': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadInlineModule,
                    request_deserializer=transform_dot_v1_dot_control__pb2.LoadInlineModuleRequest.FromString,
                    response_serializer=transform_dot_v1_dot_control__pb2.LoadInlineModuleResponse.SerializeToString,
            ),
            'VerifyInlineModule': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyInlineModule,
                    request_deserializer=transform_dot_v1_dot_control__pb2.VerifyInlineModuleRequest.FromString,
                    response_serializer=transform_dot_v1_dot_control__pb2.VerifyInlineModuleResponse.SerializeToString,
            ),
            'VerifyExternalModule': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyExternalModule,
                    request_deserializer=transform_dot_v1_dot_control__pb2.VerifyExternalModuleRequest.FromString,
                    response_serializer=transform_dot_v1_dot_control__pb2.VerifyExternalModuleResponse.SerializeToString,
            ),
            'LoadExternalModule': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadExternalModule,
                    request_deserializer=transform_dot_v1_dot_control__pb2.LoadExternalModuleRequest.FromString,
                    response_serializer=transform_dot_v1_dot_control__pb2.LoadExternalModuleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'transform.v1.control.Control', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Control(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ServerDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/transform.v1.control.Control/ServerDetails',
            transform_dot_v1_dot_control__pb2.ServerDetailsRequest.SerializeToString,
            transform_dot_v1_dot_control__pb2.ServerDetailsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def HealthCheck(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/transform.v1.control.Control/HealthCheck',
            transform_dot_v1_dot_control__pb2.HeartbeatRequest.SerializeToString,
            transform_dot_v1_dot_control__pb2.HeartbeatResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LoadInlineModule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/transform.v1.control.Control/LoadInlineModule',
            transform_dot_v1_dot_control__pb2.LoadInlineModuleRequest.SerializeToString,
            transform_dot_v1_dot_control__pb2.LoadInlineModuleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def VerifyInlineModule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/transform.v1.control.Control/VerifyInlineModule',
            transform_dot_v1_dot_control__pb2.VerifyInlineModuleRequest.SerializeToString,
            transform_dot_v1_dot_control__pb2.VerifyInlineModuleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def VerifyExternalModule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/transform.v1.control.Control/VerifyExternalModule',
            transform_dot_v1_dot_control__pb2.VerifyExternalModuleRequest.SerializeToString,
            transform_dot_v1_dot_control__pb2.VerifyExternalModuleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LoadExternalModule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/transform.v1.control.Control/LoadExternalModule',
            transform_dot_v1_dot_control__pb2.LoadExternalModuleRequest.SerializeToString,
            transform_dot_v1_dot_control__pb2.LoadExternalModuleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
