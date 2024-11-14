import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen
        
        self.image = pygame.transform.scale(pygame.image.load('eagle-4837272_960_720.jpg'), (75, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blit(self):
        self.screen.blit(self.image, self.rect)