from datetime import datetime


class CustomLogging:
    def log(self, logging_data):
        time = str(datetime.now())
        print("---------------------")
        print(time)
        print(logging_data)
        print("---------------------")
