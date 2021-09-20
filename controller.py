import datetime


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model

    # ici variables model
    def run(self):
        self.view.display_start()
        self.main_menu()

    def main_menu(self):
        section = self.view.input_main_menu()
        # section menu 'interraction avec l'utilisateur' conf view
        if section == '1':
            self.player_menu()
        elif section == '2':
            self.tournament_menu()
        elif section == '0':
            self.model.save_players()
            self.model.save_tournaments()
            self.view.display_end()
            exit()
        else:
            self.error()

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
            last_name = self.view.input_player_last_name()
            first_name = self.view.input_player_first_name()
            date_of_birth = self.view.input_player_date_of_birth()
            gender = self.view.input_player_gender()
            rating = self.view.input_player_rating()
            self.model.add_new_player(last_name, first_name, date_of_birth, gender, rating)
            #self.model.all_playersObj.append(Playercls(last_name, first_name, date_of_birth, gender, rating))
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
    def choice_ctl_time(self):
        selection_ctl_time = self.view.input_tournament_ctl_time()
        if selection_ctl_time == '1':
            choice = 'bullet_timer'
        elif selection_ctl_time == '2':
            choice = 'blitz_timer'
        elif selection_ctl_time == '3':
            choice = 'speed_chess_timer'
        return self.choice_ctl_time  # todo ???

    def tournament_menu(self):
        section_tournaments = self.view.input_tournament_menu()

        if section_tournaments == '1':
            # Classer liste des Tournois de la BDD par id
            self.view.display_tournaments(self.model.all_tournamentsObj)
            self.main_menu()
            # self.info_tournament()
        elif section_tournaments == '2':
            # Construct Tournament
            name = self.view.input_tournament_name(),
            location =  self.view.input_tournament_location(),
            tournament_players_input = self.get_tournament_players(),
            date = datetime.datetime.now(),
            nbr_round = self.view.input_tournament_nbr_round(),
            ctl_time = self.choice_ctl_time(),
            description = self.view.input_tournament_description()
            self.model.add_new_tournament(name, location, tournament_players_input, date, nbr_round, ctl_time, description)
            self.main_menu()
        elif section_tournaments == '0':
            print('Retour au menu princial\n')
            self.main_menu()
        else:
            self.error()

    def get_tournament_players(self):
        tournament_players = []
        input = None
        while input!=0:
            self.view.display_player_for_tournament_choice(self.model.all_playersObj)
            input = self.view.input_tournament_players()
            if input != 0:
                player = self.model.all_playersObj[input -1]
                tournament_players.append(player)
        return tournament_players

    def return_tournaments(self):
        choice = self.view.input_return_tournament()
        if choice == '1':
            self.tournament_menu()
        elif choice == '2':
            self.main_menu()
        else:
            self.error()

        # afiichage des tournois par ordre ordre alphabetique généré pas le nom du tournois

    def info_tournament(self):
        self.model.info_t_get_name()

    # selection tournoi
    def selected_tournament(self):
        select_user = self.view.input_selected_tournament()
        for Tournament in self.model.all_tournamentsObj:
            if str(Tournament['id']) == select_user:
                selected_tournament = Tournament
                return selected_tournament

    def infos_tournament(self):
        if self.view.infos_tournament() == '1':
            self.view.display_infos_tournament1()
            # Fonction Informations du Tournois : date, description, etc... en fonction de id_info_tournament
            return self.infos_tournament()
        elif self.view.infos_tournament == '2':
            self.view.display_infos_tournament2()
            # Fonction Liste des joueurs ayants participés par ordre alphabétique en fonction de selected_tournament
            return self.infos_tournament()
        elif self.view.infos_tournament == '3':
            self.view.display_infos_tournament3()
            # Fonction Liste des joueurs ayants participés (Classement Général) en fonction de selected_tournament
            return self.infos_tournament()
        elif self.view.infos_tournament == '4':
            self.view.display_infos_tournament4()
            # Fonction Classement interne du Tournois en fonction de id_info_tournament
            return self.infos_tournament()
        elif self.view.infos_tournament == '5':
            self.view.display_infos_tournament5()
            # Fonction Liste des Rounds du Tournoi en fonction de id_info_tournament
            return self.infos_tournament()
        elif self.view.infos_tournament == '6':
            self.view.display_infos_tournament6()
            # Fonction Liste des Matchs du Tournois en fonction de id_info_tournament
            return self.infos_tournament()
        else:
            self.error()

    # Message et Action suite mauvaise Saisie

    def error(self):
        print('Erreur de Saisie, Retour au Menu principal\n')
        return self.main_menu()
