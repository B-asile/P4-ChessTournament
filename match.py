class Match:
    def __init__(self, match_id=0, match_player1='Inconnu', match_score1=0, match_player2='Inconnu', match_score2=0, Datetime='inconnu'):
        self.match_id = match_id
        self.match_player1 = match_player1
        self.match_score1 = match_score1
        self.match_player2 = match_player2
        self.match_score2 = match_score2
        self.Datetime = Datetime

    def __int__(self, match):
        self.match_id = match['match_id']
        self.match_player1 = match['match_player1']
        self.match_score1 = match['match_score1']
        self.match_score2 = match['match_score2']
        self.Datetime = match['Datetime']

    def __str__(self):
        return f"match: {self.match_player1} VS {self.match_player2}"

    # def __repr__(self):
        # return f"match: {self.match_player1} VS {self.match_player2}"
