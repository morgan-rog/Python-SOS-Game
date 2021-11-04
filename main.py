from tkinter import *
from tkinter import messagebox
from datetime import datetime
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets


class Player():
    def __init__(self, name, color):
        #self.id = id
        self.name = name
        self.color = color
        self.num_wins = 0
        self.num_sos = 0
        self.option = StringVar()

    # def get_id(self):
    #     return self.id
    def add_win(self):
        self.num_wins += 1
    
    def reset_wins(self):
        self.num_wins = 0

    def add_sos(self):
        self.num_sos += 1

    def reset_sos(self):
        self.num_sos = 0

    def get_wins(self):
        return self.num_wins
    
    def get_sos(self):
        return self.num_sos

    def get_option(self):
        return self.option
    
    
class SOS_GAME_BOARD():

    def __init__(self, board_size):
        self.row_count = board_size
        self.col_count = board_size
        self.board = []
        self.create_board_skeleton()

    def create_board_skeleton(self):
        for row in range(self.row_count):
            self.board.append([])
            for col in range(self.col_count):
                self.board[row].append(0)  # append empty cell

    def reset_board(self):
        for r in range(self.row_count):
            for c in range(self.col_count):
                tile = self.board[r][c]
                tile['text'] = ' '
                tile['bg'] = 'white'

    def get_cell_button(self, row, col):
        return self.board[row][col]

    def get_cell_button_value(self, row, col):
        return self.board[row][col]['text']

    def check_if_full_board(self):
        for row in range(self.row_count):
            for col in range(self.col_count):
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

    def check_gen_game_status(self, move_row, move_col, player_color):
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

    def check_simple_game_status(self, move_row, move_col, player_color):
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


class SOS_GAME_GUI(SOS_GAME_BOARD):

    def __init__(self, board_size):
        super().__init__(board_size)
        # define window and widget variables
        self.WINDOW = Tk()
        self.WINDOW_WIDTH = board_size * 125
        self.WINDOW_HEIGHT = board_size * 70
        self.WINDOW_TITLE = 'Morgan\'s SOS Game'
        self.BUTTON_HEIGHT = 3
        self.BUTTON_WIDTH = 6
        self.SIMPLE_GAME = 'Simple Game'
        self.GENERAL_GAME = 'General Game'
        self.RED_TURN = 'Red\'s Turn'
        self.BLUE_TURN = 'Blue\'s Turn'
        self.gametype = ' '
        self.red_player = Player("red player", "red")
        self.blue_player = Player("blue player", "blue")
        self.current_turn = StringVar()
        self.set_red_turn()

    def start(self):
        # place window on computer screen, listen for events
        self.WINDOW.mainloop()

    def record_game(self):
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        with open('game_scores.txt', 'a') as file:
            file.write(f'{dt_string}\n')
            file.write(f'Gametype: {self.gametype}\n')
            file.write(f'\tRED # of wins: {self.red_player.get_wins()}\n')
            file.write(f'\tBLUE # of wins: {self.blue_player.get_wins()}\n')
            if self.gametype == self.GENERAL_GAME:
                file.write(f'\tRED SOS count: {self.red_player.get_sos()}\n')
                file.write(f'\tBLUE SOS count: {self.blue_player.get_sos()}\n')
            file.write('\n')

    def restart(self):
        self.reset_board()
        self.record_game()
        self.set_red_turn()
        self.red_player.reset_sos()
        self.blue_player.reset_sos()

    def create_GUI_gameboard(self):
        self.WINDOW.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.WINDOW.title(self.WINDOW_TITLE)

        for r in range(self.row_count):
            for c in range(self.col_count):
                tile = self.board[r][c] = Button(
                    self.WINDOW, bg="white", text=' ', height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, command=lambda row1=r, col1=c: self.make_move(row1, col1))
                tile.grid(row=r, column=c, padx=2, pady=2)

        # simple and general game buttons
        simple_game_button = Radiobutton(self.WINDOW, text='Simple Game', variable=self.gametype,
                                         value=self.SIMPLE_GAME, command=lambda: self.start_simple_game())
        simple_game_button.grid(row=0, column=self.col_count+1)
        general_game_button = Radiobutton(self.WINDOW, text='General Game', variable=self.gametype,
                                          value=self.GENERAL_GAME, command=lambda: self.start_general_game())
        general_game_button.grid(row=0, column=self.col_count+2)

        # restart game button
        restart_game_button = Button(
            self.WINDOW, text='Restart Game', command=lambda: self.restart())
        restart_game_button.grid(row=7, column=self.col_count+3)

        # player labels
        red_player_label = Label(self.WINDOW, text='RED PLAYER')
        red_player_label.grid(row=2, column=self.col_count+1)
        blue_player_label = Label(self.WINDOW, text='BLUE PLAYER')
        blue_player_label.grid(row=2, column=self.col_count+2, padx=100)

        # player S/O radio buttons
        red_player_S_button = Radiobutton(
            self.WINDOW, text='S', variable=self.red_player.option, value='S')
        red_player_S_button.grid(row=3, column=self.col_count+1)
        red_player_O_button = Radiobutton(
            self.WINDOW, text='O', variable=self.red_player.option, value='O')
        red_player_O_button.grid(row=4, column=self.col_count+1)
        blue_player_S_button = Radiobutton(
            self.WINDOW, text='S', variable=self.blue_player.option, value='S')
        blue_player_S_button.grid(row=3, column=self.col_count+2)
        blue_player_O_button = Radiobutton(
            self.WINDOW, text='O', variable=self.blue_player.option, value='O')
        blue_player_O_button.grid(row=4, column=self.col_count+2)

        # output of current turn label
        current_turn_label = Label(self.WINDOW, textvariable=self.current_turn)
        current_turn_label.grid(row=6, column=self.col_count+1)

    def start_simple_game(self):
        self.gametype = self.SIMPLE_GAME
        #self.restart()
        messagebox.showinfo('Game', self.gametype)

    def start_general_game(self):
        self.gametype = self.GENERAL_GAME
        #self.restart()
        messagebox.showinfo('Game', self.gametype)

    def is_simple_game(self):
        return self.gametype == self.SIMPLE_GAME

    def is_general_game(self):
        return self.gametype == self.GENERAL_GAME

    def show_player_win_message(self, winning_player):
        if self.is_simple_game():
            messagebox.showinfo('WINNER', f'{winning_player.name} wins')
        elif self.is_general_game():
            messagebox.showinfo(
                'WINNER', f'red SOS count: {self.red_player.get_sos()}\nblue SOS count: {self.blue_player.get_sos()}\n{winning_player.name} wins')

    def show_draw_message(self):
        messagebox.showinfo('DRAW', 'this game is a draw :)')

    def make_move(self, row, col):
        # print('row: ', row, ' col: ', col)
        tile = self.get_cell_button(row, col)

        if self.gametype == ' ':
            messagebox.showerror('choose gamemode', 'please choose a gamemode')

        elif tile['text'] == 'S' or tile['text'] == 'O':
            messagebox.showerror(
                'tile occupied', 'cannot make a move here - choose another tile')

        elif (self.get_current_turn() == self.RED_TURN):
            tile['text'] = self.red_player.option.get()
            color = self.red_player.color

            if self.is_simple_game():
                simple_game_status = self.check_simple_game_status(
                    row, col, color)
                if simple_game_status == 'win':
                    self.show_player_win_message(self.red_player)
                    self.red_player.add_win()
                    self.restart()
                elif simple_game_status == 'draw':
                    self.show_draw_message()
                    self.restart()
                else:
                    self.set_blue_turn()

            elif self.is_general_game():
                gen_game_status = self.check_gen_game_status(
                    row, col, color)
                if gen_game_status == 'win':
                    self.red_player.add_sos()
                elif gen_game_status == 'full_board':
                    if self.red_player.get_sos() > self.blue_player.get_sos():
                        self.show_player_win_message(self.red_player)
                        self.red_player.add_win()
                        self.restart()
                    elif self.blue_player.get_sos() > self.red_player.get_sos():
                        self.show_player_win_message(self.blue_player)
                        self.blue_player.add_win()
                        self.restart()
                    else:
                        self.show_draw_message()
                        self.restart()
                else:
                    self.set_blue_turn()

        elif (self.get_current_turn() == self.BLUE_TURN):
            tile['text'] = self.blue_player.option.get()
            color = self.blue_player.color

            if self.is_simple_game():
                simple_game_status = self.check_simple_game_status(
                    row, col, color)
                if simple_game_status == 'win':
                    self.show_player_win_message(self.blue_player)
                    self.blue_player.add_win()
                    self.restart()
                elif simple_game_status == 'draw':
                    self.show_draw_message()
                    self.restart()
                else:
                    self.set_red_turn()

            if self.is_general_game():
                gen_game_status = self.check_gen_game_status(
                    row, col, color)
                if gen_game_status == 'win':
                    self.blue_player.add_sos()
                elif gen_game_status == 'full_board':
                    if self.red_player.get_sos() > self.blue_player.get_sos():
                        self.show_player_win_message(self.red_player)
                        self.red_player.add_win()
                        self.restart()
                    elif self.blue_player.get_sos() > self.red_player.get_sos():
                        self.show_player_win_message(self.blue_player)
                        self.blue_player.add_win()
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


class START_GAME():

    def __init__(self):
        self.BOARD_SIZE_WINDOW = Tk()
        self.BOARD_SIZE_WINDOW.geometry("500x500")
        self.BOARD_SIZE_WINDOW.title("Select Board Size")
        self.label = Label(self.BOARD_SIZE_WINDOW, text="Enter a board size (must be 3 or higher)")
        self.label.pack()
        self.enter_board_size = Entry(self.BOARD_SIZE_WINDOW)
        self.enter_board_size.pack()
        self.start_button = Button(self.BOARD_SIZE_WINDOW, height=3, width=10, text="start game", command=lambda:self.start_game())
        self.start_button.pack()
        self.BOARD_SIZE_WINDOW.mainloop()

    def start_game(self):
        board_size = self.enter_board_size.get()
        board_size = int(board_size)

        if board_size <= 2:
            messagebox.showerror('invalid board size', 'enter a valid board size please (number greater than 2)')
        else:
            self.BOARD_SIZE_WINDOW.destroy()
            game = SOS_GAME_GUI(board_size)
            game.create_GUI_gameboard()
            game.start()


if __name__ == '__main__':
    game = START_GAME()