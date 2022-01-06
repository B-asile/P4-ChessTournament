import datetime


class View:

    def __init__(self):
        self.controller = None

    def set_controller(self, controller):
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
        return input('\n*** MENU PRINCIPAL *** \n'
                     '1 - Pour accéder à la Section Joueurs \n'
                     '2 - Pour accéder à la Section Tournois \n'
                     '0 - Pour quitter le Programme \n')

    @staticmethod
    def input_player_menu():
        return input('*** SECTION JOUEURS *** \n'
                         '1 - Pour afficher la liste des Joueurs par ordre alphabétique \n'
                         '2 - Pour afficher le Classement des Joueurs \n'
                         '3 - Pour Créer de nouveaux Joueurs \n'
                         '0 - Pour Retourner au Menu Principale\n')

    def display_player_sort_by_name(self, list_of_player):
        """Affichage de la liste des joueurs de A-Z"""
        print('Liste des Joueurs par ordre alphabétique\n')
        for player in list_of_player:
            print(player)

    def display_player_sort_by_rating(self, list_of_player):
        """Affichage des joueurs par classement-rang"""
        print('Classement des Joueurs\n')
        for player in list_of_player:
            print(str(player) + '  ' + '(Score: ' + str(player.player_rating) + ')')

    @staticmethod
    def input_player_first_name():
        return input("saisir le nom du joueur \n")

    @staticmethod
    def input_player_last_name():
        return input("saisir le prénom du joueur \n")

    @staticmethod
    def input_player_age():
        """gestion erreurs entrées utilisateur pour saisie age_player"""
        player_age = None
        while not player_age:
            player_age = input("saisir l'age du joueur\n"
                               "veuillez saisir un nombre\n")
            try:
                player_age = int(player_age)
            except ValueError:
                player_age = None
                print("Oops, veuillez saisir un nombre")
        return player_age

    @staticmethod
    def input_player_date_of_birth():
        """gestion entrées utilisateur formatage de date"""
        while True:
            try:
                return str(datetime.datetime.strptime(input("saisir la date de naissance du joueur\n"
                                                            "au format jj/mm/aaaa\n"), "%d/%m/%Y").date())
            except(ValueError, TypeError):
                print("Oops! le format 'date' est invalide \n veuillez recommencer la saisie \n")

    @staticmethod
    def input_player_gender():
        return input("saisir le sexe du joueur\n F(feminin)/M(masculin)\n")

    @staticmethod
    def input_player_rating():
        while True:
            try:
                return float(input("saisir le rang du joueur\n"
                                   "veuillez saisir un nombre\n"))
            except(ValueError, TypeError):
                print("Oops, veuillez saisir un nombre\n")

    def display_new_player(self):
        print(self.controller.newplayer)

    @staticmethod
    def display_return_menu():
        print('Retour au menu princial\n')

    @staticmethod
    def input_return_players():
        choice = input('1 - Effectuer une autre action dans cette section \n'
                       '2 - Retourner au Menu Princial\n')
        return choice

    @staticmethod
    def input_tournament_menu():
        section_tournaments = input(
            'SECTION TOURNOIS \n '
            '1 - Pour accéder aux tournois (anciens & en cours) \n '
            '2 - Pour Créer un nouveau Tournois \n '
            '0 - Pour Retourner au Menu Principale\n')
        return section_tournaments

    def display_tournaments_history(self, list_tournament_obj_by_date):
        print('Liste des Tournois par date:\n')
        for x in list_tournament_obj_by_date:
            print('ID :' + str(x.tournament_index) + ' ' + x.tournament_name + ' ' + str(x.tournament_date))
        print('\n')

    def input_find_id(self, lst_tournamentobj):
            #return int(input("ID du Tournois à selectionner"))
        tournament_lst_id = [tournament.tournament_index for tournament in lst_tournamentobj]
        tournament_id = None
        while not tournament_id:
            tournament_id = input("Entrez l'id du Tournois à sélectionner" + str(tournament_id) + " : ")
            try:
                tournament_id = int(tournament_id)
                if tournament_id not in tournament_lst_id:
                    raise ValueError
            except:
                tournament_id = None
                print("Oops!!! Tournoi inexistant recommencez la saisie\n")
        return tournament_id

    def display_selected_tournament(self, id):
        print("Vous avez selectionné le Tournois: " + id.tournament_name + '\n')

    def display_happen_in_tournament(self, id):
        print('Déroulement du tournois ' + id.tournament_name)
        print('Nombre de round : ' + str(id.tournament_nbr_round))

    def display_round_for_match(self, round):
        print('Matchs du round ' + str(round + 1))

    def display_match_in_round(self, match):
        print(match)

    @staticmethod
    def input_information_tournament():
        return input(" Informations à afficher :\n"
                     " 1 - Informations du Tournois : date, description, etc...\n"
                     " 2 - Liste des joueurs ayants participés par ordre alphabétique\n"
                     " 3 - Liste des joueurs ayants participés (Classement Général)\n"
                     " 4 - Liste des Rounds, Matchs et Classement du Tournois\n"
                     " 5 - Démarrer/Reprendre : Mode Tournois\n"
                     " 0 - retourner au menu principal\n")

    def display_information_tournament_selected(self, id):
        return print("INFORMATION DU TOURNOIS: "
                     "\n- Nom du Tournois: " + str(id.tournament_name) +
                     "\n- Date du Tournois: " + str(id.tournament_date) +
                     "\n- Description du Tournois: " + str(id.tournament_description) +
                     "\n- Localisation du Tournois: " + str(id.tournament_location) +
                     "\n- Time Control: " + str(id.tournament_ctl_time) + "\n")

    def display_players_in_tournament_name(self):
        print('PARTICIPANTS (Classement par nom) pour le Tournois: ' + self.controller.id.tournament_name)

    def display_tournament_player_by_name(self, list_of_player):
        print('PARTICIPANTS (Classement par Noms)')
        for player in list_of_player:
            print('Nom: ' + player.player_first_name + ' Prenom: ' + player.player_last_name)
        print('\n')

    def display_tournament_player_by_rate(self, list_of_player):
        print('PARTICIPANTS (Classement par Score Global)')
        for player in list_of_player:
            print('Score Global: ' + str(player.player_rating)
                  + ' Nom: ' + player.player_first_name
                  + ' Prenom: ' + player.player_last_name)
        print('\n')

    @staticmethod
    def display_start_new_tournament():
        print('START A NEW TOURNAMENT')

    def nbr_round_before(self, tournament_match_id_in_instance):
        print('Nombre de Rounds exécutés précédemment : ' + str(int((len(tournament_match_id_in_instance)) / 4)))

    @staticmethod
    def max_round():
        print("Nombre de Round Max atteint, retour au menu principal")

    def selected_tournament_name(self, id):
        print(id)

    def display_current_match(self, player1, player2):
        print(str(player1) + ' VS ' + str(player2))

    def selected_tournament_round(self, tournament_nbr_round):
        print('Nombre de Rounds du Tournois : ' + str(tournament_nbr_round))

    def selected_players_ids(self, tournament_players_id):
        print('ID des participants: ' + str(tournament_players_id))

    @staticmethod
    def input_tournament_name():
        return input("saisir le nom du tournois\n")

    @staticmethod
    def input_tournament_location():
        return input("saisir la localité du tournois\n")

    @staticmethod
    def input_tournament_date():
        while True:
            try:
                return str(datetime.datetime.strptime(input("saisir la date du tournois\n"
                                                            "au format jj/mm/aaaa\n"), "%d/%m/%Y").date())
            except(ValueError, TypeError):
                print("Oops! le format 'date' est invalide \n veuillez recommencer la saisie \n")

    @staticmethod
    def input_tournament_nbr_round():
        while True:
            try:
                return int(input("saisir le nombre de round\n"
                                 "veuillez saisir un nombre\n"))
            except(ValueError, TypeError):
                print("Oops, veuillez saisir un nombre\n")

    @staticmethod
    def input_tournament_description():
        return input("ajoutez une description du tournoi \n")

    # Pour créer un nouveau Tournois
    def input_tournament_player_ids(self, list_of_player):
        ''' Entrées utilisateur et gestion des erreurs input pour selection des id joueur création de tournois'''
        print('Selection des Joueurs du Tournois \n')
        for player in list_of_player:
            print('Nom: ' + player.player_first_name + ' Prenom: ' + player.player_last_name + ' id: ' + str(
                player.player_index))
        players_list_id = [player.player_index for player in list_of_player]
        lst = []
        for number in range(1, 9):
            player_id = None
            while not player_id:
                player_id = input("Entrer l'id du Player " + str(number) + " :  ")
                try:
                    player_id = int(player_id)
                    if player_id not in players_list_id:
                        raise ValueError()
                    if player_id in lst:
                        raise ValueError()
                except:
                    player_id = None
                    print("Oops! id inexistant ou déjà utilisé \n veuillez recommencer la saisie \n")
                else:
                    lst.append(player_id)
        return lst

    @staticmethod
    def input_tournament_ctl_time():
        print('*** TimeControl ***')
        while True:
            user_select = input("1 - Pour sélectionner un bullet\n"
                                "2 - Pour sélectionner un blitz\n"
                                "3 - Pour sélectionner un coup rapide\n")
            if user_select == '1': return 'BULLET'
            if user_select == '2': return 'BLITZ'
            if user_select == '3': return 'COUP RAPIDE'
            print("Saisie incorrecte, entrez 1,2 ou 3")

    @staticmethod
    def input_selected_tournament():
        return input("saisir id tournoi \n")

    @staticmethod
    def input_infos_tournament():
        return input(' INFORMATIONS TOURNOI :\n'
                     ' 1 - Informations du Tournois : date, description, etc...\n'
                     ' 2 - Liste des joueurs ayants participés par ordre alphabétique\n'
                     ' 3 - Liste des joueurs ayants participés (Classement Général)\n'
                     ' 4 - Classement interne du Tournois\n'
                     ' 5 - Liste des Rounds du Tournois\n'
                     ' 6 - Liste des Matchs du Tournois\n')

    @staticmethod
    def display_end():
        print('Fin du Programme, à bientôt\n')
