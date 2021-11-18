from operator import attrgetter
from Tournamentcls import Tournamentcls
from Playercls import Playercls
from Matchcls import Matchcls
import datetime
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
        self.tournament_matchid_in_instance = []
        self.list1 = []
        self.list2 = []
        self.player_in_instance = []
        self.nbr_joueurs_by_list = 0

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

    def tournament_matchid_instanced(self):
        self.tournament_matchid_in_instance = self.id.TournamentMatchID
        return (self.tournament_matchid_in_instance)

    def match2lists_creation(self):
        self.nbr_joueurs_by_list = int(len(self.tournament_players) / 2)
        # si le match commence (round = 0) tri par classement
        if int((len(self.tournament_matchid_in_instance) / 4)) == 0:
            self.player_in_instance = self.tournament_players
            self.player_in_instance_sorted = sorted(self.player_in_instance,
                                                    key=lambda x: x.Player_rating,
                                                    reverse=True)
            # for player in self.player_in_instance_sorted:
            #    print(str(player) + '  ' + str(player.Player_rating))
            # création des deux listes
            self.list1 = self.player_in_instance_sorted[:self.nbr_joueurs_by_list]
            self.list2 = self.player_in_instance_sorted[-self.nbr_joueurs_by_list:]
        # si le match est deja en cours, récupération des anciens scores
        else:
            # Remplir les Scores des joueurs de self.tournament_players avec les rouds précédents
            for index in self.id.Tournament_players_id:
                for Player in self.lst_players_obj_sorted_by_id:
                    # print(Player)
                    if index == Player.Player_index:
                        self.player_in_instance.append(Player)
            # Réinitialisation des score des joueurs
            for Player in self.player_in_instance:
                Player.Player_score = 0
            # Ajout des scores des matchs précédents
            for Player in self.player_in_instance:
                for m in self.id.TournamentMatchID:
                    for Match in self.lst_matchsObj:
                        if str(Player) == str(Match.MatchP1) and m == Match.MatchID:
                            Player.Player_score = (float(Player.Player_score) + float(Match.MatchS1))
                    for Match in self.lst_matchsObj:
                        if str(Player) == str(Match.MatchP2) and m == Match.MatchID:
                            Player.Player_score = (float(Player.Player_score) + float(Match.MatchS2))
            # for Player in self.player_in_instance:
            #     print(Player)
            #     print(Player.Player_score)
            # triage par score puis par classement
            self.player_in_instance_sorted = sorted(self.player_in_instance,
                                                    key=attrgetter('Player_score', 'Player_rating'),
                                                    reverse=True)
            # print('tri 2 : par Score puis Classement')
            # for player in self.player_in_instance_sorted:
            #    print(str(player) + '  ' + str(player.Player_score) + '  ' + str(player.Player_rating))
            # creation des deux listes
            # Elements de la liste self.player_in_instance_sorted commençant par 0 iteration 2
            self.list1 = self.player_in_instance_sorted[::2]
            # Elements de la liste self.player_in_instance_sorted commençant par 1 iteration 2
            self.list2 = self.player_in_instance_sorted[1::2]
            # Test si match deja existant dans les rounds précédents
            # pour chaque prochain round
            for i in range(self.nbr_joueurs_by_list):
                # pour chaque id de round deja fait dans ce tournois
                for m in self.id.TournamentMatchID:
                    # pour chaque matchs deja fait dans l'absolue
                    for p in self.lst_matchsObj:
                        if str(self.list1[i]) == p.MatchP1 and str(self.list2[i]) == p.MatchP2 and m == p.MatchID:
                            self.list1 = []
                            self.list1.append(self.player_in_instance_sorted[0])
                            self.list1.append(self.player_in_instance_sorted[1])
                            self.list1.append(self.player_in_instance_sorted[4])
                            self.list1.append(self.player_in_instance_sorted[5])
                            self.list2 = []
                            self.list2.append(self.player_in_instance_sorted[2])
                            self.list2.append(self.player_in_instance_sorted[3])
                            self.list2.append(self.player_in_instance_sorted[6])
                            self.list2.append(self.player_in_instance_sorted[7])
                            # print('une partie a deja été jouée, le tri a été modifié')
                            pass
                        if str(self.list1[i]) == p.MatchP2 and str(self.list2[i]) == p.MatchP1 and m == p.MatchID:
                            self.list1 = []
                            self.list1.append(self.player_in_instance_sorted[0])
                            self.list1.append(self.player_in_instance_sorted[1])
                            self.list1.append(self.player_in_instance_sorted[4])
                            self.list1.append(self.player_in_instance_sorted[5])
                            self.list2 = []
                            self.list2.append(self.player_in_instance_sorted[2])
                            self.list2.append(self.player_in_instance_sorted[3])
                            self.list2.append(self.player_in_instance_sorted[6])
                            self.list2.append(self.player_in_instance_sorted[7])
                            # print('une partie a deja été jouée, le tri a été modifié')
                            pass
                        else:
                            pass

    def match_datetime(self):
        return (str(datetime.datetime.now()))

    def match_id(self):
        return int(len(self.lst_matchsObj)) + 1

    def add_tournament_in_match(self, match, i):
        m = Matchcls(match['MatchID'],
                     match['MatchP1'],
                     match['MatchS1'],
                     match['MatchP2'],
                     match['MatchS2'],
                     match['Datetime'],
                     )
        # création du tuple Matchs avec le construct
        # append des id dans la liste de match du Tournois
        self.tournament_matchid_in_instance.append(self.match_id())
        self.lst_matchsObj.append(m)
        # Mise a jour du Rating dans les listes de joueurs
        for Player in self.lst_players_obj_sorted_by_id:
            # print(Player)
            # print(str(self.model.list1[i]))
            if str(Player) == str(self.list1[i]):
                Player.Player_rating = (float(Player.Player_rating) + float(m.MatchS1))
            if str(Player) == str(self.list2[i]):
                Player.Player_rating = (float(Player.Player_rating) + float(m.MatchS2))
        # print(m.__dict__)

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
