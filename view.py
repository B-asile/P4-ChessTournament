class View:

    def __init__(self):
        self.controller = None

    def setController(self, controller):
        self.controller = controller

    @staticmethod
    def display_start():
        print("START PROGRAM")

    @staticmethod
    def input_main_menu():
        section = input('MENU PRINCIPAL \n '
                        '1 - Pour accéder à la Section Joueurs \n '
                        '2 - Pour accéder à la Section Tournois \n '
                        '0 - Pour quitter le Programme \n')
        return section

    @staticmethod
    def input_player_menu():
        section_players = input('SECTION JOUEURS \n '
                                '1 - Pour afficher la liste des Joueurs par ordre alphabétique \n '
                                '2 - Pour afficher le Classement des Joueurs \n '
                                '3 - Pour Créer de nouveaux Joueurs \n '
                                '0 - Pour Retourner au Menu Principale\n')
        return section_players

    # printer player az
    def display_range_a_z(self, list_of_player):
        print('Liste des Joueurs par ordre alphabétique\n')
        for player in list_of_player:
            print(player)

    # printer player rating
    def display_range_rating(self, list_of_player):
        print('Classement des Joueurs\n')
        for player in list_of_player:
            print(player)

    # print('Création des Joueurs\n')

    def input_player_last_name(self):
        return input("saisir le prénom du joueur \n")

    def input_player_first_name(self):
        return input("saisir le nom du joueur \n")

    def input_player_date_of_birth(self):
        return input("saisir la date de naissance du joueur \n")

    def input_player_gender(self):
        return input("saisir le genre du joueur \n")

    def input_player_rating(self):
        return input("saisir le rang du joueur \n")

    def display_new_player(self):
        print(self.controller.newplayer)

    def input_return_players(self):
        choice = input('1 - Effectuer une autre action dans cette section \n '
                       '2 - Retourner au Menu Princial\n')
        return choice

    def input_tournament_menu(self):
        section_tournaments = input(
            'SECTION TOURNOIS \n '
            '1 - Pour afficher les anciens Tournois et accéder aux options \n '
            '2 - Pour Créer un nouveau Tournois \n '
            '0 - Pour Retourner au Menu Principale\n')
        return section_tournaments

    def display_tournaments(self, tournaments):
        for tournament in tournaments:
            print(tournament)

    def input_tournament_name(self):
        print('INTERFACE DE CREATION DE TOURNOIS\n')
        return input("saisir le nom du tournoi")

    def input_tournament_location(self):
        return input("saisir la localité du tournoi")

    def input_tournament_players(self):
        return int(input("saisir les joueurs participants au tournois"))

    def display_player_for_tournament_choice(self, players):
        count = 1
        for player in players:
            print(f"{count}. {player}")
            count+=1

    def input_tournament_nbr_round(self):
        return input("saisir le nombre de round")

    def input_tournament_ctl_time(self):
        return input('CHOISIR UN CONTROLEUR TEMPS \n'
                     'tapez 1, 2 ou 3 \n'
                     '1- bullet_timer \n'
                     '2- blitz_timer \n'
                     '3- speed_chess_timer \n')

    def input_tournament_description(self):
        return input("ajoutez une description du tournoi")

    def display_new_tournament(self):
        print(self.controller.newtournament)

    def input_return_tournament(self):
        return input(' 1 - Effectuer une autre action dans cette section \n '
                     ' 2 - Retourner au Menu Princial\n')

    def display_info_tournament(self):
        for tournament in self.controller.info_tournament:
            print(tournament)

    def input_selected_tournament(self):
        return input("saisir id tournoi \n")

    def input_infos_tournament(self):
        return input(' INFORMATIONS TOURNOI :\n'
                     ' 1 - Informations du Tournois : date, description, etc...\n'
                     ' 2 - Liste des joueurs ayants participés par ordre alphabétique\n'
                     ' 3 - Liste des joueurs ayants participés (Classement Général)\n'
                     ' 4 - Classement interne du Tournois\n'
                     ' 5 - Liste des Rounds du Tournois\n'
                     ' 6 - Liste des Matchs du Tournois\n')

    def display_infos_tournament1(self):
        print(f"infos du tournoi{self.controller.selected_tournament()}\n")

    def display_infos_tournament2(self):
        print('Liste des joueurs ayant participés par ordre alphabétique\n')

    def display_infos_tournament3(self):
        print('Liste des joueurs du Tournois selon le Classement Général\n')

    def display_infos_tournament4(self):
        print('Liste des joueurs du Tournois selon le classement général\n')

    def display_infos_tournament5(self):
        print('Liste des Rounds du Tournois\n')

    def display_infos_tournament6(self):
        print('Liste des Matchs du Tournois\n')

    def display_end(self):
        print('Fin du Programme, à bientôt\n')




