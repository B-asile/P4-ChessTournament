class Player:

    def __init__(self, player_index=0, player_first_name='unknown', player_last_name='unknown', player_age=0,
                 player_date_of_birth='00/00/0000', player_gender='unknown', player_rating=0.0, player_score=0.0):
        self.player_index = player_index
        self.player_first_name = player_first_name
        self.player_last_name = player_last_name
        self.player_age = player_age
        self.player_date_of_birth = player_date_of_birth
        self.player_gender = player_gender
        self.player_rating = player_rating
        self.player_score = player_score

    def __str__(self):
        return f" {self.player_first_name} {self.player_last_name}"

    @staticmethod
    def player_sort_by_name(lst_playersobj):
        """Classer par Nom et Afficher la liste Joueurs de la BDD"""
        list_az = sorted(lst_playersobj, key=lambda x: x.player_first_name.lower(), reverse=False)
        return list_az

    @staticmethod
    def player_sort_by_rating(lst_playersobj):
        """Classer par Rating et Afficher la liste des Joueurs de la BDD"""
        list_rating = sorted(lst_playersobj, key=lambda x: int(x.player_rating), reverse=True)
        return list_rating

    @staticmethod
    def create_player_index(lst_playersobj):
        """Pour Créer de nouveaux Joueurs"""
        return int(len(lst_playersobj)) + 1

    def add_player_in_class(self, kwargs_player):
        for key, value in kwargs_player.items():
            setattr(self, key, value)
            new_player = Player(player_index=kwargs_player['player_index'],
                                player_first_name=kwargs_player['player_first_name'],
                                player_last_name=kwargs_player['player_last_name'],
                                player_age=kwargs_player['player_age'],
                                player_date_of_birth=kwargs_player['player_date_of_birth'],
                                player_gender=kwargs_player['player_gender'],
                                player_rating=kwargs_player['player_rating'],
                                player_score=kwargs_player['player_score'])
            return new_player
