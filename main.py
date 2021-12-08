from tkinter import *
from tkinter import messagebox
from datetime import datetime
import random
import constant
import json


class Player():
    def __init__(self, name, color):
        self.name = StringVar()
        self.type = constant.HUMAN
        self.color = color
        self.num_sos = 0
        self.option = StringVar()
        self.name.set(name)
        self.set_option('S')

    def get_name(self):
        return self.name.get()

    def set_option(self, option):
        self.option.set(option)

    def get_option(self):
        return self.option.get()

    def add_sos(self):
        self.num_sos += 1

    def reset_sos(self):
        self.num_sos = 0
    
    def get_sos(self):
        return self.num_sos

    def make_move(self, gameboard, row, col):
        if gameboard.get_tile_symbol(row, col) != constant.EMPTY:
            messagebox.showerror(
                'tile occupied', 'cannot make a move here - choose another tile')
            return constant.BAD_MOVE
        else:
            gameboard.set_tile_symbol(row, col, self.get_option())
            return constant.GOOD_MOVE


class Computer(Player):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = constant.COMPUTER

    def pick_rand_row_col(self, gameboard):
        row_rand = random.randrange(0, gameboard.get_board_size())
        col_rand = random.randrange(0, gameboard.get_board_size())
        return row_rand, col_rand

    def pick_rand_option(self):
        option = random.choice(['S', 'O'])
        self.set_option(option)
        return option

    def select_row_col(self, gameboard):
        if gameboard.check_if_full_board():
            return constant.FULL_BOARD, constant.FULL_BOARD
        else:
            options = ['S', 'O']
            for option in options:
                self.set_option(option)
                for row in range(gameboard.board_size):
                    for col in range(gameboard.board_size):
                        if gameboard.get_tile_symbol(row, col) != constant.EMPTY:
                            continue
                        else:
                            if option == 'S':
                                if gameboard.right_move_check(row, col, 'white') or gameboard.left_move_check(row, col, 'white'):
                                    return row, col
                            elif option == 'O':
                                if gameboard.middle_move_check(row, col, 'white'):
                                    return row, col

            option = self.pick_rand_option()
            while(gameboard.get_tile_symbol(row, col) != constant.EMPTY):
                row, col = self.pick_rand_row_col(gameboard)

            return row, col

    def make_move(self, gameboard, row, col):
        gameboard.set_tile_symbol(row, col, self.get_option())
        return constant.GOOD_MOVE
        

class SimpleGame():
    def __init__(self):
        self.type = constant.SIMPLE_GAME
        self.to_record = False
        self.red_player = Player("red player", "red")
        self.blue_player = Player("blue player", "blue")
        self.red_player_type = StringVar()
        self.blue_player_type = StringVar()
        self.red_player_type.set(constant.HUMAN)
        self.blue_player_type.set(constant.HUMAN)
        self.current_turn = StringVar()
        self.current_player = self.red_player
        self.red_wins = 0
        self.blue_wins = 0
    
    def set_to_record(self):
        if self.to_record:
            self.to_record = False
        elif not self.to_record:
            self.to_record = True

    def record_game(self, winning_player, gameboard):
        board_size = gameboard.get_board_size()
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

        with open('recorded_games.txt', 'a') as file:
            if winning_player == constant.DRAW:
                data_dict = {'date_time': dt_string, 'gametype': constant.SIMPLE_GAME, 'board_size': board_size, 'winning_player': constant.DRAW}
                file.write(json.dumps(data_dict))
                file.write('\n')
            else:
                winning_player_name = winning_player.get_name()
                data_dict = {'date_time': dt_string, 'gametype': constant.SIMPLE_GAME, 'board_size': board_size, 'winning_player': winning_player_name}
                file.write(json.dumps(data_dict))
                file.write('\n')

    def add_win(self, winning_player):
        if winning_player == self.red_player:
            self.red_wins += 1
        elif winning_player == self.blue_player:
            self.blue_wins += 1

    def reset(self, gameboard, winning_player):
        if self.to_record and winning_player != constant.NULL:
            self.record_game(winning_player, gameboard)
        gameboard.reset_board()
        self.check_both_player_computers()
        self.red_player.reset_sos()
        self.blue_player.reset_sos()
        self.set_red_turn(gameboard)

    def set_red_human(self):
        self.red_player_type.set(constant.HUMAN)
        self.red_player = Player("red player", "red")

    def set_blue_human(self):
        self.blue_player_type.set(constant.HUMAN)
        self.blue_player = Player("blue player", "blue")

    def set_red_computer(self, gameboard):
        self.red_player_type.set(constant.COMPUTER)
        if self.current_player.get_name() == self.red_player.get_name():
            self.red_player = Computer("red player", "red")
            self.set_red_turn(gameboard)
        else:
            self.red_player = Computer("red player", "red")

    def set_blue_computer(self, gameboard):
        self.blue_player_type.set(constant.COMPUTER)
        if self.current_player.get_name() == self.blue_player.get_name():
            self.blue_player = Computer("blue player", "blue")
            self.set_blue_turn(gameboard)
        else:
            self.blue_player = Computer("blue player", "blue")
            
    def set_red_turn(self, gameboard=constant.NULL):
        self.current_turn.set('Current Turn: red player')
        self.current_player = self.red_player
        if self.current_player.type == constant.COMPUTER:
            row, col = self.current_player.select_row_col(gameboard)
            self.check_game_status(gameboard, row, col)

    def set_blue_turn(self, gameboard=constant.NULL):
        self.current_turn.set('Current Turn: blue player')
        self.current_player = self.blue_player
        if self.current_player.type == constant.COMPUTER:
            row, col = self.current_player.select_row_col(gameboard)
            self.check_game_status(gameboard, row, col)

    def switch_turn(self, gameboard):
        if self.current_player == self.red_player:
            self.set_blue_turn(gameboard)

        elif self.current_player == self.blue_player:
            self.set_red_turn(gameboard)

    def check_game_status(self, gameboard, row, col):
        if self.current_player.make_move(gameboard, row, col) == constant.GOOD_MOVE:
            board_game_status = gameboard.check_game_status(row, col, self.current_player.color)
            if board_game_status == constant.SCORE:
                winning_player = self.current_player
                self.show_player_win_message(winning_player)
                self.add_win(winning_player)
                self.reset(gameboard, winning_player)
                return constant.NULL
            
            if gameboard.check_if_full_board():
                winning_player = constant.DRAW
                self.show_draw_message()
                self.reset(gameboard, winning_player)
                return constant.NULL
            else:
                self.switch_turn(gameboard)
                return constant.NULL

    def check_both_player_computers(self):
        if self.red_player.type == constant.COMPUTER and self.blue_player.type == constant.COMPUTER:
            messagebox.showinfo('Players reset to Human', 'Both players reset to Human')
            self.set_red_human()
            self.set_blue_human()

    def show_player_win_message(self, winning_player):
        messagebox.showinfo('WINNER', f'{winning_player.get_name()} wins')

    def show_draw_message(self):
        messagebox.showinfo('DRAW', 'this game is a draw :)')
        

class GeneralGame(SimpleGame):
    def __init__(self):
        super().__init__()
        self.type = constant.GENERAL_GAME
        
    def record_game(self, winning_player, gameboard):
        board_size = gameboard.get_board_size()
        red_sos_count = self.red_player.get_sos()
        blue_sos_count = self.blue_player.get_sos()
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

        with open('recorded_games.txt', 'a') as file:
            if winning_player == constant.DRAW:
                data_dict = {'date_time': dt_string, 'gametype': constant.GENERAL_GAME, 'board_size': board_size, 'red_sos_count': red_sos_count, 'blue_sos_count': blue_sos_count, 'winning_player': constant.DRAW}
                file.write(json.dumps(data_dict))
                file.write('\n')
            else:
                winning_player_name = winning_player.get_name()
                data_dict = {'date_time': dt_string, 'gametype': constant.GENERAL_GAME, 'board_size': board_size, 'red_sos_count': red_sos_count, 'blue_sos_count': blue_sos_count, 'winning_player': winning_player_name}
                file.write(json.dumps(data_dict))
                file.write('\n')
    
    def get_winner(self):
        if self.red_player.get_sos() > self.blue_player.get_sos():
            return self.red_player
        elif self.blue_player.get_sos() > self.red_player.get_sos():
            return self.blue_player
        else:
            return constant.DRAW

    def check_game_status(self, gameboard, row, col):
        if row == constant.FULL_BOARD:
            winning_player = self.get_winner()
            if winning_player == constant.DRAW:
                self.show_draw_message()
                self.reset(gameboard, winning_player)
                return constant.NULL
            else:
                self.add_win(winning_player)
                self.show_player_win_message(winning_player)
                self.reset(gameboard, winning_player)
                return constant.NULL
                
        if self.current_player.make_move(gameboard, row, col) == constant.GOOD_MOVE:
            board_game_status = gameboard.check_game_status(row, col, self.current_player.color)
            if board_game_status == constant.SCORE:
                self.current_player.add_sos()
                self.check_current_player_computer(gameboard)
            else:
                self.switch_turn(gameboard)
            
            if gameboard.check_if_full_board():
                winning_player = self.get_winner()
                if winning_player == constant.DRAW:
                    self.show_draw_message()
                    self.reset(gameboard, winning_player)
                else:
                    self.add_win(winning_player)
                    self.show_player_win_message(winning_player)
                    self.reset(gameboard, winning_player)

        return constant.NULL

    def check_current_player_computer(self, gameboard):
        if self.current_player.type == constant.COMPUTER:
                row, col = self.current_player.select_row_col(gameboard)
                self.check_game_status(gameboard, row, col)

    def show_player_win_message(self, winning_player):
        messagebox.showinfo(
            'WINNER', f'red SOS count: {self.red_player.get_sos()}\nblue SOS count: {self.blue_player.get_sos()}\n\n{winning_player.get_name()} wins')

   
class SosGameBoard():
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = []
        self.create_board_skeleton()

    def create_board_skeleton(self):
        for row in range(self.board_size):
            self.board.append([])
            for col in range(self.board_size):
                self.board[row].append(0)  # append empty cell

    def reset_board(self):
        for r in range(self.board_size):
            for c in range(self.board_size):
                tile = self.board[r][c]
                tile['text'] = ' '
                tile['bg'] = 'white'

    def get_board_size(self):
        return self.board_size

    def get_tile_symbol(self, row, col):
        return self.board[row][col]['text']

    def set_tile_symbol(self, row, col, symbol):
        self.board[row][col]['text'] = symbol

    def check_if_full_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
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
                if player_color != 'white':
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
                if player_color != 'white':
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
                if player_color != 'white':
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
                if player_color != 'white':
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
                if player_color != 'white':
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
                if player_color != 'white':
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
                if player_color != 'white':
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
                if player_color != 'white':
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
                if player_color != 'white':
                    self.board[move_row][move_col+2]['bg'] = player_color
                    self.board[move_row][move_col+1]['bg'] = player_color
                    move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if self.board[move_row+2][move_col]['text'] == 'S' and self.board[move_row+1][move_col]['text'] == 'O':
                # up and down
                if player_color != 'white':
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
                if player_color != 'white':
                    self.board[move_row-2][move_col+2]['bg'] = player_color
                    self.board[move_row-1][move_col+1]['bg'] = player_color
                    move_tile['bg'] = player_color
                return True
        except IndexError:
            pass
        try:
            if self.board[move_row+2][move_col+2]['text'] == 'S' and self.board[move_row+1][move_col+1]['text'] == 'O':
                # up left to down right diag
                if player_color != 'white':
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
                return constant.SCORE
        elif symbol == 'S':
            if self.right_move_check(move_row, move_col, player_color) or self.left_move_check(move_row, move_col, player_color):
                return constant.SCORE


class SosGameGUI():
    def __init__(self):
        self.WINDOW = Tk()
        self.infoWindow = constant.EMPTY
        self.BUTTON_HEIGHT = 3
        self.BUTTON_WIDTH = 6
        self.BOARD_SIZE = constant.EMPTY
        self.START_WINDOW_WIDTH = 300
        self.START_WINDOW_HEIGHT = 300
        self.WINDOW_TITLE = 'Morgan\'s SOS Game'
        self.WINDOW.geometry(f"{self.START_WINDOW_WIDTH}x{self.START_WINDOW_HEIGHT}")
        self.WINDOW.title(self.WINDOW_TITLE)
        self.first_start_button = Button(self.WINDOW, height=3, width=10, text='press to start', command=lambda:self.get_game_info())
        self.first_start_button.pack()
        self.gameboard = constant.EMPTY
        self.game = SimpleGame()
        self.gametype = StringVar()
        self.board_size_entry = constant.EMPTY

    def start(self):
        # place window on computer screen, listen for events
        self.WINDOW.mainloop()

    def exit_window(self):
        self.WINDOW.quit()
        self.WINDOW.destroy()

    def set_simple_game(self):
        self.game = SimpleGame()

    def set_general_game(self):
        self.game = GeneralGame()      

    def get_game_info(self):
        self.first_start_button.pack_forget()
        self.infoWindow = Toplevel(self.WINDOW)
        self.infoWindow.title("Enter board size and game type")
        self.infoWindow.geometry(f"{self.START_WINDOW_WIDTH}x{self.START_WINDOW_HEIGHT}")
        board_size_label = Label(self.infoWindow, text="Enter a board size (must be >= 3 and <= 15)")
        board_size_label.pack()
        self.board_size_entry = Entry(self.infoWindow)
        self.board_size_entry.pack()
        simple_game_button = Radiobutton(self.infoWindow, text='Simple Game', variable=self.gametype, value=constant.SIMPLE_GAME, command=lambda: self.set_simple_game())
        simple_game_button.pack()
        general_game_button = Radiobutton(self.infoWindow, text='General Game', variable=self.gametype, value=constant.GENERAL_GAME, command=lambda: self.set_general_game())
        general_game_button.pack()
        start_button = Button(self.infoWindow, height=3, width=10, text='start game', command=lambda:self.check_info())
        start_button.pack()
        replay_button = Button(self.infoWindow, height=3, width=15, text='replay last game', command=lambda:self.replay_game())
        replay_button.pack()
        simple_game_button.select()

    def check_info(self):
        try:
            board_size = self.board_size_entry.get()
            self.BOARD_SIZE = int(board_size)
        except ValueError:
            messagebox.showerror(
                'invalid board size', 'enter a valid board size please (number >= 3 and <= 15)')
            return None

        if self.BOARD_SIZE < 3 or self.BOARD_SIZE > 15:
            messagebox.showerror(
                'invalid board size', 'enter a valid board size please (number >= 3 and <= 15)')
            return None
        else:
            self.create_GUI_gameboard()

    def replay_game(self):
        try:
            with open('recorded_games.txt', 'r') as file:
                recorded_list = file.readlines()
                last_game = json.loads(recorded_list[-1])
                self.BOARD_SIZE = last_game['board_size']

                if last_game['gametype'] == constant.SIMPLE_GAME:
                    self.set_simple_game()
                    self.gametype.set(constant.SIMPLE_GAME)
                elif last_game['gametype'] == constant.GENERAL_GAME:
                    self.set_general_game()
                    self.gametype.set(constant.GENERAL_GAME)

                self.create_GUI_gameboard()

        except FileNotFoundError:
            messagebox.showerror(
                'cannot find recorded games file', 'the recorded games file cannot be found - start a new game instead')
            return constant.NULL

    def create_GUI_gameboard(self):
        self.infoWindow.destroy()
        self.WINDOW.title(self.gametype.get())
        self.gameboard = SosGameBoard(self.BOARD_SIZE)
        self.GAME_WINDOW_WIDTH = (self.BUTTON_WIDTH * self.BOARD_SIZE) * 30
        self.GAME_WINDOW_HEIGHT = (self.BUTTON_HEIGHT * self.BOARD_SIZE) * 30
        self.WINDOW.geometry(f"{self.GAME_WINDOW_WIDTH}x{self.GAME_WINDOW_HEIGHT}")

        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                tile = self.gameboard.board[r][c] = Button(
                    self.WINDOW, bg="white", text=constant.EMPTY, height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, command=lambda row1=r, col1=c: self.game.check_game_status(self.gameboard, row1, col1))
                tile.grid(row=r, column=c, padx=2, pady=2)

        # output of current turn label
        current_turn_label = Label(self.WINDOW, textvariable=self.game.current_turn)
        current_turn_label.grid(row=0, column=self.BOARD_SIZE+1)

        # restart game button
        restart_game_button = Button(
            self.WINDOW, text='Restart Game', command=lambda: self.game.reset(self.gameboard, constant.NULL))
        restart_game_button.grid(row=4, column=self.BOARD_SIZE+3)

        # to record option
        to_record_checkbox = Checkbutton(self.WINDOW, text='Record game', variable=self.game.to_record, command=lambda: self.game.set_to_record())
        to_record_checkbox.grid(row=4, column=self.BOARD_SIZE+1)

        # player label frames
        red_label_frame = Frame(self.WINDOW)
        blue_label_frame = Frame(self.WINDOW)

        # player labels
        red_label = Label(red_label_frame, text='RED PLAYER')
        blue_label = Label(blue_label_frame, text='BLUE PLAYER')

        # human player radio buttons
        red_human_button = Radiobutton(red_label_frame, text='Human', variable=self.game.red_player_type, value=constant.HUMAN, command=lambda: self.game.set_red_human())
        blue_human_button = Radiobutton(blue_label_frame, text='Human', variable=self.game.blue_player_type, value=constant.HUMAN, command=lambda: self.game.set_blue_human())

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
            red_button_frame, text='S', variable=self.game.red_player.option, value='S', command=lambda: self.game.red_player.set_option('S'))
        red_O_button = Radiobutton(
            red_button_frame, text='O', variable=self.game.red_player.option, value='O', command=lambda: self.game.red_player.set_option('O'))

        blue_S_button = Radiobutton(
            blue_button_frame, text='S', variable=self.game.blue_player.option, value='S', command=lambda: self.game.blue_player.set_option('S'))
        blue_O_button = Radiobutton(
            blue_button_frame, text='O', variable=self.game.blue_player.option, value='O', command=lambda: self.game.blue_player.set_option('O'))

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
        red_computer_button = Radiobutton(red_computer_frame, text='Computer', variable=self.game.red_player_type, value=constant.COMPUTER, command=lambda: self.game.set_red_computer(self.gameboard))
        blue_computer_button = Radiobutton(blue_computer_frame, text='Computer', variable=self.game.blue_player_type, value=constant.COMPUTER, command=lambda: self.game.set_blue_computer(self.gameboard))

        red_computer_frame.grid(row=3, column=self.BOARD_SIZE+1)
        blue_computer_frame.grid(row=3, column=self.BOARD_SIZE+2)

        red_computer_button.pack(side="top")
        blue_computer_button.pack(side="top")

        red_human_button.select()
        blue_human_button.select()

        red_S_button.select()
        blue_S_button.select()


if __name__ == '__main__':
    gameGUI = SosGameGUI()
    gameGUI.start()