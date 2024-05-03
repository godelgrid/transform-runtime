import logging
import os
import sys
from concurrent import futures
from typing import Callable

import grpc
import watchtower

from protocol.transform.v1 import control_pb2_grpc, transform_pb2_grpc
from services.control_service import ControlService
from services.process_monitor_service import PROCESS_MONITOR_SERVICE
from services.transform_service import TransformService

logger = logging.getLogger(__name__)


def serve(socket_path: str, shutdown_callback: Callable):
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add services to server
    control_pb2_grpc.add_ControlServicer_to_server(ControlService(), server)
    transform_pb2_grpc.add_TransformServicer_to_server(TransformService(), server)

    # Remove the socket file if it already exists
    if os.path.exists(socket_path):
        os.unlink(socket_path)

    # Add the Unix domain socket listener
    server.add_insecure_port("unix://" + socket_path)

    # Start the server
    server.start()
    logger.info("Server started. Listening on Unix domain socket: " + socket_path)

    # Keep the server running until terminated
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)
        shutdown_callback()


if __name__ == "__main__":
    server_args = sys.argv
    if len(server_args) < 3:
        print('Usage: server.py <socket_path> <use_cloudwatch_logging>')
        exit(1)
    socket_path = server_args[1]
    use_cloudwatch = "true" == server_args[2].lower()
    root_logger = logging.getLogger()
    if use_cloudwatch:
        handler = watchtower.CloudWatchLogHandler(log_group_name='grid_transform_runtime',
                                                  log_stream_name='grid_transform_runtime',
                                                  log_group_retention_days=7)
    else:
        handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


    def shutdown_runtime():
        root_logger.info("*** Transform runtime shutdown ***")
        PROCESS_MONITOR_SERVICE.shutdown()
        handler.flush()
        PROCESS_MONITOR_SERVICE.await_shutdown(timeout=10)


    serve(socket_path, shutdown_runtime)
