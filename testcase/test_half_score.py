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

    def test_half_score_init_100(self):
        game = GameMain()
        game._score = 100
        game._score_instruction = Rectangle()
        game.half_score()

        expected_result = 50
        
        result = game._score

        self.assertEqual(result, expected_result)

    def test_half_score_init_24(self):
        game = GameMain()
        game._score = 24
        game._score_instruction = Rectangle()
        game.half_score()

        expected_result = 12
        
        result = game._score

        self.assertEqual(result, expected_result)

    def test_half_score_init_0(self):
        game = GameMain()
        game._score = 0
        game._score_instruction = Rectangle()
        game.half_score()

        expected_result = 0
        
        result = game._score

        self.assertEqual(result, expected_result)

    def test_half_score_init_99(self):
        game = GameMain()
        game._score = 99
        game._score_instruction = Rectangle()
        game.half_score()

        expected_result = 49
        
        result = game._score

        self.assertEqual(result, expected_result)

    def test_half_score_init_49(self):
        game = GameMain()
        game._score = 49
        game._score_instruction = Rectangle()
        game.half_score()

        expected_result = 24
        
        result = game._score

        self.assertEqual(result, expected_result)