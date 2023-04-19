from datetime import datetime


class Logging:
    def log(self, logging_data):
        time = str(datetime.now())
        print("---------------------")
        print(time)
        print(logging_data)
        print("---------------------")
