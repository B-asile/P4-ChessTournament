class Match:
    def __init__(self, match_id=0, match_p1='Inconnu', match_s1=0, match_p2='Inconnu', match_s2=0, Datetime='inconnu'):
        self.match_id = match_id
        self.match_p1 = match_p1
        self.match_s1 = match_s1
        self.match_p2 = match_p2
        self.match_s2 = match_s2
        self.Datetime = Datetime

    def __int__(self, match):
        self.match_id = match['match_id']
        self.match_p1 = match['match_p1']
        self.match_s1 = match['match_s1']
        self.match_s2 = match['match_s2']
        self.Datetime = match['Datetime']

    def __str__(self):
        return f"match: {self.match_p1} VS {self.match_p2}"

    # def __repr__(self):
        # return f"match: {self.match_p1} VS {self.match_p2}"
