import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():

    #initialize game and create screen

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

run_game()