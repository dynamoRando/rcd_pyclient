from email import message
import logging

import grpc
import cdata_pb2
import cdata_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cdata_pb2_grpc.SQLClientStub(channel)
        response = stub.IsOnline(cdata_pb2.TestRequest(requestEchoMessage='test1'))
    print("Greeter client received: " + response.replyEchoMessage)


def test_create_db():
    auth = cdata_pb2.AuthRequest(userName="tester", pw = "1234")
    request = cdata_pb2.CreateUserDatabaseRequest(authentication=auth, databaseName = "test_create_db.db")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cdata_pb2_grpc.SQLClientStub(channel)
        response = stub.CreateUserDatabase(request)
    print("Greeter client received: " + str(response.isCreated))

if __name__ == '__main__':
    logging.basicConfig()
    run()
    test_create_db()