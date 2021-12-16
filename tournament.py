class Tournament:

    def __init__(self, **kwargs_tournament):
        for key, value in kwargs_tournament.items():
            setattr(self, key, value)

    # tournament_index=0, tournament_name='unknown', tournament_location='unknown',
    #              tournament_date='00/00/0000', tournament_nbr_round=4, tournament_players_id=[],
    #              tournament_ctl_time='BLITZ', tournament_description='unknown', tournament_match_id=[]):
    #     self.tournament_index = tournament_index
    #     self.tournament_name = tournament_name
    #     self.tournament_location = tournament_location
    #     self.tournament_date = tournament_date
    #     self.tournament_nbr_round = tournament_nbr_round
    #     self.tournament_players_id = tournament_players_id
    #     self.tournament_ctl_time = tournament_ctl_time
    #     self.tournament_description = tournament_description
    #     self.tournament_match_id = tournament_match_id

    def __str__(self):
        return f"Tournament: {self.tournament_name} {self.tournament_location} {self.tournament_date}"

    # def __repr__(self):
    # return f"Tournament: {self.tournament_name} {self.tournament_location} {self.tournament_date}"
