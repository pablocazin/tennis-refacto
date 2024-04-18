import unittest

from tennis1 import TennisGame1


class GoldenMasterTest(unittest.TestCase):

    # Modifier en foncion de son chemin
    DIR = "C:\\EPSI\\Exo\\tennis-refacto\\python\\golden-master"
    languages = ['fr', 'en']
    @staticmethod
    def play_game(p1Points, p2Points, p1Name, p2Name, language):
        game = TennisGame1(p1Name, p2Name, language)
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        return game.score()

    def make_file_name(self, language, score_player_1, score_player_2):
        return f"{self.DIR}\\{language}_{score_player_1}_{score_player_2}.txt"

    def test_record(self):
        for language in self.languages:
            for score_player_1 in list(range(0, 16)):
                for score_player_2 in list(range(0, 16)):
                    with self.subTest(f"{score_player_1}, {score_player_2}"):
                        sortie = self.play_game(score_player_1, score_player_2, "player1", "player2", language)
                        file = open(self.make_file_name(language, score_player_1, score_player_2), "w")
                        file.writelines(sortie)
                        file.close()

    def test_replay(self):
        for language in self.languages:
            for score_player_1 in list(range(0, 16)):
                for score_player_2 in list(range(0, 16)):
                    with self.subTest(f"{score_player_1}, {score_player_2}"):
                        sortie = self.play_game(score_player_1, score_player_2, "player1", "player2", language)
                        file = open(self.make_file_name(language, score_player_1, score_player_2), "r")
                        attendu = file.read()
                        file.close()
                        self.assertEqual(attendu, sortie)

