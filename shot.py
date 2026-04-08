from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius, bounce = False):
        super().__init__(x, y, radius)
        self.has_bounce = bounce
        self.bounce_count = 0
        self.max_bounces = 3

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_SHOT, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
        if self.has_bounce:
            if not 0 < self.position.x < SCREEN_WIDTH:
                self.position.x = max(0, min(self.position.x, SCREEN_WIDTH))
                self.velocity.x *= -1
                self.bounce_count += 1
            if not 0 < self.position.y < SCREEN_HEIGHT:
                self.position.y = max(0, min(self.position.y, SCREEN_HEIGHT))
                self.velocity.y *= -1
                self.bounce_count += 1
            if self.bounce_count >= self.max_bounces:
                self.has_bounce = False