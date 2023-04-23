import threading
import time

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
        self.reducer_addresses = reducer_addresses
        self.output_dir = output_dir

    def process_data(self):
        files_in_path = self.get_all_files_in_path(self.input_dir)
        mapper_files = []
        for _ in range(len(self.mapper_addresses)):
            mapper_files.append([])

        for current_file in files_in_path:
            mapper_files[self._round_robin_index].append(current_file)
            self._increment_round_robin_index()

        self._send_input_file_address_to_mapper(mapper_files, self.number_of_reducer)
        self.log("Mapper jobs are done")
        self._send_data_to_reducer()
        self.log("Reducer jobs are done")

    def _send_input_file_address_to_mapper(self, file_path: list, number_of_reducers: int):
        threading_list = []
        for i in range(self.number_of_mapper):
            if len(file_path[i]) > 0:
                thread = threading.Thread(target=self.send_data_to_mapper, args=(
                    self.mapper_addresses[i],
                    file_path[i],
                    number_of_reducers
                ))
                thread.start()
                threading_list.append(thread)

        for thread in threading_list:
            thread.join()

    def _send_data_to_reducer(self):
        index = 0
        threading_list = []
        for reducer_address in self.reducer_addresses:
            thread = threading.Thread(target=self.send_data_to_reducer, args=(
                reducer_address,
                f"Intermediate{index}.txt"
            ))
            index += 1
            threading_list.append(thread)
        for thread in threading_list:
            thread.join()

    def _increment_round_robin_index(self):
        self._round_robin_index = (self._round_robin_index + 1) % len(self.mapper_addresses)
