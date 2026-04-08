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
        self.is_dead = False
        self.respawn_time_secs = 3.0
        self.respawn_timer = 0.0
        self.respawn_position = pygame.Vector2(x, y)
    
        #powerups
        self.shields_active = False
        self.shield_timer = 0.0
        self.fire_rate_up_active = False
        self.fire_rate_up_timer = 0.0
        self.speed_up_active = False
        self.speed_up_timer = 0.0
        self.multishot_active = False
        self.multishot_timer = 0.0
        self.bounce_active = False
        self.bounce_timer = 0.0

    def __triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        triangle_shape = self.__triangle()
        self.shot_position = triangle_shape[0]
        color = "red" if self.is_dead else COLOR_PLAYER
        pygame.draw.polygon(screen, color, triangle_shape, LINE_WIDTH)
        if self.shields_active:
            pygame.draw.circle(screen, POWERUP_DATA[1][2], self.position, self.radius * 1.4, LINE_WIDTH)

    def __rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        speed = PLAYER_SPEED * 1.25 if self.speed_up_active else PLAYER_SPEED
        rotated_with_speed_vector = rotated_vector * speed * dt
        self.position += rotated_with_speed_vector
        #clamp pos to inbounds
        self.position.x = max(0, min(self.position.x, SCREEN_WIDTH))
        self.position.y = max(0, min(self.position.y, SCREEN_HEIGHT))

    def update(self, dt):
        #shields
        self.shield_timer = max(self.shield_timer - dt, 0)
        if self.shields_active and self.shield_timer == 0:
            self.shields_active = False
        #fire rate up
        self.fire_rate_up_timer = max(self.fire_rate_up_timer - dt, 0)
        if self.fire_rate_up_active and self.fire_rate_up_timer == 0:
            self.fire_rate_up_active = False
        #speed up
        self.speed_up_timer = max(self.speed_up_timer - dt, 0)
        if self.speed_up_active and self.speed_up_timer == 0:
            self.speed_up_active = False
        #multishot
        self.multishot_timer = max(self.multishot_timer - dt, 0)
        if self.multishot_active and self.multishot_timer == 0:
            self.multishot_active = False
        #bounce
        self.bounce_timer = max(self.bounce_timer - dt, 0)
        if self.bounce_active and self.bounce_timer == 0:
            self.bounce_active = False

        self.shot_cooldown_timer = max(self.shot_cooldown_timer - dt, 0)
        self.hit_cooldown_timer = max(self.hit_cooldown_timer - dt, 0)

        #respawn logic
        if self.is_dead:
            self.respawn_timer = max(self.respawn_timer - dt, 0)
            #ready to respawn
            if self.is_dead and self.respawn_timer == 0:
                self.is_dead = False
                self.hit_cooldown_timer = PLAYER_HIT_COOLDOWN_SECONDS
                self.position = self.respawn_position
        else:
            keys = pygame.key.get_pressed()
            #movement/rotation
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.__rotate(-dt)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.__rotate(dt)
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
        #for fire rate up powerup - breaking into if statement for later
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS / 2 if self.fire_rate_up_active else PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.shot_position.x, self.shot_position.y, SHOT_RADIUS, self.bounce_active)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        if self.multishot_active:
            spread = 20
            shot2 = Shot(self.shot_position.x, self.shot_position.y, SHOT_RADIUS, self.bounce_active)
            shot2.velocity = pygame.Vector2(0, 1).rotate(self.rotation - spread) * PLAYER_SHOOT_SPEED
            shot3 = Shot(self.shot_position.x, self.shot_position.y, SHOT_RADIUS, self.bounce_active)
            shot3.velocity = pygame.Vector2(0, 1).rotate(self.rotation + spread) * PLAYER_SHOOT_SPEED

    #returns if player dies
    def is_hit(self):
        if self.hit_cooldown_timer == 0:
            self.hit_cooldown_timer = PLAYER_HIT_COOLDOWN_SECONDS
            if self.shields_active:
                self.shields_active = False
                self.shield_timer = 0
                return False
            self.is_dead = True
            self.respawn_timer = self.respawn_time_secs
            return True
        
    def shield_powerup(self, duration):
        self.shields_active = True
        self.shield_timer = duration

    def fire_rate_up_powerup(self, duration):
        self.fire_rate_up_active = True
        self.fire_rate_up_timer = duration
        #set cooldown to half the normal cooldown 
        self.shot_cooldown_timer = min(self.shot_cooldown_timer, PLAYER_HIT_COOLDOWN_SECONDS / 2)

    def speed_up_powerup(self, duration):
        self.speed_up_active = True
        self.speed_up_timer = duration

    def multishot_powerup(self, duration):
        self.multishot_active = True
        self.multishot_timer = duration

    def bounce_powerup(self, duration):
        self.bounce_active = True
        self.bounce_timer = duration

    #returns all active powerups [name, duration, color]
    def get_powerup_info(self):
        result = []
        if self.shields_active:
            result.append([POWERUP_DATA[1][0], self.shield_timer, POWERUP_DATA[1][2]])
        if self.fire_rate_up_active:
            result.append([POWERUP_DATA[2][0], self.fire_rate_up_timer, POWERUP_DATA[2][2]])
        if self.speed_up_active:
            result.append([POWERUP_DATA[3][0], self.speed_up_timer, POWERUP_DATA[3][2]])
        if self.multishot_active:
            result.append([POWERUP_DATA[4][0], self.multishot_timer, POWERUP_DATA[4][2]])
        if self.bounce_active:
            result.append([POWERUP_DATA[5][0], self.bounce_timer, POWERUP_DATA[5][2]])
        result.sort(key= lambda x: x[1])
        return result
    
    def collides_with(self, other):
        if self.is_dead:
            return False
        return self.position.distance_squared_to(other.position) < (self.radius + other.radius)**2