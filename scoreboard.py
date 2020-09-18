import pygame.font
import time
from settings import Settings

# Displays score, misses, and timer on play screen
class Scoreboard:
    score = 0
    misses = 0
    start = 0
    time = 0

    def __init__(self, ai_game): # Sets initial variable values.
        self.screen = ai_game.screen
        self.settings = Settings()
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0, 0, 0)
        self.miss_text_color = (220, 0, 0)
        self.font = pygame.font.SysFont(None, 30)
        self.prep_score()

    def prep_score(self): # turns current score and misses into a string to be output to the screen. 
        score_str = str(self.score)
        miss_str = str(self.misses)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.miss_image = self.font.render(miss_str, True, self.miss_text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.miss_rect = self.miss_image.get_rect()
        self.score_rect.right  = self.screen_rect.right - 45
        self.miss_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        self.miss_rect.top = 20
    
    def show_score(self): # Update screen with current score
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.miss_image, self.miss_rect)

    def incrementScore(self): 
        self.score += 1
    
    def incrementMisses(self):
        self.misses += 1
    
    def start_timer(self):
        self.start = time.time()
    
    def prep_timer(self): # calculates time since start and sets the time on the top left.
        self.time = int(time.time() - self.start)
        time_str =  str(self.time)
        self.time_image = self.font.render(time_str, True, self.text_color, self.settings.bg_color)
        self.time_rect = self.time_image.get_rect()
        self.time_rect.left = self.screen_rect.left + 25
        self.time_rect.top = 20
    
    def show_timer(self): # Updates time to screen
        self.screen.blit(self.time_image, self.time_rect)

    def return_time(self):
        return self.time

    def return_score(self):
        return self.score

    def return_misses(self):
        return self.misses

