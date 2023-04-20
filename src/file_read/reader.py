import os

class CustomIO:
    def read_file(self, base_url: str, file_name: str):
        full_url = base_url + "/" + file_name
        file = open(full_url, "r")
        content = file.read()
        file.close()
        return content

    def write_file(self, base_url: str, file_name: str, content: str):
        full_url = base_url + "/" + file_name
        if not os.path.exists(base_url):
            os.makedirs(base_url)
        file_content = "\n"+content
        if not os.path.isfile(full_url):
            file_content = content
            file = open(full_url, 'x')
            file.close()
        file = open(full_url, "a")
        file.writelines(file_content)
        file.close()
