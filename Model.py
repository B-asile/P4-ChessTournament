from Tournamentcls import Tournamentcls
from Playercls import Playercls
from Matchcls import Matchcls
from DB import DBcls


class Model:
    def __init__(self):
        # variables de model
        self.lst_playersObj = []
        self.lst_tournamentsObj = []
        self.lst_matchsObj = []

    # 1. Fonction Import données Saved BDD vers Mémoire Programme
    # Fonction Import Tournois
    def load_tournaments(self):
        for tournament in DBcls.table_tournaments:
            t = Tournamentcls(tournament['Tournament_index'],
                              tournament['Tournament_name'],
                              tournament['Tournament_location'],
                              tournament['Tournament_date'],
                              tournament['Tournament_nbr_round'],
                              tournament['Tournament_players_id'],
                              tournament['Tournament_ctl_time'],
                              tournament['Tournament_description'],
                              tournament['TournamentMatchID'])
            self.lst_tournamentsObj.append(t)
            # print(t)
        print(self.lst_tournamentsObj)

    # Fonction Import Joueurs
    def load_players(self):
        for player in DBcls.table_players:
            p = Playercls(player['Player_index'],
                          player['Player_first_name'],
                          player['Player_last_name'],
                          player['Player_age'],
                          player['Player_date_of_birth'],
                          player['Player_gender'],
                          player['Player_rating'],
                          player['Player_score'])
            self.lst_playersObj.append(p)
            # print(p)
        print(self.lst_playersObj)

    # fonction import des matchs
    def load_matchs(self):
        for match in DBcls.table_matchs:
            m = Matchcls(match['MatchID'],
                         match['MatchP1'],
                         match['MatchS1'],
                         match['MatchP2'],
                         match['MatchS2'])
            self.lst_matchsObj.append(m)
            # print(m)
        print(self.lst_matchsObj)

    # 2. Fonction Sauvegarde des données vers BDD (écraser tout)
    # Fonction Suppression anciennes Tables pour nouvelle sauvegarde
    @staticmethod
    def erase_tables():
        DBcls.TinyDBDropTables()

    # Fonction Sauvegarde Joueurs
    def save_players(self):
        for player in self.lst_playersObj:
            DBcls.table_players.insert(player.__dict__)

    # Fonction Sauvegarde Tournois
    def save_tournaments(self):
        for tournament in self.lst_tournamentsObj:
            DBcls.table_tournaments.insert(tournament.__dict__)

    def save_matchs(self):
        for match in self.lst_matchsObj:
            DBcls.table_matchs.insert(match.__dict__)

    # """"""""""""""""""""""""""""""""""""""""""""""

    # FONCTIONS D'OPERATIONS :

    # 1. Section Player :
    # Pour afficher la liste des Joueurs par ordre alphabétique
    # Classer par Nom et Afficher la liste Joueurs de la BDD
    def sort_by_name(self):
        list_az = sorted(self.lst_playersObj, key=lambda x: x.Player_first_name.lower(), reverse=False)
        return list_az

    # Pour afficher le Classement des Joueurs
    # Classer par Rating et Afficher la liste des Joueurs de la BDD
    def sort_by_rating(self):
        list_rating = sorted(self.lst_playersObj, key=lambda x: int(x.Player_rating), reverse=True)
        return list_rating

    # Pour Créer de nouveaux Joueurs
    def Player_index(self):
        return int(len(self.lst_playersObj)) + 1

    def add_player_in_class(self, player):
        x = Playercls(player['Player_index'],
                      player['Player_first_name'],
                      player['Player_last_name'],
                      player['Player_age'],
                      player['Player_date_of_birth'],
                      player['Player_gender'],
                      player['Player_rating'],
                      player['Player_score'])
        self.lst_playersObj.append(x)

    # 2. Section Tournois :
    # Pour afficher les anciens Tournois et accéder aux options
    def tournaments_history(self):
        return sorted(self.lst_tournamentsObj, key=lambda x: str(x.Tournament_date), reverse=False)

    # Pour créer un nouveau Tournois
    @staticmethod
    def tournament_player_ids():
        # todo:print a passer dans le view
        print('Selection des Joueurs du Tournois')
        lst = []
        for x in range(1, 9):
            y = input("Entrer l'id du Player " + str(x) + " :  ")
            lst.append(int(y))
        return lst

    @staticmethod
    def tournament_ctl_time():
        # todo:print a passer dans le view
        print('*** TimeControl ***')
        x = input("1 - Pour selectionner un bullet\n"
                  "2 - Pour selectionner un blitz\n"
                  "3 - Pour selectionner un coup rapide\n")
        if x == '1': return 'BULLET'
        if x == '2': return 'BLITZ'
        if x == '3': return 'COUP RAPIDE'

    def TournamentIndex(self):
        return int(len(self.lst_tournamentsObj)) + 1

    def AddTournamentInClass(self, tournament):
        x = Tournamentcls(tournament['Tournament_index'],
                          tournament['Tournament_name'],
                          tournament['Tournament_location'],
                          tournament['Tournament_date'],
                          tournament['Tournament_nbr_round'],
                          tournament['Tournament_players_id'],
                          tournament['Tournament_ctl_time'],
                          tournament['Tournament_description'])
        self.lst_tournamentsObj.append(x)

    def MatchID(self):
        return int(len(self.lst_matchsObj)) + 1
