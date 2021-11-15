from operator import attrgetter
from Matchcls import Matchcls
import datetime


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model
        # Listes & variables du Controller
        self.lst_tournamentsObj_by_date = []
        self.tournament_players_by_rate = []

        self.tournament_matchid_in_instance = []
        self.player_in_instance = []
        self.player_in_instance_sorted = []

    # Pour selectionner un Tournois : à déclarer en amont de la partie tournois


    # Début du code : Création d'une instance à partir du JSON de la bdd
    def run(self):
        self.view.display_start()
        self.view.display_load_db()
        # Fonction import des Tournois, players & match du Json dans la liste du model
        self.model.load_tournaments()
        self.model.load_players()
        self.model.load_matchs()
        # 2- Début du Programme : Accès au Menu Principal
        self.main_menu()

    # Choix dans le menu principal
    # 1. Accéder section Joueurs
    # 2. Accéder section Tournois
    # 3. Fin du Programme
    def main_menu(self):
        section = self.view.input_main_menu()
        # section menu 'interraction avec l'utilisateur' conf view
        if section == '1':
            self.player_menu()
        elif section == '2':
            self.tournament_menu()
        elif section == '0':
            self.end_run()
            exit()
        else:
            self.error()

    # Fin du code : Sauvegarde de l'instance dans le JSON de la bdd
    def end_run(self):
        # Fonction pour Supprimer puis Sauvegarder les nouvelles BDD
        self.model.erase_tables()
        self.view.display_save_DB()
        # Fonction Sauvegarde Tournois, Tounois, matchs
        self.model.save_tournaments()
        self.model.save_players()
        self.model.save_matchs()
        # Fonction permettant de voir que le programme est terminé
        self.view.display_end()
        exit()

    # Choix dans la Section Joueurs
    # 1. afficher la liste des joueurs par ordre alphabétique
    # 2. afficher la liste des joueurs par Classement
    # 3. fonction création de joueurs
    # 0. Retour au Menu Principal
    def player_menu(self):
        section_players = self.view.input_player_menu()
        if section_players == '1':
            # Classer par Nom et Afficher la liste Joueurs de la BDD
            self.view.display_player_sort_by_name(self.model.player_sort_by_name())
            self.return_players()
        elif section_players == '2':
            # Classer par Rating et Afficher la liste des Joueurs de la BDD
            self.view.display_player_sort_by_rating(self.model.player_sort_by_rating())
            self.return_players()
            # self.view.input_player_menu()
        elif section_players == '3':
            # Pour Créer de nouveaux Joueurs
            # Création des attributs de l'objet joueur
            player = {
                'Player_index': self.model.player_index(),
                'Player_first_name': self.view.input_Player_first_name(),
                'Player_last_name': self.view.input_Player_last_name(),
                'Player_age': self.view.input_Player_age(),
                'Player_date_of_birth': self.view.input_Player_date_of_birth(),
                'Player_gender': self.view.input_Player_gender(),
                'Player_rating': self.view.input_Player_rating(),
                'Player_score': 0}
            # Initialisation de l'objet dans la classe
            self.model.add_player_in_class(player)
            self.return_players()
        elif section_players == '0':
            self.view.display_return_menu()
            self.main_menu()
        else:
            self.error()

    # Retour au Menu Player ou Menu principal à la fin de chaque choix
    def return_players(self):
        choice = self.view.input_return_players()
        if choice == '1':
            self.player_menu()
        elif choice == '2':
            self.main_menu()
        else:
            self.error()

    # Choix dans la Section Tournois
    # 1. afficher la liste des anciens Tournois et accéder aux options
    # 2. Créer un nouveau Tournois
    # 0. Retour au Menu Principal
    def tournament_menu(self):
        section_tournaments = self.view.input_tournament_menu()
        if section_tournaments == '1':
            # Classer liste des Tournois par date pour permettre la selection des ID
            self.lst_tournamentsObj_by_date = self.model.tournaments_history()
            self.view.display_tournaments_history()
            # choix du tournois dans la liste affiché ci-dessus
            self.model.find_id = self.view.input_find_id()
            # initialisation de la variable id qui va servir dans le menu tournois
            self.view.display_selected_tournament(self.model.select_tounament())
            # Préparation des joueurs de chaque tournois pour les 2 de tri suivants:
            # Classement de la liste des Joueurs par ID
            self.tournament_players = self.model.search_tournament_player()
            # Choix de l'affichage en fonction de l'ID :
            info_tournament = self.view.input_information_tournament()

            if info_tournament == '1':
                # Afficher Informations du Tournois selectionné : date, description, etc...
                self.view.display_information_tournament_selected()
                self.main_menu()
            elif info_tournament == '2':
                # Classement de la liste des joueurs du Tournois par nom :
                self.view.display_tournament_player_by_name(self.model.tournament_players_by_name())
                self.main_menu()
            elif info_tournament == '3':
                # Classement de la liste des joueurs du Tournois par rating :
                self.view.display_tournament_player_by_rate(self.model.tournament_players_by_rate())
                self.main_menu()
            elif info_tournament == '4':
                # Pour afficher Les Rounds, Matchs & le Classement des Joueurs pour le Tournois
                self.view.display_happen_in_tournament(self.model.id)
                lst_round = self.model.id.TournamentMatchID
                for round in range(int(self.model.id.Tournament_nbr_round)):
                    list_rnd_to_display = lst_round[:4]
                    self.view.display_round_for_match(round)
                    for match_id in list_rnd_to_display:
                        for match in self.model.lst_matchsObj:
                            if match_id == match.MatchID:
                                self.view.display_match_in_round(match)
                    del lst_round[:4]

                self.main_menu()
            elif info_tournament == '5':
                self.view.display_start_new_tournament()
                # vérifier si le tournois possède deja 4ID match X Round et redemarrer a l'endroit ou ca c'est arreté
                self.tournament_matchid_in_instance = self.id.TournamentMatchID
                print('Nombre de Rounds executés précédement : '
                      + str(int((len(self.tournament_matchid_in_instance)) / 4)))
                if str(int((len(self.tournament_matchid_in_instance)) / 4)) == str(self.id.Tournament_nbr_round):
                    print("Nombre de Round Max atteint, retour au menu principal")
                    self.main_menu()
                else:
                    print(self.id)
                    print('Nombre de Rounds du Tournois : ' + str(self.id.Tournament_nbr_round))
                    print('ID des participants: ' + str(self.id.Tournament_players_id))
                    # print(str(self.tournament_players))
                    # Nombre de joueur /2
                    nbr_joueurs_by_list = int(len(self.model.tournament_players) / 2)
                    print("Nombre de joueur par liste: " + str(nbr_joueurs_by_list))
                    # Tri de la liste
                    # def get_Player_score(self.tournament_players):
                    #     return self.tournament_players.get('Player_score', 'Player_rating')
                    # self.tournament_players.sort(key=itemgetter('Player_score', 'Player_rating'), reverse=True)
                    if int((len(self.tournament_matchid_in_instance) / 4)) == 0:
                        self.player_in_instance = self.model.tournament_players
                        self.player_in_instance_sorted = sorted(self.player_in_instance,
                                                                key=lambda x: x.Player_rating,
                                                                reverse=True)
                        print('tri 1 : par Classement')
                        for player in self.player_in_instance_sorted:
                            print(str(player) + '  ' + str(player.Player_rating))
                        # création des deux listes
                        list1 = self.player_in_instance_sorted[:nbr_joueurs_by_list]
                        list2 = self.player_in_instance_sorted[-nbr_joueurs_by_list:]

                    else:
                        # Remplir les Scores des joueurs de self.tournament_players avec les rouds précédents
                        for index in self.id.Tournament_players_id:
                            for Player in self.model.lst_players_obj_sorted_by_id:
                                # print(Player)
                                if index == Player.Player_index:
                                    self.player_in_instance.append(Player)
                        # Réinitialisation des score des joueurs
                        for Player in self.player_in_instance:
                            Player.Player_score = 0
                        # Ajout des scores des matchs précédents
                        for Player in self.player_in_instance:
                            for Match in self.model.lst_matchsObj:
                                # print(Player)
                                # print(Player.Player_score)
                                # print(Match.MatchP1)
                                # print(Match.MatchS1)
                                if str(Player) == str(Match.MatchP1):
                                    Player.Player_score = (int(Player.Player_score) + int(Match.MatchS1))
                            for Match in self.model.lst_matchsObj:
                                if str(Player) == str(Match.MatchP2):
                                    Player.Player_score = (int(Player.Player_score) + int(Match.MatchS2))
                        for Player in self.player_in_instance:
                            print(Player)
                            print(Player.Player_score)
                        # triage
                        self.player_in_instance_sorted = sorted(self.player_in_instance,
                                                                key=attrgetter('Player_score', 'Player_rating'),
                                                                reverse=True)
                        print('tri 2 : par Score puis Classement')
                        for player in self.player_in_instance_sorted:
                            print(str(player) + '  ' + str(player.Player_score) + '  ' + str(player.Player_rating))
                        # creation des deux listes
                        list1 = self.player_in_instance_sorted[:nbr_joueurs_by_list]
                        list2 = self.player_in_instance_sorted[-nbr_joueurs_by_list:]
                    # début des matchs
                    # Création des Tuples = parties :
                    for i in range(nbr_joueurs_by_list):
                        print(str(list1[i]) + ' VS ' + str(list2[i]))
                        m = Matchcls(MatchID=self.model.match_id(),
                                     MatchP1=str(list1[i]),
                                     MatchS1=input('Score ' + str(list1[i]) + ': '),
                                     MatchP2=str(list2[i]),
                                     MatchS2=input('Score: ' + str(list2[i]) + ': '),
                                     Datetime=str(datetime.datetime.now())
                                     )
                        # création du tuple Matchs avec le construct
                        # append des id dans la liste de match du Tournois
                        self.tournament_matchid_in_instance.append(self.model.MatchID())
                        self.model.lst_matchsObj.append(m)
                        # Mise a jour du Rating dans les listes de joueurs
                        for Player in self.model.lst_players_obj_sorted_by_id:
                            # print(Player)
                            # print(str(list1[i]))
                            if str(Player) == str(list1[i]):
                                Player.Player_rating = (int(Player.Player_rating) + int(m.MatchS1))
                            if str(Player) == str(list2[i]):
                                Player.Player_rating = (int(Player.Player_rating) + int(m.MatchS2))
                        print(m.__dict__)
                    print(self.model.lst_matchsObj)
                    # Mise a jour de la liste de matchs dans l'objet tournois selectionné de la liste des tournois
                    self.id.TournamentMatchID = self.tournament_matchid_in_instance
                    self.main_menu()

        elif section_tournaments == '2':
            # Pour créer un nouveau Tournois
            tournament = {
                'Tournament_index': self.model.tournament_index(),
                'Tournament_name': self.view.input_tournament_name(),
                'Tournament_location': self.view.input_tournament_location(),
                'Tournament_date': self.view.input_tournament_date(),
                'Tournament_nbr_round': self.view.input_tournament_nbr_round(),
                'Tournament_players_id': self.model.tournament_player_ids(),
                'Tournament_ctl_time': self.model.tournament_ctl_time(),
                'Tournament_description': self.view.input_tournament_description()
            }
            self.model.add_tournament_in_class(tournament)

            self.main_menu()
        elif section_tournaments == '0':
            self.view.DisplayReturn_MENU_PRINCIPAL()
            self.main_menu()
        else:
            self.error()

    # Message et Action suite mauvaise Saisie

    def error(self):
        print('Erreur de Saisie, Retour au Menu principal\n')
        return self.main_menu()
