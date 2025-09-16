
import pygame
from Bullet import Bullet


class Ship():
    
    def __init__(self, space_shooter):
        pygame.init()
        
        self.screen = space_shooter.screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load('Chapter 12 - A Ship That Fires Bullets\\Chapter 12 Project\\images\\spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.rect.midbottom = self.screen_rect.midbottom
           
        self.bullets = pygame.sprite.Group()
        
    def blitme(self):
        
        self.screen.blit(self.image, self.rect)
        
    def ship_movement(self, event_flag: list, activate_boost: bool):
        
        speed_boost = 3.5
            
        if event_flag[0] and self.rect.top > 0:
            self.rect.y = float(self.rect.y - speed_boost) if activate_boost else float(self.rect.y - 1.5)            
            print('UP')
            
        if event_flag[1] and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y = float(self.rect.y + speed_boost) if activate_boost else float(self.rect.y + 1.5)
            print('DOWN')
                       
        if event_flag[2] and self.rect.left > 0:
            self.rect.x = float(self.rect.x - speed_boost) if activate_boost else float(self.rect.x - 1.5)
            print('LEFT')
            
        if event_flag[3] and self.rect.right < self.screen_rect.right:
            self.rect.x = float(self.rect.x - speed_boost) if activate_boost else float(self.rect.x + 1.5)         
            print('RIGHT')  
              
        
      
        