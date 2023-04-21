from send_data_to_mapper import MapperCommunication
from reader import CustomIO
from customlogging import CustomLogging


class Master(MapperCommunication, CustomLogging, CustomIO):
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
        files_in_path = self.get_all_files_in_path(self.input_dir)
        mapper_files = []
        for _ in range(len(self.mapper_addresses)):
            mapper_files.append([])

        for current_file in files_in_path:
            mapper_files[self._round_robin_index].append(current_file)
            self._increment_round_robin_index()

        self._send_input_file_address_to_mapper(mapper_files)

    def _send_input_file_address_to_mapper(self, file_path: list):
        for i in range(len(self.mapper_addresses)):
            self.send_data_to_mapper(
                mapper_address=self.mapper_addresses[i],
                input_file_path=file_path[i]
            )

    def _increment_round_robin_index(self):
        self._round_robin_index = (self._round_robin_index + 1) % len(self.mapper_addresses)
