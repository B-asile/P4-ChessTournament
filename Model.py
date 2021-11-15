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
        self.find_id = 0
        self.id = 0
        self.tournament_players = []
        self.lst_players_obj_sorted_by_id = []

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
    def player_sort_by_name(self):
        list_az = sorted(self.lst_playersObj, key=lambda x: x.Player_first_name.lower(), reverse=False)
        return list_az

    # Pour afficher le Classement des Joueurs
    # Classer par Rating et Afficher la liste des Joueurs de la BDD
    def player_sort_by_rating(self):
        list_rating = sorted(self.lst_playersObj, key=lambda x: int(x.Player_rating), reverse=True)
        return list_rating

    # Pour Créer de nouveaux Joueurs
    def player_index(self):
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
    def select_tounament(self):
        # Déclaration des variables pour la selection de tournois
        for selection in self.lst_tournamentsObj:
            if selection.Tournament_index == int(self.find_id):
                self.id = selection
                return selection

    def search_tournament_player(self):
        self.lst_players_obj_sorted_by_id = sorted(self.lst_playersObj, key=lambda x: x.Player_index,
                                              reverse=False)
        # Création d'une variable avec la liste des ID et liste des joueurs du Tournois
        selected_tournament_players_id = self.id.Tournament_players_id
        # Itération dans la liste des ID du Tournois
        for id in selected_tournament_players_id:
            # Itération dans la liste des Joueurs
            for Player in self.lst_players_obj_sorted_by_id:
                # Si l'ID de la liste correspond à l'ID d'un joueur de la Liste des objets joueurs
                if id == Player.Player_index:
                    # ajout à la liste des Joueurs du Tournois
                    self.tournament_players.append(Player)

    # Pour afficher les anciens Tournois et accéder aux options
    def tournaments_history(self):
        return sorted(self.lst_tournamentsObj, key=lambda x: str(x.Tournament_date), reverse=False)

    # Classement de la liste des joueurs du Tournois par nom :
    def tournament_players_by_name(self):
        return sorted(self.tournament_players, key=lambda x: x.Player_first_name.lower(), reverse=False)

    # Classement de la liste des joueurs du Tournois par rating :
    def tournament_players_by_rate(self):
        return sorted(self.tournament_players, key=lambda x: x.Player_rating, reverse=True)

    def match_by_round(self):
        lst_round = self.id.TournamentMatchID
        for round in range(int(self.id.Tournament_nbr_round)):
            list_rnd_to_display = lst_round[:4]
            print('Matchs du round ' + str(round + 1))
            for match_id in list_rnd_to_display:
                for match in self.lst_matchsObj:
                    if match_id == match.MatchID:
                        print(match)
            del lst_round[:4]


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

    def tournament_index(self):
        return int(len(self.lst_tournamentsObj)) + 1

    def add_tournament_in_class(self, tournament):
        x = Tournamentcls(tournament['Tournament_index'],
                          tournament['Tournament_name'],
                          tournament['Tournament_location'],
                          tournament['Tournament_date'],
                          tournament['Tournament_nbr_round'],
                          tournament['Tournament_players_id'],
                          tournament['Tournament_ctl_time'],
                          tournament['Tournament_description'])
        self.lst_tournamentsObj.append(x)

    def match_id(self):
        return int(len(self.lst_matchsObj)) + 1
