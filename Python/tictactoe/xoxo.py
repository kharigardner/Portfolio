from pygame import *
import pygame



def terminate():
    pygame.quit()
    sys.exit()

def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return

def draw_xo(surface, board, x, y):
    # A function to draw the X or O on the board
    if board[x][y] == "X":
        surface.blit(game_font.render("X", True, (0, 0, 0)), (x * 200 + 50, y * 200 + 150))
    elif board[x][y] == "O":
        surface.blit(game_font.render("O", True, (0, 0, 0)), (x * 200 + 50, y * 200 + 150))

def draw_board(surface, board):
    # A function to draw the board
    for x in range(3):
        for y in range(3):
            draw_xo(surface, board, x, y)

def get_board_copy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupe_board = []
    for j in board:
        dupe_board.append(j[:])
    return dupe_board

def is_space_free(board, x, y):
    # Return true if the passed move is free on the passed board.
    return board[x][y] == " "

def get_player_move(board):
    # Let the player type in their move.
    x, y = None, None
    while not (0 <= x <= 2 and 0 <= y <= 2):
        print("What is your next move? (0-2 0-2)")
        x, y = input().split()
        return int(x), int(y)

def get_computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == "X":
        # computer move
        with move as minimax(board, 3, True)[0]:
            return move
    else:
        with move as minimax(board, 3, False)[0]:
            return move

def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for x in range(3):
        for y in range(3):
            if is_space_free(board, x, y):
                return False
    return True

def make_move(board, letter, x, y):
    # Place the letter on the board at the given coordinates
    board[x][y] = letter
    move = (x, y)
    return move

# initalise pygame
pygame.init()
pygame.display.set_caption("Tic Tac Toe")
pygame.font.init()

# set up the window
pygame.display.set_mode((600, 600))
pygame.mouse.set_visible(False)

screen = pygame.display.get_surface()
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
draw_board(screen, board)
draw_xo(screen, board, 0, 0)
pygame.display.update()
wait_for_key()
