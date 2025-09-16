import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.color = (255, 147, 0)

        self.rect = pygame.Rect(0, 0, 7, 15)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        self.bullet_speed = 10.0

        self.y = float(self.rect.y)
        
    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)    