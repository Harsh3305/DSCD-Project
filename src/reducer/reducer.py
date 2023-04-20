from src.file_read.reader import CustomIO
from src.logging.logging import Logging


class Reducer(CustomIO, Logging):
    def __init__(
            self,
            address: str,
            intermediate_file_path: str,
            output_file_path: str,
            index: int
    ):
        self.address = address
        self.intermediate_file_path = intermediate_file_path
        self.output_file_path = output_file_path
        self.index = index
        self.invert_index = {}

    def process_files(self):
        files = self.get_all_files_in_path(self.intermediate_file_path)
        for file in files:
            self.process_file(file_name=file)
        self._store_data_in_file()

    def process_file(self, file_name: str):
        content = self.read_file(base_url=self.intermediate_file_path, file_name=file_name).split("\n")
        self.shuffle_and_sort(content)
        for data_entry in content:
            data_entry = data_entry.split(" ")
            self._save_inverted_index(data_entry[0], data_entry[1])
        self._store_data_in_file()

    def shuffle_and_sort(self, content: list):
        content.sort()

    def _save_inverted_index(self, word: list, file_index: str):
        if word in self.invert_index:
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
    reduce_address = "localhost:8080"
    reduce_input_file_path = "/home/harsh/Project/DSCD/AProject/output"
    reduce_intermediate_file_path = "/home/harsh/Project/DSCD/AProject/intermediate"
    reduce = Reducer(
        address=reduce_address,
        intermediate_file_path=reduce_intermediate_file_path,
        output_file_path=reduce_input_file_path,
        index=1
    )
    reduce.process_files()
