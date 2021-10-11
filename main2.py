from tkinter import *
from tkinter import messagebox
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

class Player():
    def __init__(self, player_num):
        self.player_num = player_num
        self.turn = False

    def get_turn(self):
        return self.turn
    
    def set_turn(self, turn_status):
        self.turn = turn_status


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

    def set_cell_value(self, row, col, value):
        self.board[row][col] = value

    def get_cell_value(self, row, col):
        return self.board[row][col]


class SOS_GAME_GUI():
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 500
    WINDOW = Tk()
    WINDOW.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    WINDOW.title("Morgan's SOS Game")
    BUTTON_HEIGHT = 3
    BUTTON_WIDTH = 6
    RED_PLAYER_OPTION =  StringVar()
    BLUE_PLAYER_OPTION = StringVar()
    SIMPLE_GAME = 0
    GENERAL_GAME = 1


    # red_player_label = Label(WINDOW, text='RED PLAYER')
    # red_player_label.grid(row=2, column=9)

    # blue_player_label = Label(WINDOW, text='BLUE PLAYER')
    # blue_player_label.grid(row=2, column=10, padx=200)

    # red_player_S = Radiobutton(WINDOW, text='S', variable= RED_PLAYER_OPTION, value='S').grid(row=3, column=9)
    # red_player_O = Radiobutton(WINDOW, text='O', variable= RED_PLAYER_OPTION, value='O').grid(row=4, column=9)

    # blue_player_S = Radiobutton(WINDOW, text='S', variable= BLUE_PLAYER_OPTION, value='S').grid(row=3, column=10, padx=200)
    # blue_player_O = Radiobutton(WINDOW, text='O', variable= BLUE_PLAYER_OPTION, value='O').grid(row=4, column=10, padx=200)

    
    def __init__(self):
        self.gameboard = SOS_GAME_BOARD()
        self.gametype = self.SIMPLE_GAME

    def start(self):
        self.create_GUI_gameboard()
        self.WINDOW.mainloop() # place window on computer screen, listen for events


    def create_GUI_gameboard(self):
        for r in range(self.gameboard.NUM_ROWS):
            for c in range(self.gameboard.NUM_COLS):
                self.gameboard.board[r][c] = Button(self.WINDOW, bg="SystemButtonFace", height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, command=lambda: self.make_move(r,c))
                self.gameboard.board[r][c].grid(row=r, column=c, padx= 2, pady=2)

        simple_game_button = Radiobutton(self.WINDOW, text='Simple Game', variable=self.gametype, value=self.SIMPLE_GAME, command=lambda: self.start_simple_game()).grid(row=0, column=9)
        general_game_button = Radiobutton(self.WINDOW, text='General Game', variable=self.gametype, value=self.GENERAL_GAME, command=lambda: self.start_general_game()).grid(row=0, column=10)

        red_player_label = Label(self.WINDOW, text='RED PLAYER')
        red_player_label.grid(row=2, column=9)

        blue_player_label = Label(self.WINDOW, text='BLUE PLAYER')
        blue_player_label.grid(row=2, column=10, padx=200)

        red_player_S_button = Radiobutton(self.WINDOW, text='S', variable= self.RED_PLAYER_OPTION, value='S', command=lambda: self.radio_click()).grid(row=3, column=9)
        red_player_O_button = Radiobutton(self.WINDOW, text='O', variable= self.RED_PLAYER_OPTION, value='O', command=lambda: self.radio_click()).grid(row=4, column=9)

        blue_player_S_button = Radiobutton(self.WINDOW, text='S', variable= self.BLUE_PLAYER_OPTION, value='S', command=lambda: self.radio_click()).grid(row=3, column=10, padx=200)
        blue_player_O_button = Radiobutton(self.WINDOW, text='O', variable= self.BLUE_PLAYER_OPTION, value='O', command=lambda: self.radio_click()).grid(row=4, column=10, padx=200)

    def radio_click(self):
        print('Red value: ', self.RED_PLAYER_OPTION.get())
        print('Blue value: ', self.BLUE_PLAYER_OPTION.get())

    def start_simple_game(self):
        messagebox.showinfo('Game', 'Simple Game Started!')

    def start_general_game(self):
        messagebox.showinfo('Game', 'General Game Started!')

    def make_move(self, row, col):
        print('row: ', row, ' col: ', col)
        button_pressed = self.gameboard.board[row][col]
        button_pressed['text'] = 'S'



# MAIN
game = SOS_GAME_GUI()
game.start()