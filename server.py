import logging
import os
import signal
import sys
from concurrent import futures

import grpc
import watchtower

from protocol.transform.v1 import control_pb2_grpc, transform_pb2_grpc
from services.service_factory import SERVICE_FACTORY, ServiceFactory
from shutdown_hook import ShutdownHook

logger = logging.getLogger(__name__)


class Server:

    def __init__(self, service_factory: ServiceFactory, socket_path: str):
        self._service_factory = service_factory
        self._socket_path = socket_path
        self._server = None

    def start(self):
        # Create a gRPC server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        # Add services to server
        control_pb2_grpc.add_ControlServicer_to_server(self._service_factory.get_control_service(), server)
        transform_pb2_grpc.add_TransformServicer_to_server(self._service_factory.get_transform_service(), server)

        # Remove the socket file if it already exists
        if os.path.exists(socket_path):
            os.unlink(socket_path)

        # Add the Unix domain socket listener
        server.add_insecure_port("unix://" + socket_path)

        # Start the server
        server.start()
        logger.info("Server started. Listening on Unix domain socket: " + socket_path)
        self._server = server

    def shutdown(self):
        self._server.stop(0)

    def await_termination(self):
        self._server.wait_for_termination()


if __name__ == "__main__":
    server_args = sys.argv
    if len(server_args) < 3:
        print('Usage: server.py <socket_path> <use_cloudwatch_logging>')
        exit(1)
    socket_path = server_args[1]
    use_cloudwatch = "true" == server_args[2].lower()
    root_logger = logging.getLogger()
    handlers = []
    if use_cloudwatch:
        handlers.append(watchtower.CloudWatchLogHandler(log_group_name='grid_transform_runtime',
                                                        log_stream_name='grid_transform_runtime',
                                                        log_group_retention_days=7))
    else:
        handlers.append(logging.StreamHandler(sys.stdout))
        handlers.append(logging.FileHandler('/tmp/transform-runtime.log'))

    for handler in handlers:
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        root_logger.addHandler(handler)

    root_logger.setLevel(logging.INFO)
    SERVICE_FACTORY.load_services()
    server = Server(SERVICE_FACTORY, socket_path)


    def shutdown_callback():
        root_logger.info("*** Shutting down transform runtime ***")
        server.shutdown()
        SERVICE_FACTORY.get_process_monitor_service().shutdown()
        handler.flush()
        SERVICE_FACTORY.get_process_monitor_service().await_shutdown(timeout=10)
        root_logger.info("*** Transform runtime shutdown ***")
        sys.exit(0)


    shutdown_hook = ShutdownHook(shutdown_callback=shutdown_callback)
    shutdown_hook.start()


    def signal_handler(sig, fr):
        shutdown_hook.shutdown()


    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    SERVICE_FACTORY.get_process_monitor_service().start(shutdown_hook=shutdown_hook)
    server.start()
    # Keep the server running until terminated
    try:
        server.await_termination()
    except KeyboardInterrupt:
        shutdown_hook.shutdown()
