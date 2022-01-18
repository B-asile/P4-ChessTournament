from collections import OrderedDict


class Tournament:

    def __init__(self, tournament_index=0, tournament_name='unknown', tournament_location='unknown',
                 tournament_date='00/00/0000', tournament_nbr_round=4, tournament_players_id=[],
                 tournament_ctl_time='BLITZ', tournament_description='unknown', tournament_match_id=[]):
        self.tournament_index = tournament_index
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.tournament_date = tournament_date
        self.tournament_nbr_round = tournament_nbr_round
        self.tournament_players_id = tournament_players_id
        self.tournament_ctl_time = tournament_ctl_time
        self.tournament_description = tournament_description
        self.tournament_match_id = tournament_match_id

    def __str__(self):
        return f"Tournament: {self.tournament_name} {self.tournament_location} {self.tournament_date}"

    # def __repr__(self):
    # return f"Tournament: {self.tournament_name} {self.tournament_location} {self.tournament_date}"

    # 2. Section Tournois :
    # def select_tournament(self, lst_tournamentsobj, find_id, id):
    #     """Déclaration des variables pour la selection de tournois"""
    #     for selection in lst_tournamentsobj:
    #         if selection.tournament_index == int(find_id):
    #             id = selection
    #            return selection
    def create_lst_players_obj_sorted_by_id(self, lst_playersobj):
        lst_players_obj_sorted_by_id = sorted(lst_playersobj, key=lambda x: x.player_index,
                                              reverse=False)
        return lst_players_obj_sorted_by_id

    def search_tournament_player(self, lst_players_obj_sorted_by_id, id):
        # Création d'une variable avec la liste des ID et liste des joueurs du Tournois
        tournament_players = []
        selected_tournament_players_id = id.tournament_players_id
        # Itération dans la liste des ID du Tournois
        for id in selected_tournament_players_id:
            # Itération dans la liste des Joueurs
            for Player in lst_players_obj_sorted_by_id:
                # Si l'ID de la liste correspond à l'ID d'un joueur de la Liste des objets joueurs
                if id == Player.player_index:
                    # ajout à la liste des Joueurs du Tournois
                    tournament_players.append(Player)
        return tournament_players

    def tournaments_history(self, lst_tournamentsobj):
        """Pour afficher les anciens Tournois et accéder aux options"""
        return sorted(lst_tournamentsobj, key=lambda x: str(x.tournament_date), reverse=False)

    def tournament_players_by_name(self, tournament_players):
        """Classement de la liste des joueurs du tournoi par nom"""
        tournament_list_by_name = sorted(tournament_players, key=lambda x: x.player_first_name.lower(), reverse=False)
        tournament_list_by_name = list(OrderedDict.fromkeys(tournament_list_by_name))
        return tournament_list_by_name

    def tournament_players_by_rate(self, tournament_players):
        """Classement de la liste des joueurs du Tournoi par rating"""
        tournament_list_by_rate = sorted(tournament_players, key=lambda x: x.player_rating, reverse=True)
        tournament_list_by_rate = list(OrderedDict.fromkeys(tournament_list_by_rate))
        return tournament_list_by_rate

    def create_tournament_index(self, lst_tournamentsobj):
        return int(len(lst_tournamentsobj)) + 1

    def add_tournament_in_class(self, kwargs_tournament, lst_tournamentsobj):
        for key, value in kwargs_tournament.items():
            setattr(self, key, value)
        new_tournament = Tournament(tournament_index=kwargs_tournament['tournament_index'],
                                    tournament_name=kwargs_tournament['tournament_name'],
                                    tournament_location=kwargs_tournament['tournament_location'],
                                    tournament_date=kwargs_tournament['tournament_date'],
                                    tournament_nbr_round=kwargs_tournament['tournament_nbr_round'],
                                    tournament_players_id=kwargs_tournament['tournament_players_id'],
                                    tournament_ctl_time=kwargs_tournament['tournament_ctl_time'],
                                    tournament_description=kwargs_tournament['tournament_description'],
                                    tournament_match_id=kwargs_tournament['tournament_match_id'])
        lst_tournamentsobj.append(new_tournament)
