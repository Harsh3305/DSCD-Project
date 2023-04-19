import os
from src.file_read import reader
from src.communication.send_data_to_mapper import MapperCommunication
from src.logging.logging import Logging


class Master(MapperCommunication, Logging):
    def __init__(
            self,
            input_dir: str,
            mapper_addresses: list,
            reducer_addresses: list,
            output_dir: str
    ):
        self.content = []
        self._round_robin_index = 0
        self.input_dir = input_dir
        self.number_of_mapper = len(mapper_addresses)
        self.mapper_addresses = mapper_addresses
        self.number_of_reducer = len(reducer_addresses)
        self.output_dir = output_dir

    def process_files(self):
        self.read_input_file()
        self.split_input()

    def read_input_file(self):
        files_in_path = os.listdir(self.input_dir)
        all_file_content = []
        for file_path in files_in_path:
            file_content = reader.read_single_file(file_path, self.input_dir)
            all_file_content.append(file_content)
        self.content = all_file_content
        self.log(f"{len(files_in_path)} files read successfully")

    def split_input(self):
        for data in self.content:
            self.send_split_data_to_mapper(data=data)

    def send_split_data_to_mapper(self, data):
        mapper_address = self.mapper_addresses[self._round_robin_index]
        self._round_robin_index = (self._round_robin_index + 1) % self.number_of_mapper
        self.send_data_to_mapper(
            mapper_address=mapper_address,
            data=data
        )
