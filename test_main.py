import unittest
from main import SOS_GAME_GUI


class Test_SOS_GAME_GUI(unittest.TestCase):

    def setUp(self):
        self.game = SOS_GAME_GUI(3, True)
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
        self.game.red_player.option.set('S')
        return self.assertEqual(self.game.red_player.option.get(), 'S')

    def test_set_blue_player_option(self):
        self.game.blue_player.option.set('S')
        return self.assertEqual(self.game.blue_player.option.get(), 'S')

    def test_make_move_red(self):
        self.game.start_simple_game()
        self.game.set_red_turn()
        self.game.red_player.option.set('S')
        self.game.make_move(0,1)
        return self.assertEqual(self.game.get_cell_button_value(0,1), self.game.red_player.option.get())

    def test_make_move_blue(self):
        self.game.start_simple_game()
        self.game.set_blue_turn()
        self.game.blue_player.option.set('O')
        self.game.make_move(0,1)
        return self.assertEqual(self.game.get_cell_button_value(0,1), self.game.blue_player.option.get())

    def test_make_invalid_move(self):
        self.game.start_simple_game()
        self.game.set_red_turn()
        self.game.red_player.option.set('S')
        self.game.make_move(2,2)

        # blue tries to make move in spot occupied with 'O' from red's turn
        self.game.blue_player.option.set('O')
        self.game.make_move(2,2)

        return self.assertEqual(self.game.get_cell_button_value(2,2), 'S')

    def test_start_simple_game(self):
        self.game.start_simple_game()
        return self.assertEqual(self.game.gametype, self.game.SIMPLE_GAME)

    def test_start_general_game(self):
        self.game.start_general_game()
        return self.assertEqual(self.game.gametype, self.game.GENERAL_GAME)

    def test_check_if_full_board_empty(self):
        return self.assertEqual(self.game.check_if_full_board(), False)

    def test_check_if_full_board_full(self):
        for row in range(self.game.row_count):
            for col in range(self.game.col_count):
                self.game.board[row][col]['text'] = 'S'
        return self.assertEqual(self.game.check_if_full_board(), True)

    def test_red_win_simple_game(self):
        self.game.gametype = self.game.SIMPLE_GAME
        self.game.set_red_turn()
        self.game.red_player.option.set('S')
        self.game.board[0][1]['text'] = 'S'
        self.game.board[1][1]['text'] = 'O'
        self.game.make_move(2,1)
        self.assertEqual(self.game.red_player.get_wins(), 1)

    def test_blue_win_simple_game(self):
        self.game.gametype = self.game.SIMPLE_GAME
        self.game.set_blue_turn()
        self.game.blue_player.option.set('S')
        self.game.board[0][1]['text'] = 'S'
        self.game.board[1][1]['text'] = 'O'
        self.game.make_move(2,1)
        self.assertEqual(self.game.blue_player.get_wins(), 1)

    def test_draw_simple_game(self):
        self.game.gametype = self.game.GENERAL_GAME
        for row in range(self.game.row_count):
             for col in range(self.game.col_count):
                 self.game.board[row][col]['text'] = 'S'
        self.assertEqual(self.game.check_simple_game_status(2, 2, 'red'), 'draw')

    def test_full_board_general_game(self):
        self.game.gametype = self.game.GENERAL_GAME
        for row in range(self.game.row_count):
             for col in range(self.game.col_count):
                 self.game.board[row][col]['text'] = 'S'
        self.assertEqual(self.game.check_gen_game_status(2, 2, 'red'), 'full_board')

    def test_red_sos_score_general_game(self):
        self.game.gametype = self.game.GENERAL_GAME
        self.game.set_red_turn()
        self.game.red_player.option.set('S')
        self.game.board[0][1]['text'] = 'S'
        self.game.board[1][1]['text'] = 'O'
        self.game.make_move(2,1)
        self.assertEqual(self.game.red_player.get_sos(), 1)

    def test_blue_sos_score_general_game(self):
        self.game.gametype = self.game.GENERAL_GAME
        self.game.set_blue_turn()
        self.game.blue_player.option.set('S')
        self.game.board[0][1]['text'] = 'S'
        self.game.board[1][1]['text'] = 'O'
        self.game.make_move(2,1)
        self.assertEqual(self.game.blue_player.get_sos(), 1)