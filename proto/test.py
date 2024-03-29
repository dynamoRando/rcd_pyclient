from email import message
import logging

import grpc
import rcdp_pb2
import rcdp_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = rcdp_pb2_grpc.SQLClientStub(channel)
        response = stub.IsOnline(
            rcdp_pb2.TestRequest(requestEchoMessage='test1'))
    print("Greeter client received: " + response.replyEchoMessage)


def test_create_db():
    auth = rcdp_pb2.AuthRequest(userName="tester", pw="123456")
    request = rcdp_pb2.CreateUserDatabaseRequest(
        authentication=auth, databaseName="test_create_db.db")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = rcdp_pb2_grpc.SQLClientStub(channel)
        response = stub.CreateUserDatabase(request)
    print("Greeter client received: " + str(response.isCreated))


if __name__ == '__main__':
    logging.basicConfig()
    run()
    test_create_db()

# https://grpc.io/docs/languages/python/basics/
# https://realpython.com/python-microservices-grpc/
# run this from the "proto" directory
# python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. rcdp.proto
