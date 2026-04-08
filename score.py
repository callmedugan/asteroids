import pygame
from constants import *

class Score():
    def __init__(self):
        self.points = 0
        self.lives = STARTING_LIVES
        self.level = 1
        self.modifier = 1

        self.points_position = (20, 20)
        self.lives_position = (20, 70)
        self.level_position = (20, 120)

        self.font = pygame.font.Font("assets/Tronica Mono.ttf", SCORE_FONT_SIZE) 
        self.powerup_duration_font = pygame.font.Font("assets/Tronica Mono.ttf", POWERUP_DURATION_FONT_SIZE) 
        self.__update_text()
        
    #these only need to be called when the text changes, not every frame
    def __update_text(self):
        self.points_draw_surface = self.font.render(f"Score: {self.points}", True, "white")
        self.lives_draw_surface = self.font.render(f"Lives: {self.lives}", True, "white")
        self.level_draw_surface = self.font.render(f"Level: {self.level}", True, "white")

    #checks to see if level data for next level exists and retrieves the modifier for next level
    def __check_for_levelup(self):
        if self.level in LEVEL_DATA and self.points > LEVEL_DATA[self.level][0] and self.level + 1 in LEVEL_DATA:
            self.level += 1
            self.modifier = LEVEL_DATA[self.level][1]
            return True
        return False

    #draw to the screen every frame
    def draw(self, screen, player):
        #draw the lefthand scores
        screen.blit(self.points_draw_surface, self.points_position)
        screen.blit(self.lives_draw_surface, self.lives_position)
        screen.blit(self.level_draw_surface, self.level_position)
        #draw the powerup durations
        y_offset = 20
        for p in player.get_powerup_info():
            text = f"{p[0]}: {int(p[1])}s"
            color = p[2] if p[1] > 5 else "red"
            text_surface = self.powerup_duration_font.render(text, True, color)
            width, height = self.powerup_duration_font.size(text)
            screen.blit(text_surface, (SCREEN_WIDTH - width - 20, y_offset))
            y_offset += height + 10
    
    #add points and do all necessary checks
    def add_points(self, points):
        old_score = self.points
        self.points += int(points * self.modifier)
        if self.points // EXTRA_LIFE_POINTS > old_score // EXTRA_LIFE_POINTS:
            self.lives += 1
        level_up = self.__check_for_levelup()
        self.__update_text()
        return level_up

    #try to subtract a life and return false if 0
    def subtract_life(self):
        self.lives -= 1
        self.__update_text()
        return self.lives > 0
