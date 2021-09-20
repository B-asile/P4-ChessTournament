from DB import DB


class Playercls:
    def __init__(self, last_name, first_name, date_of_birth, gender, rating=0):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rating = rating

    def __str__(self):
        return f"Playercls: {self.first_name} {self.last_name} [{self.rating}]"

    #def __repr__(self):
    #    return f"Playercls: {self.first_name} {self.last_name} [{self.rating}]"

