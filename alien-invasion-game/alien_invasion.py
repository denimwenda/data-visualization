import sys

import pygame

from settings import Settings

def run_game():
    """Initialize game and create screen object."""
    pygame.init()
    ai_settings = Settings()  #Create an instance
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)

    #Start the main loop for the game
    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)

        #Make the most recently drawn screen visible visible.
        pygame.display.flip()

run_game()