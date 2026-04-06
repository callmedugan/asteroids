from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius = PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.hit_cooldown_timer = 0
        self.shot_position = pygame.Vector2(0, 1)
    

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):

        triangle_shape = self.triangle()
        self.shot_position = triangle_shape[0]
        if self.hit_cooldown_timer != 0:
            pygame.draw.polygon(screen, "red", triangle_shape, LINE_WIDTH)
        else:
            pygame.draw.polygon(screen, COLOR_PLAYER, triangle_shape, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def update(self, dt):
        self.shot_cooldown_timer = max(self.shot_cooldown_timer - dt, 0)
        self.hit_cooldown_timer = max(self.hit_cooldown_timer - dt, 0)

        keys = pygame.key.get_pressed()

        #movement/rotation
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        #shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.shot_position.x, self.shot_position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def is_hit(self):
        if self.hit_cooldown_timer == 0:
            self.hit_cooldown_timer = PLAYER_HIT_COOLDOWN_SECONDS
            return True