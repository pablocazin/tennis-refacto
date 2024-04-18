# ========================================================================================
# Toutes les modifications sont expliquées dans le fichier README.md à la racine du projet
# ========================================================================================

class Player:
    def __init__(self, name: str):
        self.name = name
        self.point = 0

    def setScore(self, value: int):
        self.point = value

class TennisGame1:

    def __init__(self, player1: Player, player2: Player, language):
        self.p1_name = player1.name
        self.p2_name = player2.name
        self.p1_points = player1.point
        self.p2_points = player2.point
        self.language = language

        # Configuration des textes en français et en anglais
        self.config = {
            "fr": {
                "Love": "Zéro",
                "Fifteen": "Quinze",
                "Thirty": "Trente",
                "Forty": "Quarante",
                "Love-All": "Égalité",
                "Fifteen-All": "Égalité",
                "Thirty-All": "Égalité",
                "Deuce": "Égalité",
                "Advantage": "Avantage",
                "Win": "Victoire pour"
            },
            "en": {
                "Love": "Love",
                "Fifteen": "Fifteen",
                "Thirty": "Thirty",
                "Forty": "Forty",
                "Love-All": "Love-All",
                "Fifteen-All": "Fifteen-All",
                "Thirty-All": "Thirty-All",
                "Deuce": "Deuce",
                "Advantage": "Advantage",
                "Win": "Win for"
            }
        }

        # Vérification de la langue
        if self.language not in self.config:
            raise ValueError("Langue non prise en charge")

    # Ajoute un point au joueur correspondant
    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    # Obtenir la traduction d'un text
    def get_translate(self, text):
        return self.config[self.language].get(text, text)

    # Retourne le score en fonction du score des joueurs
    def score(self):
        result = ""
        temp_score=0
        if self.p1_points == self.p2_points:
            result = self.get_translate({
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1_points, "Deuce"))

        elif (self.p1_points >= 4 or self.p2_points >= 4):
            minus_result = self.p1_points - self.p2_points
            if (minus_result == 1):
                result = f"{self.get_translate('Advantage')} {self.get_translate(self.p1_name)}"
            elif (minus_result == -1):
                result = f"{self.get_translate('Advantage')} {self.get_translate(self.p2_name)}"
            elif (minus_result >= 2):
                result = f"{self.get_translate('Win')} {self.get_translate(self.p1_name)}"
            else:
                result = f"{self.get_translate('Win')} {self.get_translate(self.p2_name)}"
        else:
            for i in range(1,3):
                if (i == 1):
                    temp_score = self.p1_points
                else:
                    result += "-"
                    temp_score = self.p2_points

                result += self.get_translate({
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[temp_score])

        return result
