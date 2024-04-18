import unittest

from tennis1 import TennisGame1, Player


class GoldenMasterTest(unittest.TestCase):

    # Modifier en foncion de son chemin de dossier
    DIR = "C:\\EPSI\\Exo\\tennis-refacto\\python\\golden-master"
    languages = ['fr', 'en']

    player_1 = Player("player1")
    player_2 = Player("player2")

    @staticmethod
    def play_game(player1: Player, player2: Player, language):
        game = TennisGame1(player1, player2, language)
        for i in range(max(player1.point, player2.point)):
            if i < player1.point:
                game.won_point(player1.name)
            if i < player2.point:
                game.won_point(player2.name)
        return game.score()

    def make_file_name(self, language, score_player_1, score_player_2):
        return f"{self.DIR}\\{language}_{score_player_1}_{score_player_2}.txt"

    def test_record(self):
        for language in self.languages:
            for score_player_1 in list(range(0, 16)):
                for score_player_2 in list(range(0, 16)):
                    self.player_1.setScore(score_player_1)
                    self.player_2.setScore(score_player_2)
                    with self.subTest(f"{self.player_1.point}, {self.player_2.point}"):
                        sortie = self.play_game(self.player_1, self.player_2, language)
                        file = open(self.make_file_name(language, self.player_1.point, self.player_2.point), "w")
                        file.writelines(sortie)
                        file.close()

    def test_replay(self):
        for language in self.languages:
            for score_player_1 in list(range(0, 16)):
                for score_player_2 in list(range(0, 16)):
                    self.player_1.setScore(score_player_1)
                    self.player_2.setScore(score_player_2)
                    with self.subTest(f"{self.player_1.point}, {self.player_2.point}"):
                        sortie = self.play_game(self.player_1, self.player_2, language)
                        file = open(self.make_file_name(language, self.player_1.point, self.player_2.point), "r")
                        attendu = file.read()
                        file.close()
                        self.assertEqual(attendu, sortie)

