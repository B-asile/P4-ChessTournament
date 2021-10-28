class View:

    def __init__(self):
        self.controller = None

    def setController(self, controller):
        self.controller = controller

    @staticmethod
    def display_start():
        print("START PROGRAM")

    @staticmethod
    def display_load_db():
        print("CHARGEMENT DE LA BASE DE DONNEE")

    @staticmethod
    def display_save_DB():
        print("SAUVEGARDE DES DONNEES TERMINE")

    @staticmethod
    def input_main_menu():
        return input('MENU PRINCIPAL \n '
                        '1 - Pour accéder à la Section Joueurs \n '
                        '2 - Pour accéder à la Section Tournois \n '
                        '0 - Pour quitter le Programme \n')

    @staticmethod
    def input_player_menu():
        return input('SECTION JOUEURS \n '
                                '1 - Pour afficher la liste des Joueurs par ordre alphabétique \n '
                                '2 - Pour afficher le Classement des Joueurs \n '
                                '3 - Pour Créer de nouveaux Joueurs \n '
                                '0 - Pour Retourner au Menu Principale\n')

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

    def input_Player_first_name(self):
        return input("saisir le nom du joueur \n")

    def input_Player_last_name(self):
        return input("saisir le prénom du joueur \n")

    def input_Player_age(self):
        return input("saisir l'age du joueur\n")

    def input_Player_date_of_birth(self):
        return input("saisir la date de naissance du joueur \n")

    def input_Player_gender(self):
        return input("saisir le genre du joueur \n")

    def input_Player_rating(self):
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

    def display_tournaments_history(self):
        print('Liste des Tournois par date:\n')
        for x in self.controller.lst_tournamentsObj_by_date:
            print('ID :' + str(x.Tournament_index) + ' ' + x.Tournament_name + ' ' + x.Tournament_date)
        print('\n')

    def input_find_id(self):
        return input('ID du Tournois à selectionner\n')

    def display_selected_tournament(self):
        print("Vous avez selectionné le Tournois: " + self.controller.id.Tournament_name)

    def input_information_tournament(self):
        return input(' Informations à afficher :\n'
                     ' 1 - Informations du Tournois : date, description, etc...\n'
                     ' 2 - Liste des joueurs ayants participés par ordre alphabétique\n'
                     ' 3 - Liste des joueurs ayants participés (Classement Général)\n'
                     ' 4 - Liste des Rounds, Matchs et Classement du Tournois\n'
                     ' 5 - Démarrer/Reprendre : Mode Tournois\n')

    def display_information_tournament_selected(self):
        return print('INFORMATION DU TOURNOIS: '
                     '\n- Nom du Tournois: ' + self.controller.id.Tournament_name +
                     '\n- Date du Tournois: ' + self.controller.id.Tournament_date +
                     '\n- Description du Tournois: ' + self.controller.id.Tournament_description +
                     '\n- Localisation du Tournois: ' + self.controller.id.Tournament_location +
                     '\n- Time Control: ' + self.controller.id.Tournament_ctl_time + '\n')

    def display_players_in_tournament_name(self):
        print('PARTICIPANTS (Classement par nom) pour le Tournois: ' + self.controller.id.Tournament_name)

    def display_tournament_player_by_name(self):
        for Player in self.controller.tournament_players_by_name:
            print('Nom: ' + Player.Player_first_name + ' Prenom: ' + Player.Player_last_name)
        print('\n')

    def display_tournament_player_by_rate1(self):
        print('PARTICIPANTS (Classement par Score Global) pour le Tournois: ' + self.controller.id.Tournament_name)

    def display_tournament_player_by_rate2(self):
        for Player in self.controller.tournament_players_by_rate:
            print('Score Global: ' + str(Player.Player_rating)
                  + ' Nom: ' + Player.Player_first_name
                  + ' Prenom: ' + Player.Player_last_name)
        print('\n')

    def DisplayStartNewTournament(self):
        print('START A NEW TOURNAMENT')

    def input_tournament_name(self):
        return input("saisir le nom du tournoi")

    def input_tournament_location(self):
        return input("saisir la localité du tournoi")

    def input_tournament_date(self):
        return input("saisir la date du tournois")

    def input_tournament_nbr_round(self):
        return input("saisir le nombre de round")

    def input_tournament_description(self):
        return input("ajoutez une description du tournoi")






    def input_tournament_players(self):
        return int(input("saisir les joueurs participants au tournois"))

    def input_tournament_nbr_round(self):
        return input("saisir le nombre de round")

    def input_tournament_ctl_time(self):
        return input('CHOISIR UN CONTROLEUR TEMPS \n'
                     'tapez 1, 2 ou 3 \n'
                     '1- bullet_timer \n'
                     '2- blitz_timer \n'
                     '3- speed_chess_timer \n')







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


    def display_end(self):
        print('Fin du Programme, à bientôt\n')




