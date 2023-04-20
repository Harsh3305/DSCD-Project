from src.file_read.reader import CustomIO
from src.logging.logging import Logging


class Mapper(Logging, CustomIO):
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

    def process(self, files_name: list):
        for file_name in files_name:
            data = self.read_file(file_name=file_name, base_url=self.input_file_path)
            file_index = self._get_file_index(file_name=file_name)
            self.split_into_words(data=data, file_index=file_index)

    def split_into_words(self, data: str, file_index: int):
        paragraph = data.split("\n")
        for line in paragraph:
            for word in line.split(" "):
                self._store_in_intermediate_file(word=word.lower(), file_index=file_index)

    def _store_in_intermediate_file(self, word: str, file_index: int):
        self.write_file(
            file_name=f"Intermediate{self.index}.txt",
            content=f"{word} {file_index}",
            base_url=self.intermediate_file
        )

    def _get_file_index(self, file_name: str) -> int:
        file_name = file_name.replace("Input", "")
        index = file_name.replace(".txt", "")
        return int(index)


if __name__ == "__main__":
    mapper_address = "localhost:8080"
    mapper_input_file_path = "/home/harsh/Project/DSCD/AProject/input"
    mapper_intermediate_file_path = "/home/harsh/Project/DSCD/AProject/intermediate"
    m = Mapper(
        address=mapper_address,
        input_file_path=mapper_input_file_path,
        intermediate_file_path=mapper_intermediate_file_path,
        index=1
    )
    m.process(["Input1.txt", "Input2.txt"])
