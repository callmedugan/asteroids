from circleshape import CircleShape
from constants import *
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, size, velocity):
        super().__init__(x, y, radius)
        self.size = size
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_ASTEROID, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return self.size
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        asteroid_1_vel = self.velocity.rotate(angle) * 1.2
        asteroid_2_vel = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, self.size - 1, self.velocity)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, self.size - 1, self.velocity)
        asteroid_1.velocity = asteroid_1_vel
        asteroid_2.velocity = asteroid_2_vel
        return self.size
