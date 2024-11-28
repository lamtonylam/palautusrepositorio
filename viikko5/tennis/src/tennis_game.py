class TennisGame:
    # Point terms
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3

    # Point explainers
    WINNING_SCORE = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def draw_points(self):
        if self.player1_score == TennisGame.LOVE:
            self.score = "Love-All"
        elif self.player1_score == TennisGame.FIFTEEN:
            self.score = "Fifteen-All"
        elif self.player1_score == TennisGame.THIRTY:
            self.score = "Thirty-All"
        else:
            self.score = "Deuce"

        return self.score

    def winning_points(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            self.score = "Advantage player1"
        elif score_difference == -1:
            self.score = "Advantage player2"
        elif score_difference >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"

        return self.score

    def normal_points(self):
        temp_score = 0

        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                self.score = self.score + "-"
                temp_score = self.player2_score

            if temp_score == TennisGame.LOVE:
                self.score = self.score + "Love"
            elif temp_score == TennisGame.FIFTEEN:
                self.score = self.score + "Fifteen"
            elif temp_score == TennisGame.THIRTY:
                self.score = self.score + "Thirty"
            elif temp_score == TennisGame.FORTY:
                self.score = self.score + "Forty"

        return self.score

    def get_score(self):
        self.score = ""

        if self.player1_score == self.player2_score:
            self.draw_points()

        elif (
            self.player1_score >= TennisGame.WINNING_SCORE
            or self.player2_score >= TennisGame.WINNING_SCORE
        ):
            self.winning_points()

        else:
            self.normal_points()

        return self.score
