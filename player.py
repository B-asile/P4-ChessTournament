
class Player:
    def __init__(self, **kwargs_player):
        for key, value in kwargs_player.items():
            setattr(self, key, value)
        # self.player_index = player_index
        # self.player_first_name = player_first_name
        # self.player_last_name = player_last_name
        # self.player_age = player_age
        # self.player_date_of_birth = player_date_of_birth
        # self.player_gender = player_gender
        # self.player_rating = player_rating
        # self.player_score = player_score

    def __str__(self):
        return f" {self.player_first_name} {self.player_last_name}"

    # def __repr__(self):
        # return f"Player: {self.player_first_name} {self.player_last_name} [{self.player_rating}]"
