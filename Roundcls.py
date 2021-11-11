import datetime

class Round:
    def __init__(self, match):
        self.start_time = datetime.datetime.now()
        self.match = match
        self.end_time = 0

    def close_round(self):
        self.end_time = datetime.datetime.now()

    def __str__(self):
        pass