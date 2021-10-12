from tkinter import *
from tkinter import messagebox
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

    def get_cell_value(self, row, col):
        return self.board[row][col]


class SOS_GAME_GUI():
    # define window and widget variables
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 500
    WINDOW = Tk()
    WINDOW_TITLE = 'Morgan\'s SOS Game'
    BUTTON_HEIGHT = 3
    BUTTON_WIDTH = 6
    RED_PLAYER_OPTION =  StringVar()
    BLUE_PLAYER_OPTION = StringVar()
    SIMPLE_GAME = 'Simple Game'
    GENERAL_GAME = 'General Game'
    RED_TURN = 'Red\'s Turn'
    BLUE_TURN = 'Blue\'s Turn'

    def __init__(self):
        self.gameboard = SOS_GAME_BOARD()
        self.gametype = ' '
        self.current_turn = self.RED_TURN
        self.current_turn_string = StringVar()
        self.current_turn_string.set(self.RED_TURN)

    def start(self):
        self.create_GUI_gameboard()
        self.WINDOW.mainloop() # place window on computer screen, listen for events


    def create_GUI_gameboard(self):
        self.WINDOW.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.WINDOW.title(self.WINDOW_TITLE)
        
        for r in range(self.gameboard.NUM_ROWS):
            for c in range(self.gameboard.NUM_COLS):
                tile = self.gameboard.board[r][c] = Button(self.WINDOW, bg="SystemButtonFace", height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, command=lambda row1 = r, col1 = c: self.make_move(row1, col1))
                tile.grid(row=r, column=c, padx= 2, pady=2)

        # simple and general game buttons
        simple_game_button = Radiobutton(self.WINDOW, text='Simple Game', variable=self.gametype, value=self.SIMPLE_GAME, command=lambda: self.start_simple_game())
        simple_game_button.grid(row=0, column=9)
        general_game_button = Radiobutton(self.WINDOW, text='General Game', variable=self.gametype, value=self.GENERAL_GAME, command=lambda: self.start_general_game())
        general_game_button.grid(row=0, column=10)

        # player labels
        red_player_label = Label(self.WINDOW, text='RED PLAYER')
        red_player_label.grid(row=2, column=9)
        blue_player_label = Label(self.WINDOW, text='BLUE PLAYER')
        blue_player_label.grid(row=2, column=10, padx=100)

        # player S/O radio buttons
        red_player_S_button = Radiobutton(self.WINDOW, text='S', variable= self.RED_PLAYER_OPTION, value='S', command=lambda: self.radio_click())
        red_player_S_button.grid(row=3, column=9)
        red_player_O_button = Radiobutton(self.WINDOW, text='O', variable= self.RED_PLAYER_OPTION, value='O', command=lambda: self.radio_click())
        red_player_O_button.grid(row=4, column=9)
        blue_player_S_button = Radiobutton(self.WINDOW, text='S', variable= self.BLUE_PLAYER_OPTION, value='S', command=lambda: self.radio_click())
        blue_player_S_button.grid(row=3, column=10)
        blue_player_O_button = Radiobutton(self.WINDOW, text='O', variable= self.BLUE_PLAYER_OPTION, value='O', command=lambda: self.radio_click())
        blue_player_O_button.grid(row=4, column=10)

        # current_turn_label_description = Label(self.WINDOW, text= 'Current Turn: ')
        # current_turn_label_description.grid(row=6, column=9)
        current_turn_label = Label(self.WINDOW, textvariable=self.current_turn_string)
        current_turn_label.grid(row=6, column=9)

    def radio_click(self):
        print('Red value: ', self.RED_PLAYER_OPTION.get())
        print('Blue value: ', self.BLUE_PLAYER_OPTION.get())

    def start_simple_game(self):
        self.gametype = self.SIMPLE_GAME
        messagebox.showinfo('Game', self.gametype)

    def start_general_game(self):
        self.gametype = self.GENERAL_GAME
        messagebox.showinfo('Game', self.gametype)

    def make_move(self, row, col):
        print('row: ', row, ' col: ', col)
        tile = self.gameboard.get_cell_value(row, col)

        if (self.current_turn == self.RED_TURN) and (self.RED_PLAYER_OPTION.get() == 'S'):
            tile['text'] = 'S'
            self.set_blue_turn()
        elif (self.current_turn == self.RED_TURN) and (self.RED_PLAYER_OPTION.get() == 'O'):
            tile['text'] = 'O'
            self.set_blue_turn()

        elif (self.current_turn == self.BLUE_TURN) and (self.BLUE_PLAYER_OPTION.get() == 'S'):
            tile['text'] = 'S'
            self.set_red_turn()
        elif(self.current_turn == self.BLUE_TURN) and (self.BLUE_PLAYER_OPTION.get() == 'O'):
            tile['text'] = 'O'
            self.set_red_turn()

    def get_current_turn(self):
        return self.current_turn

    def set_red_turn(self):
        self.current_turn = self.RED_TURN
        self.current_turn_string.set(self.RED_TURN)

    def set_blue_turn(self):
        self.current_turn = self.BLUE_TURN
        self.current_turn_string.set(self.BLUE_TURN)


# MAIN
game = SOS_GAME_GUI()
game.start()
