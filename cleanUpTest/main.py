"""

@author: Antoine, Mitsou

Copyright (C) 2019,

"""

import pygame
from constants import *
from character import *
from maps import *
 #Initializing pygame

pygame.init()
clock = pygame.time.Clock()

mapInit()
block = blockInit()

start = grid[0][0]
end = grid[cols-1][rows-1]

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
game = True

# Initializing the player
Player1 = Player("Gyxius", 1)
Monster1 = Monster("Greencreeper",2)

#Setting the sprite for the player
Player1.set_sprite('Sprites/002.png')
Monster1.set_sprite('Sprites/004.png')

#selecting one character sprite within the image 002.png
Player1.set_crop_image(Player1.image,(96,0,32,32))
Monster1.set_crop_image(Monster1.image,(96,0,32,32))
pygame.key.set_repeat(1,50)

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:   
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                Player1.position = 2
                Player1.Fx += move
                if (Player1.get_Frect().collidelist(block)) != -1:
                    Player1.Fx = Player1.posx
                else:
                    Player1.posx = Player1.Fx 
            if keys[pygame.K_LEFT]:
                Player1.position = 1
                Player1.Fx -= move
                if (Player1.get_Frect().collidelist(block)) != -1:
                    Player1.Fx = Player1.posx
                else:
                    Player1.posx = Player1.Fx 
            if keys[pygame.K_UP]:
                Player1.position = 3
                Player1.Fy -= move
                if (Player1.get_Frect().collidelist(block)) != -1:
                    Player1.Fy = Player1.posy
                else:
                    Player1.posy = Player1.Fy 
            if keys[pygame.K_DOWN]:
                Player1.position = 0
                Player1.Fy += move
                if (Player1.get_Frect().collidelist(block)) != -1:
                    Player1.Fy = Player1.posy
                else:
                    Player1.posy = Player1.Fy
    screen.fill(WHITE)
    for column in range(cols):
        for row in range(rows):
            pygame.draw.rect(screen,(BLACK),[HEIGHT*column,HEIGHT*row,HEIGHT,HEIGHT],1)
            if(grid[column][row].wall):
                pygame.draw.rect(screen,(BLACK),[HEIGHT*column,HEIGHT*row,HEIGHT,HEIGHT])
    screen.blit(Player1.get_crop_image(),(Player1.getposx(),Player1.getposy()))
    screen.blit(Monster1.get_crop_image(),(Monster1.getposx(),Monster1.getposy()))
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()


