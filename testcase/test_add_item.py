from main import GameMain
import unittest

class AddItemTest(unittest.TestCase):
    def test_add_A(self):
        game = GameMain()
        game.add_items("A")
        
        expected_result = "A"

        result = game.get_items
        self.assertEqual(result, expected_result)

    