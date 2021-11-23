from tkinter import *
from tkinter import messagebox
from datetime import datetime


class Player():

    def __init__(self, name, color):
        self.name = name
        self.type = 'Human'
        self.color = color
        self.num_wins = 0
        self.num_sos = 0
        self.option = StringVar()
        self.option.set(' ')

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

    def make_move(self, gameboard, row, col):
        print('human move')


class Computer(Player):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = 'Computer'

    def make_move(self, gameboard, row, col):
        print('computer move')

    
    
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

    def get_tile(self, row, col):
        return self.board[row][col]

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
            if (move_col - 1) < 0:
                pass
            elif self.board[move_row][move_col-1]['text'] == 'S' and self.board[move_row][move_col+1]['text'] == 'S':
                # left to right
                self.board[move_row][move_col-1]['bg'] = player_color
                self.board[move_row][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0:
                pass
            elif self.board[move_row-1][move_col]['text'] == 'S' and self.board[move_row+1][move_col]['text'] == 'S':
                # up and down
                self.board[move_row-1][move_col]['bg'] = player_color
                self.board[move_row+1][move_col]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_col - 1) < 0:
                pass
            elif self.board[move_row+1][move_col-1]['text'] == 'S' and self.board[move_row-1][move_col+1]['text'] == 'S':
                # down left to up right diag
                self.board[move_row+1][move_col-1]['bg'] = player_color
                self.board[move_row-1][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_col - 1) < 0:
                pass
            elif self.board[move_row-1][move_col-1]['text'] == 'S' and self.board[move_row+1][move_col+1]['text'] == 'S':
                # up left to down right diag
                self.board[move_row-1][move_col-1]['bg'] = player_color
                self.board[move_row+1][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass

        return False

    def right_move_check(self, move_row, move_col, player_color):
        '''selected move tile is far right'''
        move_tile = self.board[move_row][move_col]
        try:
            if (move_col - 1) < 0 or (move_col - 2) < 0:
                pass
            elif self.board[move_row][move_col-2]['text'] == 'S' and self.board[move_row][move_col-1]['text'] == 'O':
                # left to right
                self.board[move_row][move_col-2]['bg'] = player_color
                self.board[move_row][move_col-1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_row - 2) < 0:
                pass
            elif self.board[move_row-2][move_col]['text'] == 'S' and self.board[move_row-1][move_col]['text'] == 'O':
                # up and down
                self.board[move_row-2][move_col]['bg'] = player_color
                self.board[move_row-1][move_col]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if (move_col - 1) < 0 or (move_col - 2) < 0:
                pass
            elif self.board[move_row+2][move_col-2]['text'] == 'S' and self.board[move_row+1][move_col-1]['text'] == 'O':
                # down left to up right diag
                self.board[move_row+2][move_col-2]['bg'] = player_color
                self.board[move_row+1][move_col-1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_row - 2) < 0 or (move_col - 1) < 0 or (move_col - 2) < 0:
                pass
            elif self.board[move_row-2][move_col-2]['text'] == 'S' and self.board[move_row-1][move_col-1]['text'] == 'O':
                # up left to down right diag
                self.board[move_row-2][move_col-2]['bg'] = player_color
                self.board[move_row-1][move_col-1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass

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
            pass
        try:
            if self.board[move_row+2][move_col]['text'] == 'S' and self.board[move_row+1][move_col]['text'] == 'O':
                # up and down
                self.board[move_row+2][move_col]['bg'] = player_color
                self.board[move_row+1][move_col]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_row - 2) < 0:
                pass
            elif self.board[move_row-2][move_col+2]['text'] == 'S' and self.board[move_row-1][move_col+1]['text'] == 'O':
                # down left to up right diag
                self.board[move_row-2][move_col+2]['bg'] = player_color
                self.board[move_row-1][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if self.board[move_row+2][move_col+2]['text'] == 'S' and self.board[move_row+1][move_col+1]['text'] == 'O':
                # up left to down right diag
                self.board[move_row+2][move_col+2]['bg'] = player_color
                self.board[move_row+1][move_col+1]['bg'] = player_color
                move_tile['bg'] = player_color
                return True
        except IndexError:
            pass

        return False

    def check_game_status(self, move_row, move_col, player_color):
        symbol = self.board[move_row][move_col]['text']

        if symbol == 'O':
            if self.middle_move_check(move_row, move_col, player_color):
                return 'score'
        elif symbol == 'S':
            if self.right_move_check(move_row, move_col, player_color) or self.left_move_check(move_row, move_col, player_color):
                return 'score'


class SIMPLE_GAME():
    def __init__(self):
        self.type = 'Simple Game'


class GENERAL_GAME():
    def __init__(self):
        self.type = 'General Game'

class SOS_GAME_GUI():

    def __init__(self, board_size, to_record):
        self.gameboard = SOS_GAME_BOARD(board_size)
        self.BOARD_SIZE = board_size
        # define window and widget variables
        self.WINDOW = Tk()
        self.WINDOW_WIDTH = 1500
        self.WINDOW_HEIGHT = 900
        self.WINDOW_TITLE = 'Morgan\'s SOS Game'
        self.BUTTON_HEIGHT = 3
        self.BUTTON_WIDTH = 6
        self.SIMPLE_GAME = 'Simple Game'
        self.GENERAL_GAME = 'General Game'
        self.COMPUTER = 'Computer'
        self.HUMAN = 'Human'
        self.RED_TURN = 'Red\'s Turn'
        self.BLUE_TURN = 'Blue\'s Turn'
        self.game = ' '
        self.red_player_type = StringVar()
        self.blue_player_type = StringVar()
        self.gametype = StringVar()
        self.red_player = Player("red player", "red")
        self.blue_player = Player("blue player", "blue")
        self.current_turn = StringVar()
        self.to_record = to_record
        self.red_player_type.set(' ')
        self.blue_player_type.set(' ')
        self.gametype.set(' ')
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
            if self.is_general_game():
                file.write(f'\tRED SOS count: {self.red_player.get_sos()}\n')
                file.write(f'\tBLUE SOS count: {self.blue_player.get_sos()}\n')
            file.write('\n')

    def restart(self):
        if self.to_record:
            self.record_game()
        self.reset_board()
        self.set_red_turn()
        self.red_player.reset_sos()
        self.blue_player.reset_sos()

    def create_GUI_gameboard(self):
        self.WINDOW.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.WINDOW.title(self.WINDOW_TITLE)

        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                tile = self.gameboard.board[r][c] = Button(
                    self.WINDOW, bg="white", text=' ', height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, command=lambda row1=r, col1=c: self.make_move(row1, col1))
                tile.grid(row=r, column=c, padx=2, pady=2)

        # simple and general game buttons
        simple_game_button = Radiobutton(self.WINDOW, text='Simple Game', variable=self.gametype,
                                         value=self.SIMPLE_GAME, command=lambda: self.start_simple_game())
        simple_game_button.grid(row=0, column=self.BOARD_SIZE+1)
        general_game_button = Radiobutton(self.WINDOW, text='General Game', variable=self.gametype,
                                          value=self.GENERAL_GAME, command=lambda: self.start_general_game())
        general_game_button.grid(row=0, column=self.BOARD_SIZE+2)

        # restart game button
        restart_game_button = Button(
            self.WINDOW, text='Restart Game', command=lambda: self.restart())
        restart_game_button.grid(row=4, column=self.BOARD_SIZE+2)

        # player label frames
        red_label_frame = Frame(self.WINDOW)
        blue_label_frame = Frame(self.WINDOW)

        # player labels
        red_label = Label(red_label_frame, text='RED PLAYER')
        blue_label = Label(blue_label_frame, text='BLUE PLAYER')

        # human player radio buttons
        red_human_button = Radiobutton(red_label_frame, text='Human', variable=self.red_player_type, value=self.HUMAN, command=lambda: self.set_red_human())
        blue_human_button = Radiobutton(blue_label_frame, text='Human', variable=self.blue_player_type, value=self.HUMAN, command=lambda: self.set_blue_human())

        red_label_frame.grid(row=1, column=self.BOARD_SIZE+1)
        blue_label_frame.grid(row=1, column=self.BOARD_SIZE+2)

        red_label.pack(side="top")
        blue_label.pack(side="top")
        red_human_button.pack(side="top")
        blue_human_button.pack(side="top")

        # player frames
        red_button_frame = Frame(self.WINDOW)
        blue_button_frame = Frame(self.WINDOW)

        # player S/O radio buttons
        red_S_button = Radiobutton(
            red_button_frame, text='S', variable=self.red_player.option, value='S')
        red_O_button = Radiobutton(
            red_button_frame, text='O', variable=self.red_player.option, value='O')

        blue_S_button = Radiobutton(
            blue_button_frame, text='S', variable=self.blue_player.option, value='S')
        blue_O_button = Radiobutton(
            blue_button_frame, text='O', variable=self.blue_player.option, value='O')

        red_button_frame.grid(row=2, column=self.BOARD_SIZE+1)
        blue_button_frame.grid(row=2, column=self.BOARD_SIZE+2)

        red_S_button.pack(side="top")
        red_O_button.pack(side="top")

        blue_S_button.pack(side="top")
        blue_O_button.pack(side="top")

        # computer button frames
        red_computer_frame = Frame(self.WINDOW)
        blue_computer_frame = Frame(self.WINDOW)

        # computer radio buttons
        red_computer_button = Radiobutton(red_computer_frame, text='Computer', variable=self.red_player_type, value=self.COMPUTER, command=lambda: self.set_red_computer())
        blue_computer_button = Radiobutton(blue_computer_frame, text='Computer', variable=self.blue_player_type, value=self.COMPUTER, command=lambda: self.set_blue_computer())

        red_computer_frame.grid(row=3, column=self.BOARD_SIZE+1)
        blue_computer_frame.grid(row=3, column=self.BOARD_SIZE+2)

        red_computer_button.pack(side="top")
        blue_computer_button.pack(side="top")

        # output of current turn label
        current_turn_label = Label(self.WINDOW, textvariable=self.current_turn)
        current_turn_label.grid(row=4, column=self.BOARD_SIZE+1)

    def start_simple_game(self):
        self.game = SIMPLE_GAME()
        messagebox.showinfo('Game', self.game.type)

    def start_general_game(self):
        self.game = GENERAL_GAME()
        messagebox.showinfo('Game', self.game.type)

    def is_simple_game(self):
        return self.game.type == self.SIMPLE_GAME

    def is_general_game(self):
        return self.game.type == self.GENERAL_GAME

    def show_player_win_message(self, winning_player):
        if self.is_simple_game():
            messagebox.showinfo('WINNER', f'{winning_player.name} wins')
        elif self.is_general_game():
            messagebox.showinfo(
                'WINNER', f'red SOS count: {self.red_player.get_sos()}\nblue SOS count: {self.blue_player.get_sos()}\n{winning_player.name} wins')

    def show_draw_message(self):
        messagebox.showinfo('DRAW', 'this game is a draw :)')

    def set_red_human(self):
        self.red_player = Player("red player", "red")

    def set_blue_human(self):
        self.blue_player = Player("blue player", "blue")

    def set_red_computer(self):
        self.red_player = Computer("red player", "red")

    def set_blue_computer(self):
        self.blue_player = Computer("blue player", "blue")

    def get_current_turn(self):
        return self.current_turn.get()

    def set_red_turn(self):
        self.current_turn.set(self.RED_TURN)

    def set_blue_turn(self):
        self.current_turn.set(self.BLUE_TURN)

    def make_move(self, row, col):
        tile = self.gameboard.get_tile(row, col)

        if self.game == ' ':
            messagebox.showerror('choose gamemode', 'please choose a gamemode')

        elif tile['text'] == 'S' or tile['text'] == 'O':
            messagebox.showerror(
                'tile occupied', 'cannot make a move here - choose another tile')

        elif (self.red_player.option.get() == ' ') or (self.blue_player.option.get() == ' '):
            messagebox.showerror('choose option', 'player must choose S or O before making a move')
                
        elif (self.get_current_turn() == self.RED_TURN):
            self.red_player.make_move(self.gameboard, row, col)

        elif (self.get_current_turn() == self.BLUE_TURN):
            self.red_player.make_move(self.gameboard, row, col)



class START_GAME_MENU():

    def __init__(self):
        self.BOARD_SIZE_WINDOW = Tk()
        self.BOARD_SIZE_WINDOW.geometry("500x500")
        self.BOARD_SIZE_WINDOW.title("Select Board Size")
        self.to_record = BooleanVar()
        self.label = Label(self.BOARD_SIZE_WINDOW, text="Enter a board size (must be >= 3 and <= 15)")
        self.label.pack()
        self.enter_board_size = Entry(self.BOARD_SIZE_WINDOW)
        self.enter_board_size.pack()
        self.to_record_checkbox = Checkbutton(self.BOARD_SIZE_WINDOW, text='Record games', variable=self.to_record, pady=20)
        self.to_record_checkbox.pack()
        self.start_button = Button(self.BOARD_SIZE_WINDOW, height=3, width=10, text="start game", command=lambda:self.start_game())
        self.start_button.pack()

    def display_start_menu(self):
        self.BOARD_SIZE_WINDOW.mainloop()

    def start_game(self):
        try:
            board_size = self.enter_board_size.get()
            board_size = int(board_size)
        except ValueError:
            messagebox.showerror(
                'invalid board size', 'enter a valid board size please (number >= 3 and <= 15)')
            return None

        if board_size < 3 or board_size > 15:
            messagebox.showerror(
                'invalid board size', 'enter a valid board size please (number >= 3 and <= 15)')
            return None
        else:
            self.BOARD_SIZE_WINDOW.destroy()
            game = SOS_GAME_GUI(board_size, self.to_record.get())
            game.create_GUI_gameboard()
            game.start()


if __name__ == '__main__':
    start = START_GAME_MENU()
    start.display_start_menu()