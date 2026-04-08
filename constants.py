#game
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
#player
PLAYER_RADIUS = 20
PLAYER_SPEED = 200
PLAYER_TURN_SPEED = 300
SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
PLAYER_HIT_COOLDOWN_SECONDS = 3
#drawing
LINE_WIDTH = 2
#asteroids
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
#powerups
POWERUP_RADIUS = 15
POWERUP_DATA = {
    #key: [name, duration, color]
    1: ["shields", 30.0, "cyan"],
    2: ["fire rate up", 30.0, (255, 92, 0)],
    3: ["speed up", 30.0, "magenta"],
    4: ["multishot", 30.0, (57, 255, 20)],
    5: ["bounce", 30.0, (255, 255, 0)],
    }
#colors
COLOR_PLAYER = (200, 200, 210)
COLOR_SHOT = "white"
COLOR_ASTEROID = (180, 137, 104)
#fonts
LEVEL_UP_FONT_SIZE = 80
GAME_OVER_FONT_SIZE = 120
GAME_OVER_POINTS_FONT_SIZE = 48
GAME_OVER_BOTTOM_TEXT_FONT_SIZE = 30
SCORE_FONT_SIZE = 48
POWERUP_DURATION_FONT_SIZE = 28
#score
STARTING_LIVES = 3
POINTS_FOR_ASTEROIDS = [0, 100, 50, 20]
EXTRA_LIFE_POINTS = 100000
LEVEL_DATA = {
    #key: [points needed for next level, static points modifier, asteroid spawn secs, asteroid speed]
    1: [500, 1.05, 0.7, 1.5],
    2: [5000, 1.1, 0.55, 1.75],
    3: [10000, 1.15, 0.4, 1.2],
    4: [20000, 1.2, 0.35, 2.5],
    5: [100000, 1.3, 0.3, 3],
    6: [250000, 1.5, 0.25, 3.75],
    7: [1000000, 1.75, 0.2, 4.5],
    }