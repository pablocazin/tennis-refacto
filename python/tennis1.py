import json
import os
# ========================================================================================
# Toutes les modifications sont expliquées dans le fichier README.md à la racine du projet
# ========================================================================================

class Player:
    def __init__(self, name: str):
        self.name = name
        self.point = 0

    def setScore(self, value: int):
        self.point = value

class Language:
    def __init__(self, language: str):
        self.name = language
        self.love = None
        self.fifteen = None
        self.thirty = None
        self.forty = None
        self.love_all = None
        self.fifteen_all = None
        self.thirty_all = None
        self.deuce = None
        self.advantage = None
        self.win = None
        self.load_languages('languages.json')

    # Permet de charger le fichier json contenant toutes les langues avec les traductions
    def load_languages(self, config_file):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, config_file)

        with open(file_path, 'r') as file:
            data = json.load(file)
            for lang_data in data:
                if lang_data['name'] == self.name:
                    translate = lang_data
                
            if not translate:
                raise ValueError("Language not supported")

            self.love = translate['Love']
            self.fifteen = translate['Fifteen']
            self.thirty = translate['Thirty']
            self.forty = translate['Forty']
            self.love_all = translate['Love-All']
            self.fifteen_all = translate['Fifteen-All']
            self.thirty_all = translate['Thirty-All']
            self.deuce = translate['Deuce']
            self.advantage = translate['Advantage']
            self.win = translate['Win']

class TennisGame1:

    def __init__(self, player1: Player, player2: Player, language: Language):
        self.p1_name = player1.name
        self.p2_name = player2.name
        self.p1_points = player1.point
        self.p2_points = player2.point
        self.language = language

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
        if self.p1_points == self.p2_points:
            result = {
                0 : self.language.love_all,
                1 : self.language.fifteen_all,
                2 : self.language.thirty_all,
            }.get(self.p1_points, self.language.deuce)

        elif (self.p1_points >= 4 or self.p2_points >= 4):
            minus_result = self.p1_points - self.p2_points
            if (minus_result == 1):
                result = f"{self.language.advantage} {self.p1_name}"
            elif (minus_result == -1):
                result = f"{self.language.advantage} {self.p2_name}"
            elif (minus_result >= 2):
                result = f"{self.language.win} {self.p1_name}"
            else:
                result = f"{self.language.win} {self.p2_name}"
        else:
            for i in range(1,3):
                if (i == 1):
                    temp_score = self.p1_points
                else:
                    result += "-"
                    temp_score = self.p2_points

                result += {
                    0 : self.language.love,
                    1 : self.language.fifteen,
                    2 : self.language.thirty,
                    3 : self.language.forty,
                }[temp_score]

        return result
