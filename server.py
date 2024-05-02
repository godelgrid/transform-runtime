import os
from concurrent import futures

import grpc

from protocol.transform.v1 import control_pb2_grpc, transform_pb2_grpc
from services.control_service import ControlService
from services.transform_service import TransformService


def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add services to server
    control_pb2_grpc.add_ControlServicer_to_server(ControlService(), server)
    transform_pb2_grpc.add_TransformServicer_to_server(TransformService(), server)

    # Define the Unix domain socket path
    socket_path = "/tmp/gridTransform.sock"

    # Remove the socket file if it already exists
    if os.path.exists(socket_path):
        os.unlink(socket_path)

    # Add the Unix domain socket listener
    server.add_insecure_port("unix://" + socket_path)

    # Start the server
    server.start()
    print("Server started. Listening on Unix domain socket", socket_path)

    # Keep the server running until terminated
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
