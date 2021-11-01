from tkinter import *
from tkinter import messagebox
from datetime import datetime
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

class SOS_GAME_BOARD():

    NUM_ROWS = 8
    NUM_COLS = 8

    board = []

    def __init__(self):
        self.create_board()

    def create_board(self):
        for row in range(self.NUM_ROWS):
            self.board.append([])
            for col in range(self.NUM_COLS):
                self.board[row].append(0)  # append empty cell

    def reset_board(self):
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                tile = self.board[r][c]
                tile['text'] = ' '
                tile['bg'] = 'white'

    def get_cell_button(self, row, col):
        return self.board[row][col]

    def get_cell_button_value(self, row, col):
        return self.board[row][col]['text']

    def check_if_full_board(self):
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                if self.board[row][col]['text'] == ' ':
                    return False
        return True

    def middle_move_check(self, move_row, move_col, player_color):
        '''selected move tile is in the middle'''
        move_tile = self.board[move_row][move_col]
        try:
            if self.board[move_row][move_col-1]['text'] == 'S' and self.board[move_row][move_col+1]['text'] == 'S':
                # left to right
                self.board[move_row][move_col-1]['bg'] = player_color
                self.board[move_row][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        try:
            if self.board[move_row-1][move_col]['text'] == 'S' and self.board[move_row+1][move_col]['text'] == 'S':
                # up and down
                self.board[move_row-1][move_col]['bg'] = player_color
                self.board[move_row+1][move_col]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        try:
            if self.board[move_row+1][move_col-1]['text'] == 'S' and self.board[move_row-1][move_col+1]['text'] == 'S':
                # down left to up right diag
                self.board[move_row+1][move_col-1]['bg'] = player_color
                self.board[move_row-1][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        try:
            if self.board[move_row-1][move_col-1]['text'] == 'S' and self.board[move_row+1][move_col+1]['text'] == 'S':
                # up left to down right diag
                self.board[move_row-1][move_col-1]['bg'] = player_color
                self.board[move_row+1][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')

        return False

    def right_move_check(self, move_row, move_col, player_color):
        '''selected move tile is far right'''
        move_tile = self.board[move_row][move_col]
        try:
            if self.board[move_row][move_col-2]['text'] == 'S' and self.board[move_row][move_col-1]['text'] == 'O':
                # left to right
                self.board[move_row][move_col-2]['bg'] = player_color
                self.board[move_row][move_col-1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        try:
            if self.board[move_row-2][move_col]['text'] == 'S' and self.board[move_row-1][move_col]['text'] == 'O':
                # up and down
                self.board[move_row-2][move_col]['bg'] = player_color
                self.board[move_row-1][move_col]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        try:
            if self.board[move_row+2][move_col-2]['text'] == 'S' and self.board[move_row+1][move_col-1]['text'] == 'O':
                # down left to up right diag
                self.board[move_row+2][move_col-2]['bg'] = player_color
                self.board[move_row+1][move_col-1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        try:
            if self.board[move_row-2][move_col-2]['text'] == 'S' and self.board[move_row-1][move_col-1]['text'] == 'O':
                # up left to down right diag
                self.board[move_row-2][move_col-2]['bg'] = player_color
                self.board[move_row-1][move_col-1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        
        return False


    def left_move_check(self, move_row, move_col, player_color):
        '''selected move tile is far left'''
        move_tile = self.board[move_row][move_col]
        try:
            if self.board[move_row][move_col+2]['text'] == 'S' and self.board[move_row][move_col+1]['text'] == 'O':
                # left to right
                self.board[move_row][move_col+2]['bg'] = player_color
                self.board[move_row][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        try:
            if self.board[move_row+2][move_col]['text'] == 'S' and self.board[move_row+1][move_col]['text'] == 'O':
                # up and down
                self.board[move_row+2][move_col]['bg'] = player_color
                self.board[move_row+1][move_col]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        try:
            if self.board[move_row-2][move_col+2]['text'] == 'S' and self.board[move_row-1][move_col+1]['text'] == 'O':
                # down left to up right diag
                self.board[move_row-2][move_col+2]['bg'] = player_color
                self.board[move_row-1][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        try:
            if self.board[move_row+2][move_col+2]['text'] == 'S' and self.board[move_row+1][move_col+1]['text'] == 'O':
                # up left to down right diag
                self.board[move_row+2][move_col+2]['bg'] = player_color
                self.board[move_row+1][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            print('index error')
        
        return False


    def general_game_is_winner(self, move_row, move_col, player_color):
        '''returns true if game over, else false'''
        '''General game: The game continues until the board has been filled up. The winner is the 
            player who made the most SOSs. If both players made the same number of SOSs, then 
            the game is a draw. When a player succeeds in creating an SOS, that player immediately 
            akes another turn and continues to do so until no SOS is created on their turn. Otherwise,
            turns alternate between players after each move'''
        symbol = self.board[move_row][move_col]['text']
        if self.check_if_full_board():
            return 'full_board'
        if symbol == 'O':
            if self.middle_move_check(move_row, move_col, player_color):
                return 'win'
        elif symbol == 'S':
            if self.right_move_check(move_row, move_col, player_color) or self.left_move_check(move_row, move_col, player_color):
                return 'win'
        

    def simple_game_is_winner(self, move_row, move_col, player_color):
        '''returns true if game over, else false'''
        '''Simple game: The player who creates the first SOS is the winner. If no SOS is created
            when the board has been filled up, then the game is a draw. Turns alternate between 
            players after each move'''
        symbol = self.board[move_row][move_col]['text']

        if self.check_if_full_board():
            return 'draw'
        elif symbol == 'O':
            if self.middle_move_check(move_row, move_col, player_color):
                return 'win'
        elif symbol == 'S':
            if self.right_move_check(move_row, move_col, player_color) or self.left_move_check(move_row, move_col, player_color):
                return 'win'
        


class SOS_GAME_GUI():
    # define window and widget variables
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 500
    WINDOW = Tk()
    WINDOW_TITLE = 'Morgan\'s SOS Game'
    BUTTON_HEIGHT = 3
    BUTTON_WIDTH = 6
    SIMPLE_GAME = 'Simple Game'
    GENERAL_GAME = 'General Game'
    RED_TURN = 'Red\'s Turn'
    BLUE_TURN = 'Blue\'s Turn'
    

    def __init__(self):
        self.gameboard = SOS_GAME_BOARD()
        self.gametype = ' '
        self.red_player_option = StringVar()
        self.blue_player_option = StringVar()
        self.current_turn = StringVar()
        self.red_wins = 0
        self.blue_wins = 0
        self.red_sos_count = 0
        self.blue_sos_count = 0
        self.set_red_turn()

    def start(self):
        # place window on computer screen, listen for events
        self.WINDOW.mainloop()

    def record_game(self):
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        with open('game_scores.txt', 'a') as file:
            file.write(f'{dt_string}\n')
            file.write(f'\tRED # of wins: {self.red_wins}\n')
            file.write(f'\tBLUE # of wins: {self.blue_wins}\n\n')

    def restart(self):
        self.gameboard.reset_board()
        self.record_game()
        self.set_red_turn()

    def create_GUI_gameboard(self):
        self.WINDOW.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.WINDOW.title(self.WINDOW_TITLE)
        
        for r in range(self.gameboard.NUM_ROWS):
            for c in range(self.gameboard.NUM_COLS):
                tile = self.gameboard.board[r][c] = Button(self.WINDOW, bg="white", text=' ', height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, command=lambda row1 = r, col1 = c: self.make_move(row1, col1))
                tile.grid(row=r, column=c, padx= 2, pady=2)

        # simple and general game buttons
        simple_game_button = Radiobutton(self.WINDOW, text='Simple Game', variable=self.gametype, value=self.SIMPLE_GAME, command=lambda: self.start_simple_game())
        simple_game_button.grid(row=0, column=9)
        general_game_button = Radiobutton(self.WINDOW, text='General Game', variable=self.gametype, value=self.GENERAL_GAME, command=lambda: self.start_general_game())
        general_game_button.grid(row=0, column=10)

        # restart game button
        restart_game_button = Button(self.WINDOW, text= 'Restart Game', command=lambda: self.restart())
        restart_game_button.grid(row=7, column=11)

        # player labels
        red_player_label = Label(self.WINDOW, text='RED PLAYER')
        red_player_label.grid(row=2, column=9)
        blue_player_label = Label(self.WINDOW, text='BLUE PLAYER')
        blue_player_label.grid(row=2, column=10, padx=100)

        # player S/O radio buttons
        red_player_S_button = Radiobutton(self.WINDOW, text='S', variable= self.red_player_option, value='S')
        red_player_S_button.grid(row=3, column=9)
        red_player_O_button = Radiobutton(self.WINDOW, text='O', variable= self.red_player_option, value='O')
        red_player_O_button.grid(row=4, column=9)
        blue_player_S_button = Radiobutton(self.WINDOW, text='S', variable= self.blue_player_option, value='S')
        blue_player_S_button.grid(row=3, column=10)
        blue_player_O_button = Radiobutton(self.WINDOW, text='O', variable= self.blue_player_option, value='O')
        blue_player_O_button.grid(row=4, column=10)

        # output of current turn label
        current_turn_label = Label(self.WINDOW, textvariable=self.current_turn)
        current_turn_label.grid(row=6, column=9)

    def radio_click(self):
        print('Red value: ', self.red_player_option.get())
        print('Blue value: ', self.blue_player_option.get())

    def start_simple_game(self):
        self.gametype = self.SIMPLE_GAME
        #self.restart()
        messagebox.showinfo('Game', self.gametype)
        
    def start_general_game(self):
        self.gametype = self.GENERAL_GAME
        #self.restart()
        messagebox.showinfo('Game', self.gametype)

    def show_player_win_message(self, winning_player):
        if winning_player == 'red':
            messagebox.showinfo('WINNER', 'RED WINS')
        elif winning_player == 'blue':
            messagebox.showinfo('WINNER', 'BLUE WINS')

    def show_draw_message(self):
        messagebox.showinfo('DRAW', 'THIS GAME IS A DRAW')

    def make_move(self, row, col):
        # print('row: ', row, ' col: ', col)
        tile = self.gameboard.get_cell_button(row, col)

        if self.gametype == ' ':
            messagebox.showerror('choose gamemode', 'please choose a gamemode')

        elif tile['text'] == 'S' or tile['text'] == 'O':
            messagebox.showerror('tile occupied', 'cannot make a move here - choose another tile')

        elif (self.get_current_turn() == self.RED_TURN):
            tile['text'] = self.red_player_option.get()
            color = 'red'

            if self.gametype == self.SIMPLE_GAME:
                simple_game_status = self.gameboard.simple_game_is_winner(row, col, color)
                if simple_game_status == 'win':
                    self.show_player_win_message('red')
                    self.red_wins += 1
                    self.restart()
                elif simple_game_status == 'draw':
                    self.show_draw_message()
                    self.restart()
                else:
                    self.set_blue_turn()

            elif self.gametype == self.GENERAL_GAME:
                gen_game_status = self.gameboard.general_game_is_winner(row, col, color)
                if gen_game_status == 'win':
                    self.red_sos_count += 1
                elif gen_game_status == 'full_board':
                    if self.red_sos_count > self.blue_sos_count:
                        self.show_player_win_message('red')
                        self.red_wins += 1
                        self.restart()
                    elif self.blue_sos_count > self.red_sos_count:
                        self.show_player_win_message('blue')
                        self.blue_wins += 1
                        self.restart()
                    else:
                        self.show_draw_message()
                        self.restart()
                else:
                    self.set_blue_turn()

        elif (self.get_current_turn() == self.BLUE_TURN):
            tile['text'] = self.blue_player_option.get()
            color = 'blue'

            if self.gametype == self.SIMPLE_GAME:
                simple_game_status = self.gameboard.simple_game_is_winner(row, col, color)
                if simple_game_status == 'win':
                    self.show_player_win_message('blue')
                    self.blue_wins += 1
                    self.restart()
                elif simple_game_status == 'draw':
                    self.show_draw_message()
                    self.restart()
                else:
                    self.set_red_turn()

            if self.gametype == self.GENERAL_GAME:
                gen_game_status = self.gameboard.general_game_is_winner(row, col, color)
                if gen_game_status == 'win':
                    self.blue_sos_count += 1
                elif gen_game_status == 'full_board':
                    if self.red_sos_count > self.blue_sos_count:
                        self.show_player_win_message('red')
                        self.red_wins += 1
                        self.restart()
                    elif self.blue_sos_count > self.red_sos_count:
                        self.show_player_win_message('blue')
                        self.blue_wins += 1
                        self.restart()
                    else:
                        self.show_draw_message()
                        self.restart()
                else:
                    self.set_red_turn()

    def get_current_turn(self):
        return self.current_turn.get()

    def set_red_turn(self):
        self.current_turn.set(self.RED_TURN)
        
    def set_blue_turn(self):
        self.current_turn.set(self.BLUE_TURN)


if __name__ == '__main__':
    game = SOS_GAME_GUI()
    game.create_GUI_gameboard()
    game.start()