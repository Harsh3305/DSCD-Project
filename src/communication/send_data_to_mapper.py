from src.logging.customlogging import CustomLogging


class MapperCommunication(CustomLogging):
    def send_data_to_mapper(self, mapper_address: str, input_file_path: list):
        self.log({
            "map address": mapper_address,
            "input file path": input_file_path
        })
