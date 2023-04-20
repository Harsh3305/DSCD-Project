import os
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

    def process_data(self):
        files_in_path = os.listdir(self.input_dir)
        for current_file_path in files_in_path:
            self._send_input_file_address_to_mapper(self.input_dir+"/"+current_file_path)

    def _send_input_file_address_to_mapper(self, file_path):
        address_of_mapper = self.mapper_addresses[self._round_robin_index]
        self._round_robin_index = (self._round_robin_index + 1) % len(self.mapper_addresses)

        self.send_data_to_mapper(
            mapper_address=address_of_mapper,
            input_file_path=file_path
        )
