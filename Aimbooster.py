import sys, pygame, time
from pygame.locals import *

from target import Target
from settings import Settings
from scoreboard import Scoreboard
from endmenu import EndMenu
from startmenu import StartMenu

# Simple game to improve mouse precision. Click on the targets to make a new one appear. Hit as many targets as you can with as few misses as possible within 60 seconds to get the highest score.
class Aimbooster:
    # Overall class
   
    def __init__(self): # Initialize Aimbooster and auxiliary objects 
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Aimbooster")
        self.target = Target(self)
        self.sb = Scoreboard(self)

    def run_game(self): # excecution loop, updates target data, timer data, scoreboard, and menu data. Constantly updates the screen. 
        pygame.display.flip()
        self.sb.start_timer()
        self.target.update()
        self.update_screen()
        while True:
            self.sb.prep_timer()
            self.sb.show_timer()
            pygame.display.flip()
            self.check_events()
            if self.sb.return_time() >= 60: # runs the game for 60 seconds, shows end screen when its done. 
                self.screen.fill(self.settings.bg_color)
                self.end_menu = EndMenu(self, self.sb.return_score(), self.sb.return_misses())
                self.end_menu.prep_end()
                self.end_menu.show_end()
                pygame.display.flip()
                break
        while True: # check for end screen input
            self.check_end_events()
            
    
    def update_screen(self): # updates the screen, targets, and scoreboard
        self.screen.fill(self.settings.bg_color)
        self.target.update()
        self.target.blitme()
        self.sb.show_score()
        pygame.display.flip()

    def check_end_events(self): # Allows exit from program from both quit and X menu button. 
        for event in pygame.event.get():
            if event.type == QUIT:
                        pygame.QUIT()
                        sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos 
                    if self.end_menu.replay_button.collidepoint(mouse_pos): #If replay button pressed, resets score and time
                        self.sb.score = 0
                        self.sb.misses = 0
                        self.sb.start = time.time()
                        self.run_game()
                        break
                    elif self.end_menu.end_button.collidepoint(mouse_pos):
                        pygame.QUIT()
                        sys.exit()

    def check_start_events(self): # checks input from the start screen
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.start_menu.start_button.collidepoint(mouse_pos):
                    self.run_game()
                elif self.start_menu.instr_button.collidepoint(mouse_pos):
                    self.screen.fill(self.settings.bg_color)
                    self.start_menu.display_instruct()
                    pygame.display.flip()
                    while True:
                        self.check_instr_events()

    def show_start_menu(self):
        self.screen.fill(self.settings.bg_color)
        self.start_menu = StartMenu(self)
        self.start_menu.prep_start()
        self.start_menu.show_start()
        pygame.display.flip()
        while True:
            self.check_start_events()

    def check_instr_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.start_menu.back_button.collidepoint(mouse_pos):
                    self.show_start_menu()

    def check_events(self): #Checks for input
            for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.QUIT()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos 
                    if self.target.button.collidepoint(mouse_pos): # If the mouse clicks on the target, progress game.
                        self.sb.incrementScore()
                        self.sb.prep_score()
                        self.target.update()
                        self.target.blitme()
                        self.update_screen()
                    else: 
                        self.sb.incrementMisses() # If the mouse click misses, increment misses.
                        self.sb.prep_score()
                        self.sb.show_score()
                        pygame.display.flip()

if __name__ == '__main__':
    ai = Aimbooster()
    ai.show_start_menu()
    

