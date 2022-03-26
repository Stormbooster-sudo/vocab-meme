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
    
    def test_move_down_5_times(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        for i in range(5):
            game.keysPressed.add("s")
            player.move_step(sender=None, dt = 1/500)
            game.keysPressed.remove("s")
        
        expected_result = (0, -5.0)

        result = player.pos

        self.assertEqual(result, expected_result)
    
    def test_move_left_5_times(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        for i in range(5):
            game.keysPressed.add("a")
            player.move_step(sender=None, dt = 1/500)
            game.keysPressed.remove("a")
        
        expected_result = (-5.0, 0)

        result = player.pos

        self.assertEqual(result, expected_result)

    def test_move_right_5_times(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        for i in range(5):
            game.keysPressed.add("d")
            player.move_step(sender=None, dt = 1/500)
            game.keysPressed.remove("d")
        
        expected_result = (5.0, 0)

        result = player.pos

        self.assertEqual(result, expected_result)
    
    def test_move_right_7_times_move_up_10_times(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        for i in range(7):
            game.keysPressed.add("d")
            player.move_step(sender=None, dt = 1/500)
            game.keysPressed.remove("d")
        for i in range(10):
            game.keysPressed.add("w")
            player.move_step(sender=None, dt = 1/500)
            game.keysPressed.remove("w")
        
        expected_result = (7.0, 10.0)

        result = player.pos

        self.assertEqual(result, expected_result)
    
    def test_not_move_wrong_keyword_2_times(self):
        game = GameMain()
        player = Player(game)
        player.pos = (0,0)
        game.keysPressed.add("q")
        player.move_step(sender=None, dt = 1/500)
        game.keysPressed.remove("q")
        game.keysPressed.add("z")
        player.move_step(sender=None, dt = 1/500)
        game.keysPressed.remove("z")
        
        expected_result = (0, 0)

        result = player.pos

        self.assertEqual(result, expected_result)