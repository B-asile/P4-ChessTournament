from operator import attrgetter
from tournament import Tournament
from player import Player
from match import Match
import datetime
from db import DB


class Model:
    def __init__(self):
        # variables de model
        self.lst_playersobj = []
        self.lst_tournamentsobj = []
        self.lst_matchsobj = []
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
        for tournament in DB.table_tournaments:
            new_tournament = Tournament(tournament['tournament_index'],
                                        tournament['tournament_name'],
                                        tournament['tournament_location'],
                                        tournament['tournament_date'],
                                        tournament['tournament_nbr_round'],
                                        tournament['tournament_players_id'],
                                        tournament['tournament_ctl_time'],
                                        tournament['tournament_description'],
                                        tournament['tournament_match_id'])
            self.lst_tournamentsobj.append(new_tournament)
            # print(new_tournament)
        print(self.lst_tournamentsobj)

    # Fonction Import Joueurs
    def load_players(self):
        for player in DB.table_players:
            new_player = Player(player['player_index'],
                                player['player_first_name'],
                                player['player_last_name'],
                                player['player_age'],
                                player['player_date_of_birth'],
                                player['player_gender'],
                                player['player_rating'],
                                player['player_score'])
            self.lst_playersobj.append(new_player)
            # print(new_player)
        print(self.lst_playersobj)

    # fonction import des matchs
    def load_matchs(self):
        for match in DB.table_matchs:
            new_match = Match(match['match_id'],
                              match['match_player1'],
                              match['match_score1'],
                              match['match_player2'],
                              match['match_score2'])
            self.lst_matchsobj.append(new_match)
            # print(new_match)
        print(self.lst_matchsobj)

    # 2. Fonction Sauvegarde des données vers BDD (écraser tout)
    # Fonction Suppression anciennes Tables pour nouvelle sauvegarde
    @staticmethod
    def erase_tables():
        DB.TinyDBDropTables()

    # Fonction Sauvegarde Joueurs
    def save_players(self):
        for player in self.lst_playersobj:
            DB.table_players.insert(player.__dict__)

    # Fonction Sauvegarde Tournois
    def save_tournaments(self):
        for tournament in self.lst_tournamentsobj:
            DB.table_tournaments.insert(tournament.__dict__)

    def save_matchs(self):
        for match in self.lst_matchsobj:
            DB.table_matchs.insert(match.__dict__)

    # """"""""""""""""""""""""""""""""""""""""""""""

    # FONCTIONS D'OPERATIONS :

    # 1. Section Player :
    # Pour afficher la liste des Joueurs par ordre alphabétique
    # Classer par Nom et Afficher la liste Joueurs de la BDD
    def player_sort_by_name(self):
        list_az = sorted(self.lst_playersobj, key=lambda x: x.player_first_name.lower(), reverse=False)
        return list_az

    # Pour afficher le Classement des Joueurs
    # Classer par Rating et Afficher la liste des Joueurs de la BDD
    def player_sort_by_rating(self):
        list_rating = sorted(self.lst_playersobj, key=lambda x: int(x.player_rating), reverse=True)
        return list_rating

    # Pour Créer de nouveaux Joueurs
    def player_index(self):
        return int(len(self.lst_playersobj)) + 1

    def add_player_in_class(self, player):
        new_player = Player(player['player_index'],
                            player['player_first_name'],
                            player['player_last_name'],
                            player['player_age'],
                            player['player_date_of_birth'],
                            player['player_gender'],
                            player['player_rating'],
                            player['player_score'])
        self.lst_playersobj.append(new_player)

    # 2. Section Tournois :
    def select_tounament(self):
        # Déclaration des variables pour la selection de tournois
        for selection in self.lst_tournamentsobj:
            if selection.tournament_index == int(self.find_id):
                self.id = selection
                return selection

    def search_tournament_player(self):
        self.lst_players_obj_sorted_by_id = sorted(self.lst_playersobj, key=lambda x: x.player_index,
                                                   reverse=False)
        # Création d'une variable avec la liste des ID et liste des joueurs du Tournois
        selected_tournament_players_id = self.id.tournament_players_id
        # Itération dans la liste des ID du Tournois
        for id in selected_tournament_players_id:
            # Itération dans la liste des Joueurs
            for Player in self.lst_players_obj_sorted_by_id:
                # Si l'ID de la liste correspond à l'ID d'un joueur de la Liste des objets joueurs
                if id == Player.player_index:
                    # ajout à la liste des Joueurs du Tournois
                    self.tournament_players.append(Player)

    # Pour afficher les anciens Tournois et accéder aux options
    def tournaments_history(self):
        return sorted(self.lst_tournamentsobj, key=lambda x: str(x.tournament_date), reverse=False)

    # Classement de la liste des joueurs du Tournois par nom :
    def tournament_players_by_name(self):
        return sorted(self.tournament_players, key=lambda x: x.player_first_name.lower(), reverse=False)

    # Classement de la liste des joueurs du Tournois par rating :
    def tournament_players_by_rate(self):
        return sorted(self.tournament_players, key=lambda x: x.player_rating, reverse=True)

    def tournament_matchid_instanced(self):
        self.tournament_matchid_in_instance = self.id.tournament_match_id
        return (self.tournament_matchid_in_instance)

    def match2lists_creation(self):
        self.nbr_joueurs_by_list = int(len(self.tournament_players) / 2)
        # si le match commence (round = 0) tri par classement
        if int((len(self.tournament_matchid_in_instance) / 4)) == 0:
            self.player_in_instance = self.tournament_players
            self.player_in_instance_sorted = sorted(self.player_in_instance,
                                                    key=lambda x: x.player_rating,
                                                    reverse=True)
            # for player in self.player_in_instance_sorted:
            #    print(str(player) + '  ' + str(player.player_rating))
            # création des deux listes
            self.list1 = self.player_in_instance_sorted[:self.nbr_joueurs_by_list]
            self.list2 = self.player_in_instance_sorted[-self.nbr_joueurs_by_list:]
        # si le match est deja en cours, récupération des anciens scores
        else:
            # Remplir les Scores des joueurs de self.tournament_players avec les rouds précédents
            for index in self.id.tournament_players_id:
                for Player in self.lst_players_obj_sorted_by_id:
                    # print(Player)
                    if index == Player.player_index:
                        self.player_in_instance.append(Player)
            # Réinitialisation des score des joueurs
            for Player in self.player_in_instance:
                Player.player_score = 0
            # Ajout des scores des matchs précédents
            for Player in self.player_in_instance:
                for new_match in self.id.tournament_match_id:
                    for old_match in self.lst_matchsobj:
                        if str(Player) == str(old_match.match_player1) and new_match == old_match.match_id:
                            Player.player_score = (float(Player.player_score) + float(old_match.match_score1))
                    for match in self.lst_matchsobj:
                        if str(Player) == str(old_match.match_player2) and new_match == old_match.match_id:
                            Player.player_score = (float(Player.player_score) + float(old_match.match_score2))
            # for Player in self.player_in_instance:
            #     print(Player)
            #     print(Player.player_score)
            # triage par score puis par classement
            self.player_in_instance_sorted = sorted(self.player_in_instance,
                                                    key=attrgetter('player_score', 'player_rating'),
                                                    reverse=True)
            # print('tri 2 : par Score puis Classement')
            # for player in self.player_in_instance_sorted:
            #    print(str(player) + '  ' + str(player.player_score) + '  ' + str(player.player_rating))
            # creation des deux listes
            # Elements de la liste self.player_in_instance_sorted commençant par 0 iteration 2
            self.list1 = self.player_in_instance_sorted[::2]
            # Elements de la liste self.player_in_instance_sorted commençant par 1 iteration 2
            self.list2 = self.player_in_instance_sorted[1::2]
            # Test si match deja existant dans les rounds précédents
            # pour chaque prochain round
            for i in range(self.nbr_joueurs_by_list):
                # pour chaque id de round deja fait dans ce tournois
                for m in self.id.tournament_match_id:
                    # pour chaque matchs deja fait dans l'absolue
                    for p in self.lst_matchsobj:
                        if str(self.list1[i]) == p.match_player1 and str(
                                self.list2[i]) == p.match_player2 and m == p.match_id:
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
                        if str(self.list1[i]) == p.match_player2 and str(
                                self.list2[i]) == p.match_player1 and m == p.match_id:
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
        return int(len(self.lst_matchsobj)) + 1

    def add_tournament_in_match(self, match, i):
        new_match = Match(match['match_id'],
                          match['match_player1'],
                          match['match_score1'],
                          match['match_player2'],
                          match['match_score2'],
                          match['Datetime'],
                          )
        # création du tuple Matchs avec le construct
        # append des id dans la liste de match du Tournois
        self.tournament_matchid_in_instance.append(self.match_id())
        self.lst_matchsobj.append(new_match)
        # Mise a jour du Rating dans les listes de joueurs
        for Player in self.lst_players_obj_sorted_by_id:
            # print(Player)
            # print(str(self.model.list1[i]))
            if str(Player) == str(self.list1[i]):
                Player.player_rating = (float(Player.player_rating) + float(new_match.match_score1))
            if str(Player) == str(self.list2[i]):
                Player.player_rating = (float(Player.player_rating) + float(new_match.match_score2))
        # print(m.__dict__)

    def match_by_round(self):
        lst_round = self.id.tournament_match_id.copy()
        for round in range(int(self.id.tournament_nbr_round)):
            list_rnd_to_display = lst_round[:4]
            print('Matchs du round ' + str(round + 1))
            for match_id in list_rnd_to_display:
                for match in self.lst_matchsobj:
                    if match_id == match.match_id:
                        print(match)
            del lst_round[:4]

    def tournament_index(self):
        return int(len(self.lst_tournamentsobj)) + 1

    def add_tournament_in_class(self, tournament):
        new_tournament = Tournament(tournament['tournament_index'],
                                    tournament['tournament_name'],
                                    tournament['tournament_location'],
                                    tournament['tournament_date'],
                                    tournament['tournament_nbr_round'],
                                    tournament['tournament_players_id'],
                                    tournament['tournament_ctl_time'],
                                    tournament['tournament_description'])
        self.lst_tournamentsobj.append(new_tournament)
