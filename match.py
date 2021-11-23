class Matchcls:
    def __init__(self, match_id=0, match_p1='Inconnu', match_s1=0, MatchP2='Inconnu', MatchS2=0, Datetime='inconnu'):
        self.match_id = match_id
        self.match_p1 = match_p1
        self.match_s1 = match_s1
        self.MatchP2 = MatchP2
        self.MatchS2 = MatchS2
        self.Datetime = Datetime

    def __int__(self, match):
        self.match_id = match['match_id']
        self.match_p1 = match['match_p1']
        self.match_s1 = match['match_s1']
        self.MatchS2 = match['MatchS2']
        self.Datetime = match['Datetime']

    def __str__(self):
        return f"Match: {self.match_p1} VS {self.MatchP2}"

    # def __repr__(self):
        # return f"Match: {self.match_p1} VS {self.MatchP2}"
