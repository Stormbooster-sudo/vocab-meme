from unittest import result
from main import GameMain
import unittest

class ClearItemTest(unittest.TestCase):
    def test_clear_item_B(self):
        game = GameMain()
        game.add_items("B")
        
        game.clear_items()

        expected_result = ""

        result = game.get_items
        self.assertEqual(result, expected_result)
    
    def test_clear_item_CHEM(self):
        game = GameMain()
        list_name = ['C','H','E','M']
        for i in list_name:
            game.add_items(i)
        
        game.clear_items()

        expected_result = ""

        result = game.get_items
        self.assertEqual(result, expected_result)
    
    def test_clear_CHADARAT(self):
        game = GameMain()
        list_name = ['C','H','A','D','A','R','A','T']
        for i in list_name:
            game.add_items(i)
        
        game.clear_items()

        expected_result = ""

        result = game.get_items
        self.assertEqual(result, expected_result)
    
    
    