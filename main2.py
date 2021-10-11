from tkinter import *
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
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 1200
    WINDOW = Tk()
    WINDOW.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    WINDOW.title("Morgan's SOS Game")
    BUTTON_HEIGHT = 3
    BUTTON_WIDTH = 4

    def __init__(self):
        self.gameboard = SOS_GAME_BOARD()

    def start(self):
        self.create_GUI_board()
        #self.create_player_buttons()
        self.WINDOW.mainloop() # place window on computer screen, listen for events

    def create_GUI_board(self):
        for r in range(self.gameboard.NUM_ROWS):
            for c in range(self.gameboard.NUM_COLS):
                self.gameboard.board[r][c] = Button(self.WINDOW, bg="SystemButtonFace", height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH)
                self.gameboard.board[r][c].grid(row=r, column=c)

    #def create_player_buttons():

            

        


# MAIN
game = SOS_GAME_GUI()
game.start()