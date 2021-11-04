import unittest
from main import SOS_GAME_GUI

class Test_SOS_GAME_GUI(unittest.TestCase):

    def setUp(self):
        self.game = SOS_GAME_GUI()
        self.game.create_GUI_gameboard()

    def tearDown(self):
        return None

    def test_set_red_turn(self):
        self.game.set_red_turn()
        return self.assertEqual(self.game.current_turn.get(), self.game.RED_TURN)

    def test_set_blue_turn(self):
        self.game.set_blue_turn()
        return self.assertEqual(self.game.current_turn.get(), self.game.BLUE_TURN)

    def test_set_red_player_option(self):
        self.game.red_player_option.set('S')
        return self.assertEqual(self.game.red_player_option.get(), 'S')

    def test_set_blue_player_option(self):
        self.game.blue_player_option.set('S')
        return self.assertEqual(self.game.blue_player_option.get(), 'S')

    def test_start_simple_game(self):
        self.game.start_simple_game()
        return self.assertEqual(self.game.gametype, self.game.SIMPLE_GAME)

    def test_start_general_game(self):
        self.game.start_general_game()
        return self.assertEqual(self.game.gametype, self.game.GENERAL_GAME)

    def test_make_move_red(self):
        self.game.start_simple_game()
        self.game.set_red_turn()
        self.game.red_player_option.set('S')
        self.game.make_move(3,5)
        return self.assertEqual(self.game.gameboard.get_cell_button_value(3,5), self.game.red_player_option.get())

    def test_make_move_blue(self):
        self.game.start_simple_game()
        self.game.set_blue_turn()
        self.game.blue_player_option.set('O')
        self.game.make_move(4,4)
        return self.assertEqual(self.game.gameboard.get_cell_button_value(4,4), self.game.blue_player_option.get())

    def test_make_invalid_move(self):
        self.game.start_simple_game()
        self.game.set_red_turn()
        self.game.red_player_option.set('S')
        self.game.make_move(2,2)

        # blue tries to make move in spot occupied with 'O' from red's turn
        # self.game.set_blue_turn()
        # self.game.blue_player_option.set('O')
        self.game.make_move(2,2)

        return self.assertEqual(self.game.gameboard.get_cell_button_value(2,2), 'S')


class Test_SOS_GAME_BOARD(unittest.TestCase):
    def setUp(self):
        self.game = SOS_GAME_GUI()
        self.game.create_GUI_gameboard()

    def tearDown(self):
        return None

    def test_check_if_full_board_empty(self):
        return self.assertEqual(self.game.gameboard.check_if_full_board(), False)

    def test_check_if_full_board_full(self):
        for row in range(self.game.gameboard.NUM_ROWS):
            for col in range(self.game.gameboard.NUM_COLS):
                self.game.gameboard.board[row][col]['text'] == 'S'

        return self.assertEqual(self.game.gameboard.check_if_full_board(), True)