
# -*- coding: utf-8 -*-
"""

@author: Antoine

Copyright (C) 2019,

Created on 09/04/2019

"""
import pygame


from characters import*
from sprite import*
from maps import*
from collisionBlocks import*
from log import*
from pprint import pprint

##Initialise pygame
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,640))

pseudo = loginTest()

new_sheet = spritesheet("sprites/002.png",12,8)

new_player = Player(pseudo,new_sheet.sheet)
ahah = maps("new")
blockList = ahah.get_blocks()
pygame.display.flip()


pygame.key.set_repeat(1,50)
game = True
while game:

    new_player.getEvent(new_sheet,ahah,blockList)
    screen.fill((0,0,0)) 
    maps.render(ahah)

#######################################################

    new_player.draw(screen)
    #screen.blit(new_player.sprite.subsurface(surface),new_player.get_pos())


    pygame.display.update()
    
    clock.tick(10)

##End pygame              
pygame.quit()
