""" THIS FILES CONTAINS ALL THE CONSTANTS FOR THE GAME
"""

# Related to the screen

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640

# Colors

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,128,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
GRAY = (128,128,128)
LIGHT_BLUE = (21,223,223)

# FPS

FPS = 10


# Grid

WIDTH = HEIGHT = move = 32
cols = int(SCREEN_WIDTH/WIDTH)
rows = int(SCREEN_HEIGHT/HEIGHT)
grid = []


# How many monsters we want to create

LEVEL = 1

MONSTERS_STILL_NUMBER = 1
MONSTERS_MOVING_NUMBER = 5
