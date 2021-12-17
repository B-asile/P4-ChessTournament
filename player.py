
class Player:
    def __init__(self, player_index=0, player_first_name='unknown', player_last_name='unknown', player_age=0,
                 player_date_of_birth='00/00/0000', player_gender='unknown', player_rating=0.0, player_score=0.0):
        self.player_index = player_index
        self.player_first_name = player_first_name
        self.player_last_name = player_last_name
        self.player_age = player_age
        self.player_date_of_birth = player_date_of_birth
        self.player_gender = player_gender
        self.player_rating = player_rating
        self.player_score = player_score

    def __str__(self):
        return f" {self.player_first_name} {self.player_last_name}"

    # def __repr__(self):
        # return f"Player: {self.player_first_name} {self.player_last_name} [{self.player_rating}]"
