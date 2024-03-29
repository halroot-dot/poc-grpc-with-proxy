# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print("request.name:", request.name)
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    print("server start!")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


# def serve():
#     print("server(ssl) start!")
#     SERVER_CERTIFICATE_KEY = open("../ssl/localhost.key", "rb").read()
#     SERVER_CERTIFICATE = open("../ssl/localhost.crt", "rb").read()

#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
#     helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

#     server_credentials = grpc.ssl_server_credentials([(SERVER_CERTIFICATE_KEY, SERVER_CERTIFICATE)])
#     server.add_secure_port('localhost:50051', server_credentials)

#     server.start()
#     server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
