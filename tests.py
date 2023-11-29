import unittest
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_initial_empty_board(self):
        game = TicTacToe()
        self.assertEqual(game.board, [[None, None, None], [None, None, None], [None, None, None]])

    def test_game_mode_initialization(self):
        single_player_game = TicTacToe(single_player=True)
        two_player_game = TicTacToe(single_player=False)
        self.assertIsNotNone(single_player_game.bot)
        self.assertIsNone(two_player_game.bot)

    def test_unique_piece_assignment(self):
        game = TicTacToe()
        self.assertIn(game.current_player, ['X', 'O'])

    def test_switch_player(self):
        game = TicTacToe()
        first_player = game.current_player
        game.switch_player()
        second_player = game.current_player
        self.assertNotEqual(first_player, second_player)

    def test_end_game_conditions(self):
        game = TicTacToe()
        game.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
        self.assertEqual(game.check_winner(), 'X')
        game.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertEqual(game.check_winner(), 'draw')

    def test_play_in_valid_spot(self):
        game = TicTacToe()
        game.board = [['X', None, None], [None, 'O', None], [None, None, 'X']]
        game.board[1][0] = 'O'  
        self.assertNotEqual(game.board[1][0], 'X')

    def test_correct_winner_detection(self):
        game = TicTacToe()
        game.board = [['O', 'O', 'O'], [None, 'X', None], ['X', None, 'X']]
        self.assertEqual(game.check_winner(), 'O')

if __name__ == '__main__':
    unittest.main()
