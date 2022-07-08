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


if __name__ == '__main__':
    logging.basicConfig()
    run()