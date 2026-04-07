import pygame
from circleshape import CircleShape
from constants import *
from player import Player
import random

class Powerup(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

        self.type = None
        self.duration = None
        self.type_key = None
        self.__get_random_powerup()

    def __get_random_powerup(self):
        self.type_key = random.choice(list(POWERUP_DATA))
        self.type = POWERUP_DATA[self.type_key][0]
        self.duration = POWERUP_DATA[self.type_key][1]

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_POWERUP, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def activate(self, player):
        #shields
        if self.type_key == 1:
            player.shield_powerup(self.duration)
        #fire rate up
        elif self.type_key == 2:
            player.fire_rate_up_powerup(self.duration)