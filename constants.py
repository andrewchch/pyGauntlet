"""
Game constants and configuration
"""

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Tile settings
TILE_SIZE = 32

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Game settings
PLAYER_SPEED = 4
ENEMY_SPEED = 2
PROJECTILE_SPEED = 8
SPAWN_INTERVAL = 3000  # milliseconds

# Map dimensions (in tiles)
MAP_WIDTH = 40
MAP_HEIGHT = 30

# Player starting position (in tiles)
PLAYER_START_X = 15
PLAYER_START_Y = 15

# Game states
STATE_MENU = 0
STATE_PLAYING = 1
STATE_PAUSED = 2
STATE_GAME_OVER = 3

# Animation settings
SPRITE_FRAME_SIZE = 64  # Size of each sprite frame in pixels
ANIMATION_SPEED = 0.15  # Animation speed (frames advanced per update)
