from tinydb import TinyDB
from chess_app.models.tournament import Tournament
from chess_app.models.player import Player
from chess_app.models.match import Match


class DB:

    def __init__(self):
        self.db = TinyDB('chess_app/stored_data.json')
        self.table_players = self.db.table('Player')
        self.table_matchs = self.db.table('Matchs')
        self.table_tournaments = self.db.table('Tournament')
        self.lst_playersobj = []
        self.lst_tournamentsobj = []
        self.lst_matchsobj = []
        self.find_id = 0
        self.id = 0
        self.tournament_players = []
        self.lst_players_obj_sorted_by_id = []
        self.tournament_match_id_in_instance = []
        self.list1 = []
        self.list2 = []
        self.player_in_instance = []
        self.nbr_players_by_list = 0
        self.new_match = None
        self.new_tournament = None
        self.new_player = None

    @staticmethod
    def TinyDBDropTables():
        DB.db.drop_tables()

    def load_tournaments(self):
        """
        1. Fonction Import données Saved BDD vers Mémoire Programme :
        import des tournois.
        """
        for kwargs_tournament in self.table_tournaments:
            data_tournament = Tournament(tournament_index=kwargs_tournament['tournament_index'],
                                         tournament_name=kwargs_tournament['tournament_name'],
                                         tournament_location=kwargs_tournament['tournament_location'],
                                         tournament_date=kwargs_tournament['tournament_date'],
                                         tournament_nbr_round=kwargs_tournament['tournament_nbr_round'],
                                         tournament_players_id=kwargs_tournament['tournament_players_id'],
                                         tournament_ctl_time=kwargs_tournament['tournament_ctl_time'],
                                         tournament_description=kwargs_tournament['tournament_description'],
                                         tournament_match_id=kwargs_tournament['tournament_match_id'])
            self.lst_tournamentsobj.append(data_tournament)
        print(self.lst_tournamentsobj)

    def load_players(self):
        """Fonction Import Joueurs"""
        for kwargs_player in self.table_players:
            data_player = Player(player_index=kwargs_player['player_index'],
                                 player_first_name=kwargs_player['player_first_name'],
                                 player_last_name=kwargs_player['player_last_name'],
                                 player_age=kwargs_player['player_age'],
                                 player_date_of_birth=kwargs_player['player_date_of_birth'],
                                 player_gender=kwargs_player['player_gender'],
                                 player_rating=kwargs_player['player_rating'],
                                 player_score=kwargs_player['player_score'])
            self.lst_playersobj.append(data_player)
        print(self.lst_playersobj)

    def load_matchs(self):
        """Fonction import des matchs"""
        for kwargs_match in self.table_matchs:
            data_match = Match(match_id=kwargs_match['match_id'],
                               match_player1=kwargs_match['match_player1'],
                               match_score1=kwargs_match['match_score1'],
                               match_player2=kwargs_match['match_player2'],
                               match_score2=kwargs_match['match_score2'], )
            self.lst_matchsobj.append(data_match)
        print(self.lst_matchsobj)


    def erase_tables(self):
        """
        2. Fonction Sauvegarde des données vers BDD :
        Fonction Suppression anciennes Tables pour nouvelle sauvegarde
        """
        self.db.drop_tables()

    def save_players(self):
        """ Sauvegarde Joueurs"""
        for player in self.lst_playersobj:
            self.table_players.insert(player.__dict__)

    def save_tournaments(self):
        """ sauvegarde des tournois"""
        for tournament in self.lst_tournamentsobj:
            self.table_tournaments.insert(tournament.__dict__)

    def save_matchs(self):
        """sauvegarde de matchs"""
        for match in self.lst_matchsobj:
            self.table_matchs.insert(match.__dict__)
