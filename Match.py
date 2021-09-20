class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.p1_score = 0
        self.p2_score = 0
        self.description = ""

    def set_score(self, p1_score, p2_score):
        self.p1_score = p1_score
        self.p2_score = p2_score

    def set_description(self, description):
        self.description = description

    def __repr__(self):
        return f"{self.player1}{self.p1_score}, {self.player2}{self.p2_score}"

    def __str__(self):
        return str(self.__dict__)
