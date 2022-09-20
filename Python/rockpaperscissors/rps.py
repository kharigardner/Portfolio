from pygame import *
import pygame
import random


# defining functions to use for game logic
def terminate():
    # A function to terminate the game
    pygame.quit()
    sys.exit()

def wait_for_key():
    # A function to wait for a key press
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return

# function to draw widgets representing rock, paper, scissors
def draw_rps(surface):
    rock = pygame.image.load("rock.png")
    paper = pygame.image.load("paper.png")
    scissors = pygame.image.load("scissors.png")
    for x in range(3):
        for y in range(3):
            if x == 0:
                surface.blit(rock, (x * 200 + 50, y * 200 + 150))
            elif x == 1:
                surface.blit(paper, (x * 200 + 50, y * 200 + 150))
            elif x == 2:
                surface.blit(scissors, (x * 200 + 50, y * 200 + 150))
    # make the images clickable
    rock_rect = rock.get_rect()
    paper_rect = paper.get_rect()
    scissors_rect = scissors.get_rect()
    # wait for a click
    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                try:
                    if rock_rect.collidepoint(x, y):
                        return "rock"
                    if paper_rect.collidepoint(x, y):
                        return "paper"
                    if scissors_rect.collidepoint(x, y):
                        return "scissors"
                except:
                    raise Exception("Invalid move")
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

def computer_rps():
    # A function to return a random move for the computer
    return random.choice(["rock", "paper", "scissors"])

def game_sequence():
    # A function to run the game sequence
    pygame.init()
    pygame.display.set_caption("Rock Paper Scissors")
    screen = pygame.display.set_mode((600, 600))
    screen.fill((255, 255, 255))
    player_move = draw_rps(screen)
    computer_move = computer_rps()
    if player_move == computer_move:
        print("It's a tie!")
    elif player_move == "rock":
        if computer_move == "paper":
            print("You lose!")
        elif computer_move == "scissors":
            print ("You win!")
    elif player_move == "paper":
        if computer_move == "rock":
            print("You win!")
        elif computer_move == "scissors":
            print("You lose!")
    elif player_move == "scissors":
        if computer_move == "rock":
            print("You lose!")
        elif computer_move == "paper":
            print("You win!")
    wait_for_key()
    print("Thanks for playing!")


if __name__ == "__main__":
    game_sequence()