from operator import attrgetter
from Matchs import Matchcls


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model
        # Listes & variables du Controller
        self.lst_tournamentsObj_by_date = []
        self.id = 0
        self.find_id = 0
        self.tournament_players_by_name = []
        self.tournament_players_by_rate = []
        self.tournament_players = []

    # Pour selectionner un Tournois (dans la section tournament menu)
    def select_tounament(self):
        # Déclaration des variables pour la selection de tournois
        for x in self.model.lst_tournamentsObj:
            if x.Tournament_index == int(self.find_id):
                return x

    def run(self):
        self.view.display_start()
        self.view.display_load_db()
        # Fonction import des Tournois du Json dans la liste
        self.model.load_tournaments()
        # Fonction Import Joueurs
        self.model.load_players()
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

    def end_run(self):
        # Fonction pour Supprimer puis Sauvegarder les nouvelles BDD
        self.model.erase_tables()
        self.view.display_save_DB()
        # Fonction Sauvegarde Tournois
        self.model.save_tournaments()
        # Fonction Sauvegarde Joueurs
        self.model.save_players()
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
            self.view.display_range_a_z(self.model.sort_by_name())
            self.main_menu()
        elif section_players == '2':
            # Classer par Rating et Afficher la liste des Joueurs de la BDD
            self.view.display_range_rating(self.model.sort_by_rating())
            self.main_menu()
            # self.view.input_player_menu()
        elif section_players == '3':
            # Pour Créer de nouveaux Joueurs
            player = {
                'Player_index': self.model.Player_index(),
                'Player_first_name': self.view.input_Player_first_name(),
                'Player_last_name': self.view.input_Player_last_name(),
                'Player_age': self.view.input_Player_age(),
                'Player_date_of_birth': self.view.input_Player_date_of_birth(),
                'Player_gender': self.view.input_Player_gender(),
                'Player_rating': self.view.input_Player_rating(),
                'Player_score': 0}
            self.model.add_player_in_class(player)
            self.main_menu()
        elif section_players == '0':
            print('Retour au menu princial\n')
            self.main_menu()
        else:
            self.error()

    # Retour au Menu Player ou Menu principal à la fin de chaque choix sans la section Joueur
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
            # Classer liste des Tournois par date
            self.lst_tournamentsObj_by_date = self.model.tournaments_history()
            self.view.display_tournaments_history()
            # choix du tournois
            self.find_id = self.view.input_find_id()
            self.id = self.select_tounament()
            self.view.display_selected_tournament()
            print(self.id.Tournament_players_id)

            # Préparation des joueurs de chaque tournois pour les 2 choix suivants:
            # Classement de la liste des Joueurs par ID
            Lst_players_obj_sorted_by_id = sorted(self.model.lst_playersObj, key=lambda x: x.Player_index,
                                                  reverse=False)
            # Création d'une variable avec la liste des ID et liste des joueurs du Tournois
            selected_tournament_players_id = self.id.Tournament_players_id
            # Itération dans la liste des ID du Tournois
            for x in selected_tournament_players_id:
                # Itération dans la liste des Joueurs
                for Player in Lst_players_obj_sorted_by_id:
                    # Si l'ID de la liste correspond à l'ID d'un joueur de la Liste des objets joueurs
                    if x == Player.Player_index:
                        # ajout à la liste des Joueurs du Tournois
                        self.tournament_players.append(Player)

            # Choix de l'affichage en fonction de l'ID :
            info_tournament = self.view.input_information_tournament()

            if info_tournament == '1':
                # Afficher Informations du Tournois selectionné : date, description, etc...
                self.view.display_information_tournament_selected()
                self.main_menu()
            elif info_tournament == '2':
                # Classement de la liste des joueurs du Tournois par nom :
                self.tournament_players_by_name = sorted(self.tournament_players, key=lambda x: x.Player_first_name.lower(),
                                                         reverse=False)
                print(self.tournament_players_by_name)
                self.view.display_tournament_player_by_name()
                self.main_menu()
            elif info_tournament == '3':
                # Pour afficher la Liste des joueurs ayants participés (Classement Général)'
                self.view.display_tournament_player_by_rate1()
                # Classement de la liste des joueurs du Tournois par rating :
                self.tournament_players_by_rate = sorted(self.tournament_players, key=lambda x: x.Player_rating,
                                                         reverse=True)
                # print(self.tournament_players_by_rate)
                self.view.display_tournament_player_by_rate2()
                self.main_menu()
            elif info_tournament == '4':
                # Pour afficher Les Rounds, Matchs & le Classement des Joueurs pour le Tournois
                print('blablablabla')
                self.main_menu()
            elif info_tournament == '5':
                self.view.display_start_new_tournament()
                # vérifier si le tournois possède deja 4ID match X Round et redemarrer a l'endroit ou ca c'est arreté
                # liste des rounds = bla
                print(self.id)
                print('Nombre de Rounds du Tournois : ' + str(self.id.Tournament_nbr_round))
                print('ID des participants: ' + str(self.id.Tournament_players_id))
                # print(str(self.tournament_players))
                # Nombre de joueur /2
                nbr_joueurs_by_list = int(len(self.tournament_players) / 2)
                print("Nombre de joueur par liste: " + str(nbr_joueurs_by_list))
                # Tri de la liste
                # def get_Player_score(self.tournament_players):
                #     return self.tournament_players.get('Player_score', 'Player_rating')
                # self.tournament_players.sort(key=itemgetter('Player_score', 'Player_rating'), reverse=True)
                sorted(self.tournament_players, key=attrgetter('Player_score', 'Player_rating'), reverse=True)
                # print("Liste triée par Rang: ")
                # print(self.tournament_players)
                # Liste de la première moitié
                # print("Liste 1:")
                List1 = self.tournament_players[:nbr_joueurs_by_list]
                # print(List1)
                # Liste de la deuxieme moitié
                # print("Liste 2:")
                List2 = self.tournament_players[-nbr_joueurs_by_list:]
                # print(List2)
                # Création des Tuples = parties :
                for i in range(nbr_joueurs_by_list):
                    print(str(List1[i]) + ' VS ' + str(List2[i]))
                    m = Matchcls(MatchID=input('ID '),
                                 MatchP1=str(List1[i]),
                                 MatchS1=input('Score ' + str(List1[i]) + ': '),
                                 MatchP2=str(List2[i]),
                                 MatchS2=input('Score: ' + str(List2[i]) + ': '))
                    self.model.LstObjMatchs.append(m)
                    print(m.__dict__)
                    self.model.lst_matchsObj.append(m)
                print(self.model.lst_matchsObj)
                #         création du tuple Matchs avec le construct
                #         append des id dans la liste de match du Tournois
                self.main_menu()

        elif section_tournaments == '2':
            # Pour créer un nouveau Tournois
            tournament = {
                'Tournament_index': self.model.TournamentIndex(),
                'Tournament_name': self.view.input_tournament_name(),
                'Tournament_location': self.view.input_tournament_location(),
                'Tournament_date': self.view.input_tournament_date(),
                'Tournament_nbr_round': self.view.input_tournament_nbr_round(),
                'Tournament_players_id': self.model.tournament_player_ids(),
                'Tournament_ctl_time': self.model.tournament_ctl_time(),
                'Tournament_description': self.view.input_tournament_description()
            }
            self.model.AddTournamentInClass(tournament)

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
