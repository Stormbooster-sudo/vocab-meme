from main import GameMain
import unittest

class AddItemTest(unittest.TestCase):
    def test_add_A(self):
        game = GameMain()
        game.add_items("A")
        
        expected_result = "A"

        result = game.get_items
        self.assertEqual(result, expected_result)

    def test_add_CHADARAT(self):
        game = GameMain()
        list_name = ['C','H','A','D','A','R','A','T']
        for i in list_name:
            game.add_items(i)

        expected_result = 'CHADARAT'

        result = game.get_items
        self.assertEqual(result, expected_result)

    def test_add_CHADARAT(self):
        game = GameMain()
        list_name = ['C','H','A','D','A','R','A','T']
        for i in list_name:
            game.add_items(i)

        expected_result = 'CHADARAT'

        result = game.get_items
        self.assertEqual(result, expected_result)