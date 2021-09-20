from tinydb import TinyDB, Query

from Playercls import Playercls
from DB import DB
from Tournamentcls import Tournamentcls


class Model:
    def __init__(self):
        # variables de model
        self.db = DB()
        self.all_playersObj = self.load_players()
        self.all_tournamentsObj = self.load_tournaments()
        #self.player = {}

    def load_players(self):
        # DB.create_table_player()
        players = []
        for player in self.db.load_players():
            player = Playercls(player['last_name'],
                               player['first_name'],
                               player['date_of_birth'],
                               player['gender'],
                               player['rating'])
            print(f"chargement joueur:{player.first_name}{player.last_name}")
            players.append(player)
        return players

    def add_player(self, last_name, first_name, date_of_birth, gender, rating):
        player = Playercls( last_name,
                            first_name,
                            date_of_birth,
                            gender,
                            rating)
        self.all_playersObj.append(player)

    def save_players(self):
        self.db.save_players(self.all_playersObj)
    '''
    def load_tournaments(self):
        # DB.create_table_tournament()
        for tournament in DB.table_tournaments:
            tournament = Tournamentcls(tournament['id'],
                                       tournament['name'],
                                       tournament['location'],
                                       tournament['tournament_players'],
                                       tournament['nbr_round'],
                                       tournament['ctl_time'],
                                       tournament['description'])
            print(f"chargement tournoi:{tournament.name}{tournament.date}")
            self.all_tournamentsObj.append(tournament)

    @staticmethod
    def delete_all_table():
        DB.clean_db()

    def save_players(self):
        for Player in self.all_playersObj:
            DB.table_players.insert(Player.__dict__)


    def save_tournaments(self):
        for Tournament in self.all_tournamentsObj:
            DB.table_tournaments.insert(Tournament.__dict__)

# Classer par Nom et Afficher la liste Joueurs de la BDD

    def get_first_name(self): # player ou Tournament (playercls pr moi???)
        list_az = sorted(self.all_playersObj, key=lambda x: x.first_name, reverse=False)
        return list_az


# Classer par Rating et Afficher la liste des Joueurs de la BDD
    def get_rating(self):
        list_rating = sorted(self.all_playersObj, key=lambda x: x.rating, reverse=True)
        return list_rating
'''
# gérer id
    def id_player(self):
        self.id_player = int(len(self.all_playersObj)) + 1

    def add_new_player(self, last_name, first_name, date_of_birth, gender, rating):
        np = Playercls(last_name,
                       first_name,
                       date_of_birth,
                       gender,
                       rating)
        self.all_playersObj.append(np)
        # return f"chargement joueur:{np.first_name} {np.last_name}"

    def get_id_tournament(self):
        list_id_tournament = sorted(self.all_tournamentsObj, key=lambda x: x.id, reverse=False)
        return list_id_tournament

    def id_tournament(self):
        self.id_tournament = int(len(self.all_tournamentsObj)) + 1


    def add_new_tournament(self, name, location, tournament_players, date, nbr_round, ctl_time, description):
        nt = Tournamentcls(name, location, tournament_players, date, nbr_round, ctl_time, description)
        self.all_tournamentsObj.append(nt)
        # return f"chargement joueur:{nt.id} {nt.name} {nt.location}"

    def info_t_get_name(self):
        list_info_t_get_name = sorted(self.all_tournamentsObj, key=lambda x: x.name, reverse=False)
        return list_info_t_get_name

    # Classer par Nom et Afficher la liste Joueurs de la BDD
    def sort_by_name(self):
        list_az = sorted(self.all_playersObj, key=lambda x: x.first_name, reverse=False)
        return list_az

    # Classer par Rating et Afficher la liste des Joueurs de la BDD
    def sort_by_rating(self):
        list_rating = sorted(self.all_playersObj, key=lambda x: x.rating, reverse=True)
        return list_rating

    def save_tournaments(self):
        self.db.save_tournaments(self.all_tournamentsObj)

    def load_tournaments(self):
        tournaments = []
        for tournament in self.db.load_tournament():
            tournaments.append(Tournamentcls(
                                       tournament['name'],
                                       tournament['location'],
                                       tournament['tournament_players'],
                                       tournament['nbr_round'],
                                       tournament['ctl_time'],
                                       tournament['description']) )
        return tournaments