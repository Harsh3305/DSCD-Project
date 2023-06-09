import math
from concurrent import futures
import grpc

import message_pb2
import message_pb2_grpc
from reader import CustomIO
from customlogging import CustomLogging


class Reducer(CustomIO, CustomLogging, message_pb2_grpc.ReducerServicer):
    def __init__(
            self,
            address: str,
            intermediate_file_path: str,
            output_file_path: str,
            index: int
    ):
        self.file_pattern = None
        self.address = address
        self.intermediate_file_path = intermediate_file_path
        self.output_file_path = output_file_path
        self.index = index
        self.invert_index = {}
        self._serve_request()
        self.current_index = None
        self.total_size = None

    def _serve_request(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        message_pb2_grpc.add_ReducerServicer_to_server(self, server=server)
        server.add_insecure_port(self.address)
        server.start()
        server.wait_for_termination()

    def SendFilePattern(self, request, context):
        self.file_pattern = request.file_name_pattern
        self.log(request)
        mapper_reply = message_pb2.ReducerReply()
        self.process_files()
        self.log(f"Reducer-{self.index} job is done")
        return mapper_reply

    def process_files(self):
        files = self.get_all_files_in_path(self.intermediate_file_path)
        for file in files:
            self.process_file(file_partition_path=file)
        self._store_data_in_file()

    def process_file(self, file_partition_path: str):
        content = self.read_file(
            base_url=f"{self.intermediate_file_path}/{file_partition_path}",
            file_name=self.file_pattern
        ).split("\n")
        self.shuffle_and_sort(content)
        for data_entry in content:
            data_entry = data_entry.split(" ")
            try:
                self._save_inverted_index(data_entry[0], data_entry[1])
            except Exception as _:
                self.log(f"{file_partition_path}/{self.file_pattern}.txt file is empty")


    def shuffle_and_sort(self, content: list):
        content.sort()

    def _save_inverted_index(self, word: list, file_index: str):
        if word in self.invert_index.keys():
            self.invert_index[word].add(file_index)
        else:
            self.invert_index[word] = {file_index}

    def _store_data_in_file(self):
        unique_words = list(self.invert_index.keys())
        content = ""
        for word in unique_words:
            files = list(self.invert_index[word])
            files_name = ""
            for file in files:
                file = str(file)
                # String formatting
                file = file.replace("Intermediate", "")
                file = file.replace(".txt", "")
                #
                if len(files_name) == 0:
                    files_name += file
                else:
                    files_name += f", {file}"
            if len(content) > 0:
                content += f"\n{word} {files_name}"
            else:
                content += f"{word} {files_name}"
        self.write_file(base_url=self.output_file_path, file_name=f"Output{self.index}.txt", content=content)


if __name__ == "__main__":
    reduce_address = input("Enter reducer address: ")
    index = int(input("Enter id of reducer (eg 1): "))
    reduce_input_file_path = "/home/harsh/Project/DSCD/DSCD-Project/output"
    reduce_intermediate_file_path = "/home/harsh/Project/DSCD/DSCD-Project/intermediate"
    reduce = Reducer(
        address=reduce_address,
        intermediate_file_path=reduce_intermediate_file_path,
        output_file_path=reduce_input_file_path,
        index=index
    )
    reduce.process_files()
