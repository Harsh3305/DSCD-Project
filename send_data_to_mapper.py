import grpc

import message_pb2
import message_pb2_grpc
from customlogging import CustomLogging


class MapperCommunication:
    def send_data_to_mapper(self, mapper_address: str, input_file_path: list, number_of_reducer: int):
        file_name = ""
        for file in input_file_path:
            if len(file_name) == 0:
                file_name += file
            else:
                file_name += " " + file

        with grpc.insecure_channel(mapper_address) as channel:
            stub = message_pb2_grpc.MapperStub(channel)
            message_request = message_pb2.MapperRequest(file_name=file_name, number_of_reducers=number_of_reducer)
            message_reply = stub.SendFileLocation(message_request)
            CustomLogging().log({
                "map address": mapper_address,
                "input file path": input_file_path
            })
            return message_reply

    def send_data_to_reducer(self, reducer_address: str, file_name_pattern: str):
        with grpc.insecure_channel(reducer_address) as channel:
            stub = message_pb2_grpc.ReducerStub(channel=channel)
            message_request = message_pb2.ReducerRequest(file_name_pattern=file_name_pattern)
            message_reply = stub.SendFilePattern(message_request)

            CustomLogging().log({
                "reduce address": reducer_address,
                "file name pattern": file_name_pattern
            })
            return message_reply
