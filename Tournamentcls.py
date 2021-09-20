from DB import DB

class Tournamentcls:
    def __init__(self, name, location, tournament_players, date, nbr_round=4, ctl_time='blitz',
                 description=''):
        self.name = name
        self.location = location
        self.date = date
        self.tournament_players = tournament_players
        self.nbr_round = nbr_round
        self.ctl_time = ctl_time
        self.description = description

    def __str__(self):
        return f"Tournamentcls: {self.name} {self.location} {self.date}"

###    def __repr__(self):
#        return f"Tournamentcls: {self.name} {self.location} {self.date}"





    # def add_players(self, tournament_players):
        # self.tournament_players = tournament_players


# tri des joueurs et génération des paires pour le premier round
# def get_rating(player):
    # return player.rating
