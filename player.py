
class Playercls:
    def __init__(self, Player_index=0, Player_first_name='unknown', Player_last_name='unknown', Player_age=0,
                 Player_date_of_birth='00/00/0000', Player_gender='unknown', Player_rating=0.0, Player_score=0.0):
        self.Player_index = Player_index
        self.Player_first_name = Player_first_name
        self.Player_last_name = Player_last_name
        self.Player_age = Player_age
        self.Player_date_of_birth = Player_date_of_birth
        self.Player_gender = Player_gender
        self.Player_rating = Player_rating
        self.Player_score = Player_score

    def _int__(self, player):
        self.Player_index = player['Player_index']
        self.Player_first_name = player['Player_first_name']
        self.Player_last_name = player['Player_last_name']
        self.Player_age = player['Player_age']
        self.Player_date_of_birth = player['Player_date_of_birth']
        self.Player_gender = player['Player_gender']
        self.Player_rating = player['Player_rating']
        self.Player_score = player['Player_score']

    def __str__(self):
        return f" {self.Player_first_name} {self.Player_last_name}"

    # def __repr__(self):
        # return f"Playercls: {self.Player_first_name} {self.Player_last_name} [{self.Player_rating}]"
