class Controller:

    def __init__(self, view, data_base, player, tournament, match):
        self.view = view
        self.data_base = data_base
        self.player = player
        self.tournament = tournament
        self.match = match
        self.player_in_instance_sorted = []

    def run(self):
        """
        Début du code : 1-création d'une instance à partir du JSON de la BDD
                        - import des données
                        2- Début du Programme : Accès au Menu Principal
        """
        self.view.display_start()
        self.view.display_load_db()
        self.data_base.load_tournaments()
        self.data_base.load_players()
        self.data_base.load_matchs()
        self.main_menu()

    def main_menu(self):
        """
        Choix dans le menu principal(interaction avec utilisateur, conf view)
        1. Accéder section Joueurs
        2. Accéder section Tournois
        3. Fin du Programme
        """
        section = self.view.input_main_menu()
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
        """
        Fin du code : Sauvegarde de l'instance dans le JSON de la bdd
        1. Supprimer puis Sauvegarder les nouvelles BDD
        2. Sauvegarde Tournois, joueurs, matchs.
        """
        self.data_base.erase_tables()
        self.view.display_save_DB()
        self.data_base.save_tournaments()
        self.data_base.save_players()
        self.data_base.save_matchs()
        self.view.display_end()
        exit()

    def player_menu(self):
        """
        Choix dans la Section Joueurs
        1. afficher la liste des joueurs par ordre alphabétique
        2. afficher la liste des joueurs par Classement
        3. fonction création de joueurs
        0. Retour au Menu Principal
        """
        section_players = self.view.input_player_menu()
        if section_players == '1':
            self.view.display_player_sort_by_name(self.player.player_sort_by_name(self.data_base.lst_playersobj))
            self.return_players()
        elif section_players == '2':
            self.view.display_player_sort_by_rating(self.player.player_sort_by_rating(self.data_base.lst_playersobj))
            self.return_players()
        elif section_players == '3':
            player = {
                'player_index': self.player.create_player_index(self.data_base.lst_playersobj),
                'player_first_name': self.view.input_player_first_name(),
                'player_last_name': self.view.input_player_last_name(),
                'player_age': self.view.input_player_age(),
                'player_date_of_birth': self.view.input_player_date_of_birth(),
                'player_gender': self.view.input_player_gender(),
                'player_rating': self.view.input_player_rating(),
                'player_score': 0}
            self.data_base.new_player = self.player.add_player_in_class(player)
            self.data_base.lst_playersobj.append(self.data_base.new_player)
            self.return_players()
        elif section_players == '0':
            self.view.display_return_menu()
            self.main_menu()
        else:
            self.error()

    def return_players(self):
        """Retour au Menu Player ou Menu principal à la fin de chaque choix"""
        choice = self.view.input_return_players()
        if choice == '1':
            self.player_menu()
        elif choice == '2':
            self.main_menu()
        else:
            self.error()

    def tournament_menu(self):
        """ Choix dans la Section Tournois
         1. afficher la liste des anciens Tournois et accéder aux options
         2. Créer un nouveau Tournoi
         0. Retour au Menu Principal
        """
        section_tournaments = self.view.input_tournament_menu()
        if section_tournaments == '1':
            self.view.display_tournaments_history(self.tournament.tournaments_history
                                                  (self.data_base.lst_tournamentsobj))
            self.data_base.find_id = self.view.input_find_id(self.data_base.lst_tournamentsobj)
            for selection in self.data_base.lst_tournamentsobj:
                if selection.tournament_index == int(self.data_base.find_id):
                    self.data_base.id = selection
            self.view.display_selected_tournament(self.data_base.id)
            self.data_base.lst_players_obj_sorted_by_id = self.tournament.create_lst_players_obj_sorted_by_id(
                self.data_base.lst_playersobj)
            self.data_base.tournament_players = self.tournament.search_tournament_player(
                self.data_base.lst_players_obj_sorted_by_id,
                self.data_base.id)
            info_tournament = self.view.input_information_tournament()

            self.selected_infos_tournament(info_tournament)
        elif section_tournaments == '2':
            """création d'un nouveau Tournoi"""
            tournament = {
                'tournament_index': self.tournament.create_tournament_index(self.data_base.lst_tournamentsobj),
                'tournament_name': self.view.input_tournament_name(),
                'tournament_location': self.view.input_tournament_location(),
                'tournament_date': self.view.input_tournament_date(),
                'tournament_nbr_round': self.view.input_tournament_nbr_round(),
                'tournament_players_id': self.view.input_tournament_player_ids(
                    self.player.player_sort_by_name(self.data_base.lst_playersobj)),
                'tournament_ctl_time': self.view.input_tournament_ctl_time(),
                'tournament_description': self.view.input_tournament_description(),
                'tournament_match_id': []
            }
            self.data_base.new_tournament = self.tournament.add_tournament_in_class(tournament)
            self.data_base.lst_tournamentsobj.append(self.data_base.new_tournament)

            self.tournament_menu()
        elif section_tournaments == '0':
            self.main_menu()
        else:
            self.error()

    def selected_infos_tournament(self, info_tournament):
        """Afficher les informations du Tournoi sélectionné :
        1-information du tournoi
        2-Classement de la liste des joueurs du Tournoi par nom
        3-Classement de la liste des joueurs du Tournoi par rating
        4-Pour afficher Les Rounds, Matchs & le Classement des Joueurs pour le Tournoi
        5-lancement du tournoi sélectionné(en fonction de son avancement-nbre de rounds déjà exécuté,
        reprise du tournoi/ affichage des matchs, ajout des scores par joueur)
        """
        if info_tournament == '1':
            self.view.display_information_tournament_selected(self.data_base.id)
            self.tournament_menu()
        elif info_tournament == '2':
            self.view.display_tournament_player_by_name(
                self.tournament.tournament_players_by_name(self.data_base.tournament_players))
            self.tournament_menu()
        elif info_tournament == '3':
            self.view.display_tournament_player_by_rate(
                self.tournament.tournament_players_by_rate(self.data_base.tournament_players))
            self.tournament_menu()
        elif info_tournament == '4':
            self.view.display_happen_in_tournament(self.data_base.id)
            self.view.display_tournament_infos(self.data_base.id,
                                               self.data_base.lst_players_obj_sorted_by_id,
                                               self.data_base.lst_matchsobj)
            self.tournament_menu()
        elif info_tournament == '5':
            self.view.display_start_new_tournament()
            self.data_base.tournament_match_id_in_instance = self.match.tournament_match_id_instanced(
                self.data_base.id)
            self.view.nbr_round_before(self.data_base.tournament_match_id_in_instance)
            if str(int((len(self.data_base.tournament_match_id_in_instance)) / 4)) == str(
                    self.data_base.id.tournament_nbr_round):
                self.view.max_round()
                self.tournament_menu()
            else:
                self.view.selected_tournament_name(self.data_base.id)
                self.view.selected_tournament_round(self.data_base.id.tournament_nbr_round)
                self.view.selected_players_ids(self.tournament.tournament_players_id)
                self.data_base.nbr_players_by_list = 0
                self.data_base.nbr_players_by_list = self.match.create_nbr_players_by_list(
                    self.data_base.tournament_players)
                self.data_base.list1, self.data_base.list2 = self.match.match2lists_creation(
                    self.data_base.nbr_players_by_list,
                    self.data_base.tournament_match_id_in_instance,
                    self.data_base.lst_players_obj_sorted_by_id,
                    self.data_base.id,
                    self.data_base.lst_matchsobj,
                    self.data_base.tournament_players)

                for i in range(self.data_base.nbr_players_by_list):
                    self.view.display_current_match(self.data_base.list1[i], self.data_base.list2[i])
                    m = {
                        'match_id': self.match.create_match_id(self.data_base.lst_matchsobj),
                        'match_player1': str(self.data_base.list1[i]),
                        'match_score1': self.view.input_player_score(self.data_base.list1[i]),
                        'match_player2': str(self.data_base.list2[i]),
                        'match_score2': self.view.input_player_score(self.data_base.list2[i]),
                        'Datetime': self.match.match_datetime()
                    }
                    match_id, self.data_base.new_match = self.match.add_tournament_in_match(m)
                    self.data_base.tournament_match_id_in_instance.append(match_id)
                    self.data_base.lst_matchsobj.append(self.data_base.new_match)
                    self.match.update_rating_in_player(i,
                                                       self.data_base.lst_players_obj_sorted_by_id,
                                                       self.data_base.list1, self.data_base.list2,
                                                       self.data_base.new_match)

                # print(self.data_base.lst_matchsobj)
                self.data_base.id.tournament_match_id = self.data_base.tournament_match_id_in_instance
                self.tournament_menu()

        elif info_tournament == '0':
            self.main_menu()

        else:
            self.error()

    def error(self):
        """Message et Action suite mauvaise Saisie"""
        print('Erreur de Saisie, Retour au Menu principal\n')
        return self.tournament_menu()
