# -*- coding: utf-8 -*-

"""

@author: Antoine

Copyright (C) 2019,

Created on 09/06/2019

"""

## Création de fichier pour lister les coordonnées de blocks
## Version test

import pygame
from pprint import pprint

pygame.init()

## CONSTANTES
WIDTH = 800
HEIGHT = 640
SIZE = 32
RED = (255,0,0, 0.5)
i=0
#############

grid = []
dict_grid = {}
for row in range(20):
    grid.append([])
    for column in range(25):
        grid[row].append(0)

        
screen = pygame.display.set_mode((WIDTH,HEIGHT))
      
background = pygame.image.load("maps/log.png") ### Map à définir
screen.blit(background, (0, 0))

#############
file = open("log.txt","w") ### Fichier txt à définir


Run = True
test = True

while test:
    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    Run = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Récupère la position du click
                posClick = pygame.mouse.get_pos()
                # Transforme les coordonées pixel en coordonées grille
                column = posClick[0] // 32
                row = posClick[1] // 32
                # Set that location to one
                grid[row][column] = 1
                # Enregistre la case dans un dictionnaire
                dict_grid[i] = column*SIZE,row*SIZE,SIZE,SIZE
                # Ecrit sur le fichier texte
                a = str(column*SIZE)
                b = str(row*SIZE)
                c = str(SIZE)
                d = str(SIZE)
                temp = a + ' ' + b+ ' ' + c+ ' ' + d
                pprint(temp)
                file.write(temp +'\n')
                # Colorie en rouge la case cliqué
                pygame.draw.rect(screen,RED,(column*SIZE,row*SIZE,SIZE,SIZE))
                i += 1
                #print("Click ", posClick, "Grid coordinates: ", row, column)

       
        pygame.display.update()
    
    file.close()
    pprint(dict_grid)
    test = False
pygame.quit()
