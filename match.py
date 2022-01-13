from operator import attrgetter
from datetime import datetime
from tournament import Tournament


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

    def tournament_match_id_instanced(self, tournament_match_id_in_instance, id):
        tournament_match_id_in_instance = id.tournament_match_id
        return (tournament_match_id_in_instance)

    def match2lists_creation(self, nbr_joueurs_by_list, tournament_players, tournament_match_id_in_instance,
                             lst_players_obj_sorted_by_id, id, lst_matchsobj):
        nbr_joueurs_by_list = int(len(tournament_players) / 2)
        # si le match commence (round = 0) tri par classement
        if int((len(tournament_match_id_in_instance) / 4)) == 0:
            self.player_in_instance = tournament_players
            self.player_in_instance_sorted = sorted(self.player_in_instance,
                                                    key=lambda x: x.player_rating,
                                                    reverse=True)
            # création des deux listes
            self.list1 = self.player_in_instance_sorted[:nbr_joueurs_by_list]
            self.list2 = self.player_in_instance_sorted[-nbr_joueurs_by_list:]
        # si le match est deja en cours, récupération des anciens scores
        else:
            # Remplir les Scores des joueurs de self.tournament_players avec les rounds précédents
            for index in id.tournament_players_id:
                for Player in lst_players_obj_sorted_by_id:
                    # print(Player)
                    if index == Player.player_index:
                        self.player_in_instance.append(Player)
            # Réinitialisation des score des joueurs
            for Player in self.player_in_instance:
                Player.player_score = 0
            # Ajout des scores des matchs précédents
            for Player in self.player_in_instance:
                for new_match in id.tournament_match_id:
                    for old_match in lst_matchsobj:
                        if str(Player) == str(old_match.match_player1) and new_match == old_match.match_id:
                            Player.player_score = (float(Player.player_score) + float(old_match.match_score1))
                    for match in lst_matchsobj:
                        if str(Player) == str(old_match.match_player2) and new_match == old_match.match_id:
                            Player.player_score = (float(Player.player_score) + float(old_match.match_score2))
            # for Player in self.player_in_instance:
            #     print(Player)
            #     print(Player.player_score)
            # triage par score puis par classement
            self.player_in_instance_sorted = sorted(self.player_in_instance,
                                                    key=attrgetter('player_score', 'player_rating'),
                                                    reverse=True)
            # print('tri 2 : par Score puis Classement')
            # for player in self.player_in_instance_sorted:
            #    print(str(player) + '  ' + str(player.player_score) + '  ' + str(player.player_rating))
            # creation des deux listes
            # Elements de la liste self.player_in_instance_sorted commençant par 0 iteration 2
            self.list1 = self.player_in_instance_sorted[::2]
            # Elements de la liste self.player_in_instance_sorted commençant par 1 iteration 2
            self.list2 = self.player_in_instance_sorted[1::2]
            # Test si match deja existant dans les rounds précédents
            # pour chaque prochain round
            for i in range(nbr_joueurs_by_list):
                # pour chaque id de round deja fait dans ce tournois
                for m in id.tournament_match_id:
                    # pour chaque matchs deja fait dans l'absolue
                    for p in lst_matchsobj:
                        if str(self.list1[i]) == p.match_player1 and str(
                                self.list2[i]) == p.match_player2 and m == p.match_id:
                            self.list1 = []
                            self.list1.append(self.player_in_instance_sorted[0])
                            self.list1.append(self.player_in_instance_sorted[1])
                            self.list1.append(self.player_in_instance_sorted[4])
                            self.list1.append(self.player_in_instance_sorted[5])
                            self.list2 = []
                            self.list2.append(self.player_in_instance_sorted[2])
                            self.list2.append(self.player_in_instance_sorted[3])
                            self.list2.append(self.player_in_instance_sorted[6])
                            self.list2.append(self.player_in_instance_sorted[7])
                            # print('une partie a deja été jouée, le tri a été modifié')
                            pass
                        if str(self.list1[i]) == p.match_player2 and str(
                                self.list2[i]) == p.match_player1 and m == p.match_id:
                            self.list1 = []
                            self.list1.append(self.player_in_instance_sorted[0])
                            self.list1.append(self.player_in_instance_sorted[1])
                            self.list1.append(self.player_in_instance_sorted[4])
                            self.list1.append(self.player_in_instance_sorted[5])
                            self.list2 = []
                            self.list2.append(self.player_in_instance_sorted[2])
                            self.list2.append(self.player_in_instance_sorted[3])
                            self.list2.append(self.player_in_instance_sorted[6])
                            self.list2.append(self.player_in_instance_sorted[7])
                            # print('une partie a deja été jouée, le tri a été modifié')
                            pass
                        else:
                            pass

    def match_datetime(self):
        return (str(datetime.datetime.now()))

    def create_match_id(self, lst_matchsobj):
        return int(len(lst_matchsobj)) + 1

    def add_tournament_in_match(self, kwargs_match, i, tournament_match_id_in_instance, lst_matchsobj, lst_players_obj_sorted_by_id):
        for key, value in kwargs_match.items():
            setattr(self, key, value)
        new_match = Match(match_id=kwargs_match['match_id'],
                          match_player1=kwargs_match['match_player1'],
                          match_score1=kwargs_match['match_score1'],
                          match_player2=kwargs_match['match_player2'],
                          match_score2=kwargs_match['match_score2'],
                          Datetime=kwargs_match['Datetime'])
        tournament_match_id_in_instance.append(self.match_id)
        lst_matchsobj.append(new_match)
        # Mise a jour du Rating dans les listes de joueurs
        for Player in lst_players_obj_sorted_by_id:
            # print(Player)
            # print(str(self.model.list1[i]))
            if str(Player) == str(self.list1[i]):
                Player.player_rating = (float(Player.player_rating) + float(new_match.match_score1))
            if str(Player) == str(self.list2[i]):
                Player.player_rating = (float(Player.player_rating) + float(new_match.match_score2))

    def match_by_round(self, id, lst_matchsobj):
        lst_round = id.tournament_match_id.copy()
        for round in range(int(id.tournament_nbr_round)):
            list_rnd_to_display = lst_round[:4]
            print('Matchs du round ' + str(round + 1))
            for match_id in list_rnd_to_display:
                for match in lst_matchsobj:
                    if match_id == match.match_id:
                        print(match)
            del lst_round[:4]