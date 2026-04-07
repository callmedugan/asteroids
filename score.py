import pygame
from constants import *

class Score():
    def __init__(self):
        self.points = 0
        self.lives = 3
        self.level = 1
        self.modifier = 1

        self.points_position = (20, 20)
        self.lives_position = (20, 70)
        self.level_position = (20, 120)

        self.font = pygame.font.Font("assets/Tronica Mono.ttf", SCORE_FONT_SIZE) 
        self.__update_text()
        
    #change text only needs to be called when the text changes, not every frame
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
    def draw(self, screen):
        screen.blit(self.points_draw_surface, self.points_position)
        screen.blit(self.lives_draw_surface, self.lives_position)
        screen.blit(self.level_draw_surface, self.level_position)
    
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
