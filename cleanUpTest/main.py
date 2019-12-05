"""

@author: Antoine, Mitsou

Copyright (C) 2019,

"""

import pygame
from constants import *

# Initializing pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
game = True

# Initializing the player
Gyxius = Player("Gyxius", 1, "test_sprite")

while game:

    screen.fill(WHITE)
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()


