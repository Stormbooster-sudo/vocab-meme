from main import GameMain
from kivy.graphics import Rectangle
import unittest

class HalfScoreTest(unittest.TestCase):
    def test_half_score_init_20(self):
        game = GameMain()
        game._score = 20
        game._score_instruction = Rectangle()
        game.half_score()

        expected_result = 10
        
        result = game._score

        self.assertEqual(result, expected_result)