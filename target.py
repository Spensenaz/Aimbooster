import pygame
import random

#Class to represent target object. 
class Target:
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/target.png') #Load target image
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.button = pygame.draw.circle(self.screen , (0, 0, 0), (int(self.settings.screen_width/2), int(self.settings.screen_height/2)), 25) # Draw the button

    def blitme(self): #update screen with target
        self.screen.blit(self.image, self.rect)
    
    def update(self): #randomly sets button location on screen
        self.x = random.randrange(50, self.settings.screen_width - 50) 
        self.y = random.randrange(50, self.settings.screen_height - 50)
        self.rect.x = self.x
        self.rect.y = self.y
        self.button.x = self.x
        self.button.y = self.y
