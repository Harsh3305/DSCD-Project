def read_single_file(file_path, base_dir):
    file = open(base_dir + "/" + file_path, "r")
    content = file.read()
    return content
