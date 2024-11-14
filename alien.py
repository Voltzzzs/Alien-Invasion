import pygame
from settings import Settings
from eagle import Ship



import sys


def run_game():
    pygame.init()
    g_settings = Settings()
    screen = pygame.display.set_mode((g_settings.screen_width, g_settings.screen_height))
    eagle = Ship(screen) 
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(g_settings.bg_color)
        eagle.blit()
        
        pygame.display.flip()

run_game()
    