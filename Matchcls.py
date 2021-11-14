class Matchcls:
    def __init__(self, MatchID=0, MatchP1='Inconnu', MatchS1=0, MatchP2='Inconnu', MatchS2=0, Datetime='inconnu'):
        self.MatchID = MatchID
        self.MatchP1 = MatchP1
        self.MatchS1 = MatchS1
        self.MatchP2 = MatchP2
        self.MatchS2 = MatchS2
        self.Datetime = Datetime

    def __str__(self):
        return f"Match: {self.MatchP1} VS {self.MatchP2}"

    # def __repr__(self):
        # return f"Match: {self.MatchP1} VS {self.MatchP2}"
