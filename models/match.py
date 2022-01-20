from operator import attrgetter
from datetime import datetime


class Match:
    def __init__(self, match_id=0, match_player1='unknown', match_score1=0, match_player2='unknown',
                 match_score2=0, Datetime='unknown'):
        self.match_id = match_id
        self.match_player1 = match_player1
        self.match_score1 = match_score1
        self.match_player2 = match_player2
        self.match_score2 = match_score2
        self.Datetime = Datetime

    def __str__(self):
        return f"match: {self.match_player1} VS {self.match_player2}"

    # def __repr__(self):
    # return f"match: {self.match_player1} VS {self.match_player2}"

    def tournament_match_id_instanced(self, id):
        """ ID de match du tournoi sélectionné"""
        tournament_match_id_in_instance = id.tournament_match_id
        return (tournament_match_id_in_instance)

    def create_nbr_players_by_list(self, tournament_players):
        """Création de listes(préparation du tri des joueurs pour les matchs)."""
        nbr_players_by_list = int(len(tournament_players) / 2)
        return nbr_players_by_list

    def match2lists_creation(self, nbr_players_by_list, tournament_match_id_in_instance,
                             lst_players_obj_sorted_by_id, id, lst_matchsobj, tournament_players):
        """
        Génération des listes avec tri des joueurs pour :
        1-1er round = tri des joueurs en fonction de leur classement.
        2-Rounds suivants = récupération des anciens scores 1er round,
        tri des joueurs en fonction de leur score, si trop d'égalité pour le tri -> ajout du rating.
          + association des joueurs n'ayant pas déjà joués ensemble.
          """
        player_in_instance = []
        # new_match = None
        # list1 = []
        # list2 = []
        if int((len(tournament_match_id_in_instance) / 4)) == 0:
            player_in_instance = tournament_players
            self.player_in_instance_sorted = sorted(player_in_instance,
                                                    key=lambda x: x.player_rating,
                                                    reverse=True)
            list1 = self.player_in_instance_sorted[:nbr_players_by_list]
            list2 = self.player_in_instance_sorted[-nbr_players_by_list:]
        else:
            for index in id.tournament_players_id:
                for Player in lst_players_obj_sorted_by_id:
                    # print(Player)
                    if index == Player.player_index:
                        player_in_instance.append(Player)
            for Player in player_in_instance:
                Player.player_score = 0
            for Player in player_in_instance:
                for new_match in id.tournament_match_id:
                    for old_match in lst_matchsobj:
                        if str(Player) == str(old_match.match_player1) and new_match == old_match.match_id:
                            Player.player_score = (float(Player.player_score) + float(old_match.match_score1))
                        if str(Player) == str(old_match.match_player2) and new_match == old_match.match_id:
                            Player.player_score = (float(Player.player_score) + float(old_match.match_score2))
            self.player_in_instance_sorted = sorted(player_in_instance,
                                                    key=attrgetter('player_score', 'player_rating'),
                                                    reverse=True)
            list1 = self.player_in_instance_sorted[::2]
            list2 = self.player_in_instance_sorted[1::2]
            for i in range(nbr_players_by_list):
                for m in id.tournament_match_id:
                    for p in lst_matchsobj:
                        if str(list1[i]) == p.match_player1 and str(
                                list2[i]) == p.match_player2 and m == p.match_id:
                            list1 = []
                            list1.append(self.player_in_instance_sorted[0])
                            list1.append(self.player_in_instance_sorted[1])
                            list1.append(self.player_in_instance_sorted[4])
                            list1.append(self.player_in_instance_sorted[5])
                            list2 = []
                            list2.append(self.player_in_instance_sorted[2])
                            list2.append(self.player_in_instance_sorted[3])
                            list2.append(self.player_in_instance_sorted[6])
                            list2.append(self.player_in_instance_sorted[7])
                            pass
                        if str(list1[i]) == p.match_player2 and str(
                                list2[i]) == p.match_player1 and m == p.match_id:
                            list1 = []
                            list1.append(self.player_in_instance_sorted[0])
                            list1.append(self.player_in_instance_sorted[1])
                            list1.append(self.player_in_instance_sorted[4])
                            list1.append(self.player_in_instance_sorted[5])
                            list2 = []
                            list2.append(self.player_in_instance_sorted[2])
                            list2.append(self.player_in_instance_sorted[3])
                            list2.append(self.player_in_instance_sorted[6])
                            list2.append(self.player_in_instance_sorted[7])
                            pass
                        else:
                            pass
        return list1, list2

    def match_datetime(self):
        return (str(datetime.now()))

    def create_match_id(self, lst_matchsobj):
        return int(len(lst_matchsobj)) + 1

    def add_tournament_in_match(self, kwargs_match):
        for key, value in kwargs_match.items():
            setattr(self, key, value)
        new_match = Match(match_id=kwargs_match['match_id'],
                          match_player1=kwargs_match['match_player1'],
                          match_score1=kwargs_match['match_score1'],
                          match_player2=kwargs_match['match_player2'],
                          match_score2=kwargs_match['match_score2'],
                          Datetime=kwargs_match['Datetime'])
        return self.match_id, new_match

    def update_rating_in_player(self, i, lst_players_obj_sorted_by_id, list1, list2, new_match):
        """Mise à jour du Rating dans les listes de joueurs"""
        for Player in lst_players_obj_sorted_by_id:
            if str(Player) == str(list1[i]):
                Player.player_rating = (float(Player.player_rating) + float(new_match.match_score1))
            if str(Player) == str(list2[i]):
                Player.player_rating = (float(Player.player_rating) + float(new_match.match_score2))

    def match_by_round(self, id, lst_matchsobj):
        """Définit le nbre de matchs ds le tournoi"""
        lst_round = id.tournament_match_id.copy()
        for round in range(int(id.tournament_nbr_round)):
            list_rnd_to_display = lst_round[:4]
            print('Matchs du round ' + str(round + 1))
            for match_id in list_rnd_to_display:
                for match in lst_matchsobj:
                    if match_id == match.match_id:
                        print(match)
            del lst_round[:4]
