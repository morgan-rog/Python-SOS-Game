import tkinter
import unittest
from main import SOS_GAME_GUI

class TestSosGameGui(unittest.TestCase):
    # def test_set_blue_turn(self):
    #     game = SOS_GAME_GUI()
    #     game.set_blue_turn()
    #     return self.assertEqual(game.current_turn, game.BLUE_TURN)

    def test_make_move(self):
        # preconditions
        game = SOS_GAME_GUI()
        game.set_red_turn()
        game.red_player_option.set('S')

        game.make_move(1,0)
        return self.assertEqual(game.gameboard.get_cell_button_value(1,0), 'S')

    

        
