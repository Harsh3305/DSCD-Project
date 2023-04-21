import grpc

import message_pb2
import message_pb2_grpc
from customlogging import CustomLogging


class MapperCommunication:
    def send_data_to_mapper(self, mapper_address: str, input_file_path: list):
        file_name = ""
        for file in input_file_path:
            if len(file_name) == 0:
                file_name += file
            else:
                file_name += " " + file

        with grpc.insecure_channel(mapper_address) as channel:
            stub = message_pb2_grpc.MapperStub(channel)
            message_request = message_pb2.MapperRequest(file_name=file_name)
            message_reply = stub.SendFileLocation(message_request)
            CustomLogging().log({
                "map address": mapper_address,
                "input file path": input_file_path
            })
            return message_reply

