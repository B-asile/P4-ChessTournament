class Controller:

    def __init__(self, view, data_base, player, tournament, match):
        self.view = view
        self.data_base = data_base
        self.player = player
        self.tournament = tournament
        self.match = match
        # Listes & variables du Controller
        self.player_in_instance_sorted = []

    # Pour selectionner un Tournois : à déclarer en amont de la partie tournois

    # Début du code : Création d'une instance à partir du JSON de la bdd
    def run(self):
        self.view.display_start()
        self.view.display_load_db()
        # Fonction import des tournois, players & match du Json dans la liste du model
        self.data_base.load_tournaments()
        self.data_base.load_players()
        self.data_base.load_matchs()
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
        self.data_base.erase_tables()
        self.view.display_save_DB()
        # Fonction Sauvegarde Tournois, Tounois, matchs
        self.data_base.save_tournaments()
        self.data_base.save_players()
        self.data_base.save_matchs()
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
            self.view.display_player_sort_by_name(self.player.player_sort_by_name(self.data_base.lst_playersobj))
            self.return_players()
        elif section_players == '2':
            # Classer par Rating et Afficher la liste des Joueurs de la BDD
            self.view.display_player_sort_by_rating(self.player.player_sort_by_rating(self.data_base.lst_playersobj))
            self.return_players()
        elif section_players == '3':
            # Pour Créer de nouveaux Joueurs
            # Création des attributs de l'objet joueur
            player = {
                'player_index': self.player.create_player_index(self.data_base.lst_playersobj),
                'player_first_name': self.view.input_player_first_name(),
                'player_last_name': self.view.input_player_last_name(),
                'player_age': self.view.input_player_age(),
                'player_date_of_birth': self.view.input_player_date_of_birth(),
                'player_gender': self.view.input_player_gender(),
                'player_rating': self.view.input_player_rating(),
                'player_score': 0}
            # Initialisation de l'objet dans la classe
            self.player.add_player_in_class(player, self.data_base.lst_playersobj)
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
            self.view.display_tournaments_history(self.tournament.tournaments_history
                                                  (self.data_base.lst_tournamentsobj))
            # choix du tournois dans la liste affiché ci-dessus
            self.data_base.find_id = self.view.input_find_id(self.data_base.lst_tournamentsobj)
            # initialisation de la variable id qui va servir dans le menu tournois
            for selection in self.data_base.lst_tournamentsobj:
                if selection.tournament_index == int(self.data_base.find_id):
                    self.data_base.id = selection
            self.view.display_selected_tournament(self.data_base.id)
            # Préparation des joueurs de chaque tournois pour les 2 de tri suivants:
            # transformation liste ID en List d'objet
            self.data_base.tournament_players = self.tournament.search_tournament_player(
                self.data_base.lst_players_obj_sorted_by_id,
                self.data_base.lst_playersobj,
                self.data_base.id,
                self.data_base.tournament_players)
            # Choix de l'affichage en fonction de l'ID :
            info_tournament = self.view.input_information_tournament()

            if info_tournament == '1':
                # Afficher Informations du Tournois selectionné : date, description, etc...
                self.view.display_information_tournament_selected(self.data_base.id)
                self.tournament_menu()
            elif info_tournament == '2':
                # Classement de la liste des joueurs du Tournois par nom :
                self.view.display_tournament_player_by_name(
                    self.tournament.tournament_players_by_name(self.data_base.tournament_players))
                self.tournament_menu()
            elif info_tournament == '3':
                # Classement de la liste des joueurs du Tournois par rating :
                self.view.display_tournament_player_by_rate(
                    self.tournament.tournament_players_by_rate(self.data_base.tournament_players))
                self.tournament_menu()
            elif info_tournament == '4':
                # Pour afficher Les Rounds, Matchs & le Classement des Joueurs pour le Tournois
                self.view.display_happen_in_tournament(self.data_base.id)
                self.tournament_menu()
            elif info_tournament == '5':
                # print demarrage d'un nouveau tournois
                self.view.display_start_new_tournament()
                # vérifier si le tournois possède deja 4ID match X Round et redemarrer à l'endroit ou ca c'est arreté
                # if self.model.tournament_match_id_in_instance() != None:
                # Nombre de rounds executés précédement
                self.match.tournament_match_id_instanced(self.data_base.tournament_match_id_in_instance,
                                                         self.data_base.id)
                self.view.nbr_round_before(self.data_base.tournament_match_id_in_instance)
                if str(int((len(self.data_base.tournament_match_id_in_instance)) / 4)) == str(
                        self.data_base.id.tournament_nbr_round):
                    self.view.max_round()
                    self.tournament_menu()
                else:
                    self.view.selected_tournament_name(self.data_base.id)
                    self.view.selected_tournament_round(self.data_base.id.tournament_nbr_round)
                    self.view.selected_players_ids(self.data_base.id, self.tournament.tournament_players_id)
                    self.match.match2lists_creation(self.data_base.nbr_joueurs_by_list,
                                                    self.data_base.tournament_players,
                                                    self.data_base.tournament_match_id_in_instance,
                                                    self.data_base.lst_players_obj_sorted_by_id,
                                                    self.data_base.id,
                                                    self.data_base.lst_matchsobj)
                    # début des matchs
                    # Création des Tuples = parties :

                    for i in range(self.data_base.nbr_joueurs_by_list):
                        # Affichage du match en cours avec l'iteration 1 de la list 1 et 1 de la list 2
                        self.view.display_current_match(self.match.list1[i], self.match.list2[i])
                        m = {
                            'match_id': self.match.create_match_id(self.data_base.lst_matchsobj),
                            'match_player1': str(self.match.list1[i]),
                            'match_score1': self.view.input_player_score(self.match.list1[i]),
                            'match_player2': str(self.match.list2[i]),
                            'match_score2': self.view.input_player_score(self.match.list2[i]),
                            'Datetime': self.match.match_datetime()
                        }
                        self.match.add_tournament_in_match(m, i)
                    print(self.data_base.lst_matchsobj)
                    # Mise à jour de la liste de matchs dans l'objet tournois sélectionné de la liste des tournois
                    self.match.id.tournament_match_id = self.data_base.tournament_match_id_in_instance
                    self.tournament_menu()

            elif info_tournament == '0':
                self.main_menu()
        elif section_tournaments == '2':
            # Pour créer un nouveau Tournois
            tournament = {
                'tournament_index': self.tournament.create_tournament_index(self.data_base.lst_tournamentsobj),
                'tournament_name': self.view.input_tournament_name(),
                'tournament_location': self.view.input_tournament_location(),
                'tournament_date': self.view.input_tournament_date(),
                'tournament_nbr_round': self.view.input_tournament_nbr_round(),
                'tournament_players_id': self.view.input_tournament_player_ids(self.player.player_sort_by_name()),
                'tournament_ctl_time': self.view.input_tournament_ctl_time(),
                'tournament_description': self.view.input_tournament_description(),
                'tournament_match_id': []
            }
            self.tournament.add_tournament_in_class(tournament)

            self.tournament_menu()
        elif section_tournaments == '0':
            self.main_menu()
        else:
            self.error()

    # Message et Action suite mauvaise Saisie

    def error(self):
        print('Erreur de Saisie, Retour au Menu principal\n')
        return self.tournament_menu()
