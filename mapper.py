from concurrent import futures
import grpc

import message_pb2
import message_pb2_grpc
from reader import CustomIO
from customlogging import CustomLogging


class Mapper(CustomLogging, CustomIO, message_pb2_grpc.MapperServicer):
    def __init__(
            self,
            address: str,
            input_file_path: str,
            intermediate_file_path: str,
            index: int
    ):
        self.address = address
        self.input_file_path = input_file_path
        self.intermediate_file = intermediate_file_path
        self.index = index
        self._serve_request()

    def _serve_request(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        message_pb2_grpc.add_MapperServicer_to_server(self, server=server)
        server.add_insecure_port(self.address)
        server.start()
        server.wait_for_termination()

    def process(self, files_name: list):
        for file_name in files_name:
            data = self.read_file(file_name=file_name, base_url=self.input_file_path)
            file_index = self._get_file_index(file_name=file_name)
            self.split_into_words(data=data, file_index=file_index)

    def SendFileLocation(self, request, context):
        files_name = request.file_name.split(" ")
        self.log(request)
        mapper_reply = message_pb2.MapperReply()
        self.process(files_name=files_name)
        return mapper_reply

    def split_into_words(self, data: str, file_index: int):
        paragraph = data.split("\n")
        content = {}
        for line in paragraph:
            for word in line.split(" "):
                a = f"{word} {file_index}"
                if not a in content:
                    content[a] = ""
        data = ""
        for x in content.keys():
            if len(data) == 0:
                data += x
            else:
                data += f"\n{x}"
        self._store_in_intermediate_file(content=data)

    def _store_in_intermediate_file(self, content: str):
        self.write_file(
            file_name=f"Intermediate{self.index}.txt",
            content=content,
            base_url=self.intermediate_file
        )

    def _get_file_index(self, file_name: str) -> int:
        file_name = file_name.replace("Input", "")
        index = file_name.replace(".txt", "")
        return int(index)


if __name__ == "__main__":
    mapper_address = input("Enter mapper address: ")
    index = int(input("Enter id of mapper (eg 1): "))
    mapper_input_file_path = "/home/harsh/Project/DSCD/DSCD-Project/input"
    mapper_intermediate_file_path = "/home/harsh/Project/DSCD/DSCD-Project/intermediate"
    m = Mapper(
        address=mapper_address,
        input_file_path=mapper_input_file_path,
        intermediate_file_path=mapper_intermediate_file_path,
        index=index
    )
