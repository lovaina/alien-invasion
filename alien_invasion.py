import sys
import pygame


def run_game():

    #initialize game and create screen

    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    # Set the backgroud color
    bg_color = (230,230,230)

    # Start the main loop for the game
    while True:

        # Watch for the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(bg_color)

        #Make the most recently drawn screen visible
        pygame.display.flip()

run_game()