class Tournamentcls:

    def __init__(self, Tournament_index=0, Tournament_name='unknown', Tournament_location='unknown',
                 Tournament_date='00/00/0000', Tournament_nbr_round=4, Tournament_players_id='unknown',
                 Tournament_ctl_time='BLITZ', Tournament_description='unknown', TournamentMatchID='unknow'):
        self.Tournament_index = Tournament_index
        self.Tournament_name = Tournament_name
        self.Tournament_location = Tournament_location
        self.Tournament_date = Tournament_date
        self.Tournament_nbr_round = Tournament_nbr_round
        self.Tournament_players_id = Tournament_players_id
        self.Tournament_ctl_time = Tournament_ctl_time
        self.Tournament_description = Tournament_description
        self.TournamentMatchID = TournamentMatchID

    def __int__(self, tournament):
        self.Tournament_index = tournament['Tournament_index']
        self.Tournament_name = tournament['Tournament_name']
        self.Tournament_location = tournament['Tournament_location']
        self.Tournament_date = tournament['Tournament_date']
        self.Tournament_nbr_round = tournament['Tournament_nbr_round']
        self.Tournament_players_id = tournament['Tournament_players_id']
        self.Tournament_ctl_time = tournament['Tournament_ctl_time']
        self.Tournament_description = tournament['Tournament_description']
        self.TournamentMatchID = tournament['TournamentMatchID']

    def __str__(self):
        return f"Tournamentcls: {self.Tournament_name} {self.Tournament_location} {self.Tournament_date}"

    # def __repr__(self):
    # return f"Tournamentcls: {self.Tournament_name} {self.Tournament_location} {self.Tournament_date}"

    # def add_players(self, tournament_players):
    # self.tournament_players = tournament_players

# tri des joueurs et génération des paires pour le premier round
# def get_rating(player):
# return player.rating
