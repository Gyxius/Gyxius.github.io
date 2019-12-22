"""

@author: Antoine, Mitsou

Copyright (C) 2019,

"""

import pygame
from constants import *
from character import *
from maps import *
import random
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

#Setting the sprite for the player
Player1.set_sprite('Sprites/002.png')

#selecting one character sprite within the image 002.png
Player1.set_crop_image(Player1.image,(96,0,32,32))

#Initializing the monsters
Monsters = {}
damaged_monsters_id = []
for i in range(MONSTERS_STILL_NUMBER):
    Monsters[i] = Monster_still("Easy",i)
    Monsters[i].set_sprite('Sprites/004.png')
    Monsters[i].set_crop_image(Monsters[i].image,(0,0,32,32))

for j in range(i+1,MONSTERS_MOVING_NUMBER + i + 1):
    Monsters[j] = Monster_moving("Medium",i)
    Monsters[j].set_sprite('Sprites/004.png')
    Monsters[j].set_crop_image(Monsters[j].image,(96,0,32,32))


pygame.key.set_repeat(1,50)

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:   
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_e:
                damaged_monsters_id = Player1.attack(Monsters,damaged_monsters_id)
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
            Player1.set_crop_image(Player1.image,(96,0,32,32))
    screen.fill(WHITE)
    for column in range(cols):
        for row in range(rows):
            pygame.draw.rect(screen,(BLACK),[HEIGHT*column,HEIGHT*row,HEIGHT,HEIGHT],1)
            if(grid[column][row].wall):
                pygame.draw.rect(screen,(BLACK),[HEIGHT*column,HEIGHT*row,HEIGHT,HEIGHT])
    screen.blit(Player1.get_crop_image(),(Player1.getposx(),Player1.getposy()))

    
    # Blitting the monsters and updating the monsters info
    for i in range(MONSTERS_STILL_NUMBER):
        if i in damaged_monsters_id:
            Monsters[i].life -= 20
        screen.blit(Monsters[i].get_crop_image(),(Monsters[i].getposx(),Monsters[i].getposy()))
    for j in range(i+1,MONSTERS_MOVING_NUMBER + i + 1):
        random.seed()
        if j in damaged_monsters_id:
            Monsters[j].life -= 20
        # blitting the healthbar
        Monsters[j].draw_stats(screen)
        
        # How to make the monster move randomly with a probability for each movement
        population = [-1,0,1]
        weight = [0.005,0.99,0.005]
        randomx = random.choices(population,weight)[0]
        randomy = random.choices(population,weight)[0]
        Monsters[j].posx += 32*randomx
        Monsters[j].posy += 32*randomy

        screen.blit(Monsters[j].get_crop_image(),(Monsters[j].getposx(),Monsters[j].getposy()))

    damaged_monsters_id = []
    
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()


