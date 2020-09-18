
import pygame.font
from settings import Settings

#Class for the start menu with buttons
class StartMenu:
    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        self.settings = Settings()
        self.screen_rect = self.screen.get_rect()
        self.text_color = (100, 100, 100)
        self.str_text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 100)
        self.start_button = pygame.draw.rect(self.screen , self.settings.bg_color , (int(self.settings.screen_width/2) - 50, int(self.settings.screen_height/2 - 30), 100, 60)) #draws start button
        self.instr_button = pygame.draw.rect(self.screen , self.settings.bg_color , (int(self.settings.screen_width/2) - 125, int(self.settings.screen_height/2 + 70), 250, 60)) #draws instr button

    def prep_start(self):   #gets the text for the start screen placed and ready
        self.aim_image = self.font.render("Aimbooster", True, (255, 0, 0), self.settings.bg_color)
        self.aim_rect = self.aim_image.get_rect()
        self.aim_rect.center = self.screen_rect.center
        self.aim_rect.top = 100
        self.font = pygame.font.SysFont(None, 60)
        self.start_image = self.font.render("Start", True, self.text_color, self.settings.bg_color)
        self.start_rect = self.start_image.get_rect()
        self.start_rect.center = self.screen_rect.center
        self.instr_image = self.font.render("Instructions", True, (self.text_color), self.settings.bg_color)
        self.instr_rect = self.instr_image.get_rect()
        self.instr_rect.center = self.screen_rect.center
        self.instr_rect.y += 100
         
    def show_start(self): # displays the images on the rectangles
        self.screen.blit(self.start_image, self.start_rect)
        self.screen.blit(self.instr_image, self.instr_rect)
        self.screen.blit(self.aim_image, self.aim_rect)

    def display_instruct(self): # full prep and show of the text and button in the intructions page
        self.back_button = pygame.draw.rect(self.screen ,self.settings.bg_color , (int(self.settings.screen_width/2) - 65, int(self.settings.screen_height/2) + 90, 130, 60)) 
        self.font = pygame.font.SysFont(None, 40)
        instructions_str1 = "This is a simple aim training game."
        self.instruct_image = self.font.render(instructions_str1,True ,self.str_text_color , self.settings.bg_color)
        self.instruct_rect = self.instruct_image.get_rect()
        self.instruct_rect.center = self.screen_rect.center
        self.instruct_rect.top = 300
        self.screen.blit(self.instruct_image, self.instruct_rect)
        instructions_str2 = "Hit as many targets as you can without missing!"
        self.instruct2_image = self.font.render(instructions_str2,True ,self.str_text_color , self.settings.bg_color)
        self.instruct2_rect = self.instruct2_image.get_rect()
        self.instruct2_rect.center = self.screen_rect.center
        self.instruct2_rect.top = 330
        self.screen.blit(self.instruct2_image, self.instruct2_rect)
        instructions_str3 = "The game ends in 60 seconds."
        self.instruct3_image = self.font.render(instructions_str3,True ,self.str_text_color , self.settings.bg_color)
        self.instruct3_rect = self.instruct3_image.get_rect()
        self.instruct3_rect.center = self.screen_rect.center
        self.instruct3_rect.top = 360
        self.font = pygame.font.SysFont(None, 60)
        self.screen.blit(self.instruct3_image, self.instruct3_rect)
        self.back_image = self.font.render("Back" ,True ,self.text_color , self.settings.bg_color)
        self.back_rect = self.back_image.get_rect()
        self.back_rect.center = self.screen_rect.center
        self.back_rect.top = 500
        self.screen.blit(self.back_image, self.back_rect)
