
import sys
import pygame
import time

from Ship import Ship
from Bullet import Bullet

class SpaceShooter():
    
    def __init__(self):
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((900, 600))
        
        pygame.display.set_caption('Space Shooter')
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
        
        self.move = [False, False, False, False]
        self.boost = False
        
    def run_game(self):
        
        while True:            
            self._check_events()
            
            self.bullets.update()
            
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                  self.bullets.remove(bullet)
            
            self._update_screen()
            
            self.clock.tick(60) #framerate           
            self.ship.ship_movement(self.move, self.boost)
            
            
 
            
    def _check_events(self):
              
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                sys.exit()               
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.move[0] = True
                
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.move[1] = True
                    
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.move[2] = True
                    
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.move[3] = True                            
                
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
                
                if event.key == pygame.K_LSHIFT:
                    self.boost = True
                        
            if event.type == pygame.KEYUP:
                self.move = [False, False, False, False]
                self.boost = False
                
                
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)   
    
    
    def _update_screen(self):               
        self.screen.fill((10, 100, 255))
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()            
        self.ship.blitme()
        pygame.display.flip()
        
        
if __name__ == '__main__':
    space_shooter = SpaceShooter()
    space_shooter.run_game()        
            