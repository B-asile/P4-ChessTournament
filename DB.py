from tinydb import TinyDB, Query

class DB:
    def __init__(self):
        self.db = TinyDB('db.json')
        self.table_players = self.db.table('Playercls')
        self.table_tournaments = self.db.table('Tournamentcls')
        self.db_player = Query()
        self.db_tournament = Query()

    # create tblePlayer/tournament a revoir
    # def create_table_player(self):
    #     self.db = TinyDB('db.json')
    #     self.table_players = self.db.table('Playercls')

    def load_players(self):
        return self.table_players.all()


    def load_tournament(self):
        return self.table_tournaments.all()

    # @staticmethod
    # def delete_all_table():
    #     DB.clean_db()

    def save_players(self, all_playersObj):
        for player in all_playersObj :
            self.table_players.upsert({ 'last_name' : player.last_name, 'first_name':  player.first_name, 'date_of_birth': player.date_of_birth, 'gender' : player.gender, 'rating': player.rating },
                                      (self.db_player['last_name'] == player.last_name) & (self.db_player['first_name'] == player.first_name) & (self.db_player['date_of_birth'] == player.date_of_birth) )

    def save_tournaments(self, all_tournaments):
        for tournament in all_tournaments :
            print(tournament.tournament_players)
            tournament_current_players = []
            for player in tournament.tournament_players :
                tournament_current_players.append( self.table_players.search(
                        (self.db_player['last_name'] == player.last_name) &
                        (self.db_player['first_name'] == player.first_name) &
                        (self.db_player['date_of_birth'] == player.date_of_birth) ))
            print(tournament_current_players)
            self.table_tournaments.upsert(
                {
                    'name' : tournament.name,
                    'location' : tournament.location,
                    'tournament_players' : tournament_current_players ,
                    'nb_round' : tournament.nbr_round,
                    'ctl_time' : tournament.ctl_time,
                    'description' : tournament.description },
                 self.db_tournament['name'] == tournament.name  )







