
import pygame.font
from settings import Settings

# End menu to display score and ask to play again or quit.
class EndMenu:
    points = 0


    def __init__(self, ai_game, score, misses): # initial values set. 
        self.screen = ai_game.screen
        self.score = score
        self.misses = misses
        self.settings = Settings()
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 100)
        self.replay_button = pygame.draw.rect(self.screen, self.settings.bg_color, (int(self.settings.screen_width/2) - 130, int(self.settings.screen_height/2), 100, 50)) #set up buttons in middle of screen
        self.end_button = pygame.draw.rect(self.screen , self.settings.bg_color, (int(self.settings.screen_width/2) + 50, int(self.settings.screen_height/2), 100, 50)) 

    def show_end(self): # Set the screen with the buttons and text
        self.screen.blit(self.end_image, self.end_rect)
        self.screen.blit(self.retry_image, self.retry_rect)
        self.screen.blit(self.quit_image, self.quit_rect)

    def prep_end(self): # Set up end buttons with text overlay, and show score. 
        self.points = self.score - self.misses
        end_str = "Your score was {}.".format(self.points)
        self.end_image = self.font.render(end_str, True, self.text_color, self.settings.bg_color)
        self.end_rect = self.end_image.get_rect()
        self.end_rect.center  = self.screen_rect.center
        self.end_rect.top = 100
        self.font = pygame.font.SysFont(None, 60)
        self.retry_image = self.font.render("Retry", True, (100, 100, 100), self.settings.bg_color)
        self.quit_image = self.font.render("Quit", True, (100, 100, 100), self.settings.bg_color)
        self.retry_rect = self.retry_image.get_rect()
        self.quit_rect = self.quit_image.get_rect()
        self.retry_rect.x = 467 # specific horizontal values for text overlay to go in line with the buttons
        self.quit_rect.x = 655
        self.retry_rect.top = int(self.settings.screen_height/2) 
        self.quit_rect.top = int(self.settings.screen_height/2) 
        self.retry_rect.y += 4 # fine tune the vertical buttons to go in line with buttons
        self.quit_rect.y += 4






