# test_module.py
#
# Tests para el proyecto Rock Paper Scissors

import unittest
from RPS import player
from RPS_game import play, quincy, abbey, kris, mrugesh


class RPSGameTest(unittest.TestCase):
    def test_player_vs_quincy(self):
        result = play(player, quincy, 1000, verbose=False)
        p1_wins, p2_wins, _ = result
        self.assertGreaterEqual(
            p1_wins, p2_wins, "El jugador debería ganar o empatar contra quincy."
        )

    def test_player_vs_abbey(self):
        result = play(player, abbey, 1000, verbose=False)
        p1_wins, p2_wins, _ = result
        self.assertGreaterEqual(
            p1_wins, p2_wins, "El jugador debería ganar o empatar contra abbey."
        )

    def test_player_vs_kris(self):
        result = play(player, kris, 1000, verbose=False)
        p1_wins, p2_wins, _ = result
        self.assertGreaterEqual(
            p1_wins, p2_wins, "El jugador debería ganar o empatar contra kris."
        )

    def test_player_vs_mrugesh(self):
        result = play(player, mrugesh, 1000, verbose=False)
        p1_wins, p2_wins, _ = result
        self.assertGreaterEqual(
            p1_wins, p2_wins, "El jugador debería ganar o empatar contra mrugesh."
        )


def test():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(RPSGameTest)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    test()
