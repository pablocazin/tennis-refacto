# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_points += 1
        else:
            self.p2_points += 1

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
            minus_result = self.p1_points-self.p2_points
            if (minus_result==1):
                result ="Advantage player1"
            elif (minus_result ==-1):
                result ="Advantage player2"
            elif (minus_result>=2):
                result = "Win for player1"
            else:
                result ="Win for player2"
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
