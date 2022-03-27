
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

    def test_colision_itemB_pos_40_50_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (20, 30)
        pos = (40, 50)
        e2 = Items(pos = pos,speed =  0,item_type= "B", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)

    def test_colision_itemC_pos_38_56_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (27, 45)
        pos = (38, 56)
        e2 = Items(pos = pos,speed =  0,item_type= "C", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)

    def test_not_colision_itemD_pos_600_700_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (20, 30)
        pos = (600, 700)
        e2 = Items(pos = pos,speed =  0,item_type= "D", game = game)

        result = game.collides(e1, e2)
        self.assertFalse(result)

    def test_not_colision_itemE_pos_800_820_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (40, 60)
        pos = (800, 820)
        e2 = Items(pos = pos,speed =  0,item_type= "E", game = game)

        result = game.collides(e1, e2)
        self.assertFalse(result)
    
    def test_colision_itemF_pos_45_57_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (15, 27)
        pos = (45, 57)
        e2 = Items(pos = pos,speed =  0,item_type= "F", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)
    
    def test_colision_itemG_pos_134_107_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (85, 58)
        pos = (134, 107)
        e2 = Items(pos = pos,speed =  0,item_type= "G", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)
    
    def test_colision_itemH_pos_62_72_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (18, 28)
        pos = (62, 72)
        e2 = Items(pos = pos,speed =  0,item_type= "H", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)

    def test_colision_itemI_pos_99_134_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (52, 87)
        pos = (99, 134)
        e2 = Items(pos = pos,speed =  0,item_type= "I", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)

    def test_colision_itemJ_pos_88_99_true(self):
        game = GameMain()
        e1 = Player(game)
        e1.pos = (38, 49)
        pos = (88, 99)
        e2 = Items(pos = pos,speed =  0,item_type= "J", game = game)

        result = game.collides(e1, e2)
        self.assertTrue(result)


