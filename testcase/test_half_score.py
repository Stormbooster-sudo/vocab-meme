
from main import GameMain
from game_objects import Player, Items
import unittest

class HalfScoreTest(unittest.TestCase):
    def test_colision_itemA_pos_10_10_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (10, 10)
        pos = (10, 10)
        e2 = Items(pos = pos,speed =  0,item_type= "A", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)