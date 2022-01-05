class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model
        # Listes & variables du Controller
        self.player_in_instance_sorted = []

    # Pour selectionner un Tournois : à déclarer en amont de la partie tournois

    # Début du code : Création d'une instance à partir du JSON de la bdd
    def run(self):
        self.view.display_start()
        self.view.display_load_db()
        # Fonction import des tournois, players & match du Json dans la liste du model
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
        elif section_players == '3':
            # Pour Créer de nouveaux Joueurs
            # Création des attributs de l'objet joueur
            player = {
                'player_index': self.model.create_player_index(),
                'player_first_name': self.view.input_player_first_name(),
                'player_last_name': self.view.input_player_last_name(),
                'player_age': self.view.input_player_age(),
                'player_date_of_birth': self.view.input_player_date_of_birth(),
                'player_gender': self.view.input_player_gender(),
                'player_rating': self.view.input_player_rating(),
                'player_score': 0}
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
            self.view.display_tournaments_history(self.model.tournaments_history())
            # choix du tournois dans la liste affiché ci-dessus
            self.model.find_id = self.view.input_find_id(self.model.lst_tournamentsobj)
            # initialisation de la variable id qui va servir dans le menu tournois
            self.view.display_selected_tournament(self.view.input_find_id())
            # Préparation des joueurs de chaque tournois pour les 2 de tri suivants:
            # transformation liste ID en List d'objet
            self.tournament_players = self.model.search_tournament_player()
            # Choix de l'affichage en fonction de l'ID :
            info_tournament = self.view.input_information_tournament()

            if info_tournament == '1':
                # Afficher Informations du Tournois selectionné : date, description, etc...
                self.view.display_information_tournament_selected(self.model.id)
                self.tournament_menu()
            elif info_tournament == '2':
                # Classement de la liste des joueurs du Tournois par nom :
                self.view.display_tournament_player_by_name(self.model.tournament_players_by_name())
                self.tournament_menu()
            elif info_tournament == '3':
                # Classement de la liste des joueurs du Tournois par rating :
                self.view.display_tournament_player_by_rate(self.model.tournament_players_by_rate())
                self.tournament_menu()
            elif info_tournament == '4':
                # Pour afficher Les Rounds, Matchs & le Classement des Joueurs pour le Tournois
                self.view.display_happen_in_tournament(self.model.id)
                self.tournament_menu()
            elif info_tournament == '5':
                # print demarrage d'un nouveau tournois
                self.view.display_start_new_tournament()
                # vérifier si le tournois possède deja 4ID match X Round et redemarrer à l'endroit ou ca c'est arreté
                # Nombre de rounds executés précédement
                self.view.nbr_round_before(self.model.tournament_matchid_instanced())
                if str(int((len(self.model.tournament_match_id_in_instance)) / 4)) == str(
                        self.model.id.tournament_nbr_round):
                    self.view.max_round()
                    self.tournament_menu()
                else:
                    self.view.selected_tournament_name(self.model.id)
                    self.view.selected_tournament_round(self.model.id.tournament_nbr_round)
                    self.view.selected_players_ids(self.model.id.tournament_players_id)
                    self.model.match2lists_creation()
                    # début des matchs
                    # Création des Tuples = parties :

                    for i in range(self.model.nbr_joueurs_by_list):
                        # Affichage du match en cours avec l'iteration 1 de la list 1 et 1 de la list 2
                        self.view.display_current_match(self.model.list1[i], self.model.list2[i])
                        m = {
                            'match_id': self.model.create_match_id(),
                            'match_player1': str(self.model.list1[i]),
                            'match_score1': input('Score ' + str(self.model.list1[i]) + ': '),
                            'match_player2': str(self.model.list2[i]),
                            'match_score2': input('Score: ' + str(self.model.list2[i]) + ': '),
                            'Datetime': self.model.match_datetime()
                        }
                        self.model.add_tournament_in_match(m, i)
                    print(self.model.lst_matchsobj)
                    # Mise a jour de la liste de matchs dans l'objet tournois selectionné de la liste des tournois
                    self.model.id.tournament_match_id = self.model.tournament_match_id_in_instance
                    self.tournament_menu()

            elif info_tournament == '0':
                self.main_menu()
        elif section_tournaments == '2':
            # Pour créer un nouveau Tournois
            tournament = {
                'tournament_index': self.model.create_tournament_index(),
                'tournament_name': self.view.input_tournament_name(),
                'tournament_location': self.view.input_tournament_location(),
                'tournament_date': self.view.input_tournament_date(),
                'tournament_nbr_round': self.view.input_tournament_nbr_round(),
                'tournament_players_id': self.view.input_tournament_player_ids(self.model.player_sort_by_name()),
                'tournament_ctl_time': self.view.input_tournament_ctl_time(),
                'tournament_description': self.view.input_tournament_description(),
                'tournament_match_id': []
            }
            self.model.add_tournament_in_class(tournament)

            self.tournament_menu()
        elif section_tournaments == '0':
            self.main_menu()
        else:
            self.error()

    # Message et Action suite mauvaise Saisie

    def error(self):
        print('Erreur de Saisie, Retour au Menu principal\n')
        return self.tournament_menu()
