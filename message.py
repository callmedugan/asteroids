import pygame
from constants import *
from enum import Enum

class Message_status(Enum):
    NONE = 0
    LEVEL_UP = 1
    POWERUP = 2
    GAME_OVER = 3

class Message():
    def __init__(self, screen):
        self.font = pygame.font.Font("assets/Tronica Mono.ttf", LEVEL_UP_FONT_SIZE) 
        self.game_over_font = pygame.font.Font("assets/Tronica Mono.ttf", GAME_OVER_FONT_SIZE)  
        self.points_font = pygame.font.Font("assets/Tronica Mono.ttf", GAME_OVER_POINTS_FONT_SIZE)  
        self.bottom_text_font = pygame.font.Font("assets/Tronica Mono.ttf", GAME_OVER_BOTTOM_TEXT_FONT_SIZE)  

        #vars
        self.status = Message_status.NONE
        self.is_shown = False
        self.duration_secs = 4
        self.flicker_time_secs = 0.6
        self.timer = 0.0
        self.flicker_timer = 0.0

        #custom settings
        self.show_powerups = False

        #refs
        self.screen = screen
        self.top_screen_position = None
        self.mid_screen_position = None
        self.bottom_screen_position = None

        self.top_draw_surface = None
        self.mid_draw_surface = None
        self.bottom_draw_surface = None
        
    #change text only needs to be called when the text changes, not every frame
    def level_up(self):
        self.top_draw_surface = self.font.render("LEVEL UP!", True, "white")
        self.top_screen_position = self.top_draw_surface.get_rect(center=self.screen.get_rect().center)
        self.status = Message_status.LEVEL_UP
        self.is_shown = True
        self.timer = 0
        self.flicker_timer = 0

    def powerup(self, name, duration):
        if not self.show_powerups:
            return
        self.top_draw_surface = self.font.render(f"{name.upper()}! ({int(duration)}s)", True, "white")
        self.top_screen_position = self.top_draw_surface.get_rect(center=self.screen.get_rect().center)
        self.status = Message_status.POWERUP
        self.is_shown = True
        self.timer = 0
        self.flicker_timer = 0

    def game_over(self, points):
        self.top_draw_surface = self.game_over_font.render("GAME OVER!", True, "white")
        self.mid_draw_surface = self.points_font.render(f"Final score: {points}", True, "white")
        self.bottom_draw_surface = self.bottom_text_font.render("Press ENTER...", True, "white")
        self.top_screen_position = self.top_draw_surface.get_rect(center=self.screen.get_rect().center)
        self.mid_screen_position = self.mid_draw_surface.get_rect(center=self.screen.get_rect().center).move(0, 80)
        self.bottom_screen_position = self.bottom_draw_surface.get_rect(center=self.screen.get_rect().center).move(0, 140)
        self.status = Message_status.GAME_OVER
        self.is_shown = True
        #doing this way to have the option to revert to flicker style game over screen
        self.duration_secs = float("inf")
        self.flicker_time_secs = float("inf")

    def draw(self, dt):
        if self.status:
            self.flicker_timer += dt
            self.timer += dt
            #if flicker timer is over the flicker time, flip is_shown and reset the timer
            if self.flicker_timer > self.flicker_time_secs:
                self.is_shown = not self.is_shown
                self.flicker_timer = 0
            #while duration is within the message duration seconds
            if self.timer < self.duration_secs:
                if self.is_shown:
                    if self.status == Message_status.LEVEL_UP or self.status == Message_status.POWERUP:
                        self.screen.blit(self.top_draw_surface, self.top_screen_position)
                    elif self.status == Message_status.GAME_OVER:
                        self.screen.blit(self.top_draw_surface, self.top_screen_position)
                        self.screen.blit(self.mid_draw_surface, self.mid_screen_position)
                        self.screen.blit(self.bottom_draw_surface, self.bottom_screen_position)
            #message has ended
            else:
                self.status = Message_status.NONE