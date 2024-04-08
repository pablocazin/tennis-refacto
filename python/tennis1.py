# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_points = 0
        self.p2_points = 0

    # Ajoute un point au joueur correspondant
    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    # Retourne le score en fonction du score des joueurs
    def score(self):
        result = ""
        temp_score=0
        if (self.p1_points==self.p2_points):
            result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1_points, "Deuce")
        elif (self.p1_points>=4 or self.p2_points>=4):
            minus_result = self.p1_points - self.p2_points
            if (minus_result == 1):
                result = f"Advantage {self.p1_name}"
            elif (minus_result == -1):
                result = f"Advantage {self.p2_name}"
            elif (minus_result >= 2):
                result = f"Win for {self.p1_name}"
            else:
                result = f"Win for {self.p2_name}"
        else:
            for i in range(1,3):
                if (i==1):
                    temp_score = self.p1_points
                else:
                    result+="-"
                    temp_score = self.p2_points
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[temp_score]
        return result
