import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # FPS stuff
    clock = pygame.time.Clock()
    dt = 0
    desired_fps = 60

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    #objects
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    score = Score()

    while True:
        #update
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                if player.is_hit() and not score.subtract_life():
                    print("Game over!")
                    sys.exit()
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    s.kill()
                    asteroid_hit_size = a.split()
                    score.add_points(SCORES_FOR_ASTEROIDS[asteroid_hit_size])

        #drawing
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        score.draw(screen)
        pygame.display.flip()
        dt = clock.tick(desired_fps)/1000


if __name__ == "__main__":
    main()
