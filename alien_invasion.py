#October, 31 - 2021 - SELFOR - Jundiai - SP - BR

import sys

import pygame
from settings import Settings
from ship import Ship


def run_game():
    #game start and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")

    #Spaceship creation
    ship=Ship(screen)

    #main loop
    while True:

        #keyboard and mouse events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #increases screen visibility
        pygame.display.flip()        

run_game()