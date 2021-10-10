import pygame, sys

pygame.init()

class Player():
    def __init__(self, player_num):
        self.player_num = player_num


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
                self.board[row].append(0) # append empty cell
    
    def get_cell_value(self, row, col):
        return self.board[row][col]


class SOS_GAME_GUI():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    BACKGROUND_COLOR = (153, 209, 204)
    EMPTY_CELL_COLOR = (255, 255, 255)
    CELL_WIDTH = 20
    CELL_HEIGHT = 20
    MARGIN = 5
    LINE_COLOR = (6, 89, 82)
    LINE_WIDTH = 10
    BLOCK_SIZE = 30

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('SOS GAME')
    SCREEN.fill(BACKGROUND_COLOR)
    
    def __init__(self):
        self.board = SOS_GAME_BOARD()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.draw_board()
            pygame.display.update()

    def draw_board(self):
        for row in range(self.board.NUM_ROWS):
            for col in range(self.board.NUM_COLS):
                color = (255, 0, 0)
                if self.board.get_cell_value(row, col) == 0:
                    color = self.EMPTY_CELL_COLOR
                
                pygame.draw.rect(self.SCREEN, color, [(self.MARGIN + self.CELL_WIDTH) * col + self.MARGIN, (self.MARGIN + self.CELL_HEIGHT) * row + self.MARGIN, self.CELL_WIDTH, self.CELL_HEIGHT])



# MAIN
game = SOS_GAME_GUI()
game.start()