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
        list_name = ["C","H","A","D","A","R","A","T"]
        for i in list_name:
            game.add_items(i)

        expected_result = "CHADARAT"

        result = game.get_items
        self.assertEqual(result, expected_result)

    def test_add_PANG(self):
        game = GameMain()
        list_name = ["P","A","N","G"]
        for i in list_name:
            game.add_items(i)

        expected_result = "PANG"

        result = game.get_items
        self.assertEqual(result, expected_result)

    def test_add_SOURCE(self):
        game = GameMain()
        list_name = ["S","O","U","R","C","E"]
        for i in list_name:
            game.add_items(i)
        
        expected_result = "SOURCE"

        result = game.get_items
        self.assertEqual(result, expected_result)

    def test_add_SAHACHAT(self):
        game = GameMain()
        list_name = ["S","A","H","A","C","H","A","T"]
        for i in list_name:
            game.add_items(i)
        
        expected_result = "SAHACHAT"

        result = game.get_items
        self.assertEqual(result, expected_result)

    def test_add_SUN(self):
        game = GameMain()
        list_name = ["S","U","N"]
        for i in list_name:
            game.add_items(i)
        
        expected_result = "SUN"

        result = game.get_items
        self.assertEqual(result, expected_result)

