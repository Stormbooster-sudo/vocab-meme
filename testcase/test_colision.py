
from main import GameMain
from game_objects import Player, Items
import unittest

class ColisionTest(unittest.TestCase):
    def test_colision_itemA_pos_10_10_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (10, 10)
        pos = (10, 10)
        e2 = Items(pos = pos,speed =  0,item_type= "A", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)

    def test_colision_itemB_pos_10_10_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (20, 30)
        pos = (40, 50)
        e2 = Items(pos = pos,speed =  0,item_type= "B", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)

    def test_colision_itemC_pos_10_10_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (27, 45)
        pos = (38, 60)
        e2 = Items(pos = pos,speed =  0,item_type= "C", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)
