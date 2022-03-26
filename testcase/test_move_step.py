from unittest import result
from game_objects import Player
from main import GameMain
from game_objects import Player
import unittest

class MoveStepTest(unittest.TestCase):
    def test_move_up_1_time(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        game.keysPressed.add("w")
        player.move_step(sender=None, dt = 1/500)
        
        expected_result = (0, 1.0)

        result = player.pos

        self.assertEqual(result, expected_result)
    
    def test_move_down_1_time(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        game.keysPressed.add("s")
        player.move_step(sender=None, dt = 1/500)
        
        expected_result = (0, -1.0)

        result = player.pos

        self.assertEqual(result, expected_result)

    def test_move_right_1_time(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        game.keysPressed.add("d")
        player.move_step(sender=None, dt = 1/500)
        
        expected_result = (1.0, 0)

        result = player.pos

        self.assertEqual(result, expected_result)

    def test_move_left_1_time(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        game.keysPressed.add("a")
        player.move_step(sender=None, dt = 1/500)
        
        expected_result = (-1.0, 0)

        result = player.pos

        self.assertEqual(result, expected_result)

    def test_move_up_5_time(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        for i in range(5):
            game.keysPressed.add("w")
            player.move_step(sender=None, dt = 1/500)
            game.keysPressed.remove("w")
        
        expected_result = (0, 5.0)

        result = player.pos

        self.assertEqual(result, expected_result)