import pygame
from constants import *

class Score():
    def __init__(self):
        self.score = 0
        self.lives = 3

        self.font = pygame.font.Font("assets/Tronica Mono.ttf", SCORE_FONT_SIZE) 
        self.__draw_score()
        
    def __draw_score(self):
        self.points_draw_surface = self.font.render(f"Score: {self.score}", True, "white")
        self.lives_draw_surface = self.font.render(f"Lives: {self.lives}", True, "white")
    
    def add_points(self, points):
        old_score = self.score
        self.score += points
        if self.score // EXTRA_LIFE_POINTS > old_score // EXTRA_LIFE_POINTS:
            self.lives += 1
        self.__draw_score()

    def draw(self, screen):
        screen.blit(self.points_draw_surface, SCORE_POSITION)
        screen.blit(self.lives_draw_surface, LIVES_POSITION)

    def subtract_life(self):
        self.lives -= 1
        self.__draw_score()
        return self.lives > 0
