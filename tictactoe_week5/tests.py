import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_board_with_space(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.board_with_space(board), True)

    def test_board_with_space(self):
        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.board_with_space(board), False)

    def test_other_player(self):
        player = 'X'    
        self.assertEqual(logic.other_player(player), 'O')  
    
    def test_make_move(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', None],
        ]
        player = 'X'
        x = 3
        y = 3
        self.assertEqual(logic.make_move(board, player, x, y), [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]) 

    def test_empty_spot(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', None],
        ] 
        x = 3
        y = 3
        self.assertEqual(logic.empty_spot(board, x, y), True)              
    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()