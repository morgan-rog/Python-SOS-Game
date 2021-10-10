import pygame
import sys

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
                self.board[row].append(0)  # append empty cell

    def set_cell_value(self, row, col, value):
        self.board[row][col] = value

    def get_cell_value(self, row, col):
        return self.board[row][col]


class SOS_GAME_GUI():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    SYMBOL_COLOR = (0, 0, 0)
    BACKGROUND_COLOR = (153, 209, 204)
    WHITE_CELL_COLOR = (255, 255, 255)
    CELL_WIDTH = 30
    CELL_HEIGHT = 30
    MARGIN = 30
    FONT = pygame.font.Font('freesansbold.ttf', 30)
    EMPTY_CELL = FONT.render('-', True, SYMBOL_COLOR, WHITE_CELL_COLOR)
    S_SYMBOL = FONT.render('S', True, SYMBOL_COLOR, WHITE_CELL_COLOR)
    O_SYMBOL = FONT.render('O', True, SYMBOL_COLOR, WHITE_CELL_COLOR)
    BLOCK_SIZE = 30

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('SOS GAME')
    SCREEN.fill(BACKGROUND_COLOR)

    def __init__(self):
        self.board = SOS_GAME_BOARD()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    column = mouse_position[0] // (self.CELL_WIDTH + self.MARGIN)
                    row = mouse_position[1] // (self.CELL_HEIGHT + self.MARGIN)
                    self.board.set_cell_value(row, column, 1)

                    print("Click ", mouse_position, "Grid coordinates: ", row, column)


                if event.type == pygame.QUIT:
                    sys.exit()

            self.draw_board()
            pygame.display.update()

    def draw_board(self):
        for row in range(self.board.NUM_ROWS):
            for col in range(self.board.NUM_COLS):
                if self.board.get_cell_value(row, col) == 0:
                    symbol = self.EMPTY_CELL
                    
                elif self.board.get_cell_value(row, col) == 1:
                    symbol = self.S_SYMBOL
                
                elif self.board.get_cell_value(row, col) == 2:
                    symbol = self.O_SYMBOL

                symbolRect = symbol.get_rect(topleft=((self.MARGIN + self.CELL_WIDTH) * col + self.MARGIN, (
                    self.MARGIN + self.CELL_HEIGHT) * row + self.MARGIN))
                self.SCREEN.blit(symbol, symbolRect)

                # pygame.draw.rect(self.SCREEN, cell_display, [(self.MARGIN + self.CELL_WIDTH) * col + self.MARGIN, (
                #     self.MARGIN + self.CELL_HEIGHT) * row + self.MARGIN, self.CELL_WIDTH, self.CELL_HEIGHT])


# MAIN
game = SOS_GAME_GUI()
game.start()
