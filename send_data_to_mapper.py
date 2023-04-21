from concurrent import futures

import grpc

import message_pb2
import message_pb2_grpc
from customlogging import CustomLogging


class MapperCommunication(message_pb2_grpc.MapperServicer):
    def send_data_to_mapper(self, mapper_address: str, input_file_path: list):
        file_name=""
        for file in input_file_path:
            if len(file_name) == 0:
                file_name += file
            else:
                file_name += " " + file

        with grpc.insecure_channel(mapper_address) as channel:
            stub = message_pb2_grpc.MapperStub(channel)
            message_request = message_pb2.MapperRequest(file_name=file_name)
            message_reply = stub.SendFileLocation(message_request)
            self.log(message_reply)

            self.log({
                "map address": mapper_address,
                "input file path": input_file_path
            })

    def SendFileLocation(self, request, context):
        file_names = request.file_name.split()
        CustomLogging().log(context)
        mapper_reply = message_pb2.MapperReply()
        return mapper_reply

    def serve_request(self, mapper_address):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        message_pb2_grpc.add_MapperServicer_to_server(self, server=server)
        server.add_insecure_port(mapper_address)
        server.start()
        server.wait_for_termination()
