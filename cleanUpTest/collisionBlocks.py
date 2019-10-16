import pygame
from maps import*
import os

def listes(filename):

    blockList = []
    if os.path.isfile('maps/'+filename+'.txt'):
        
        file = open("maps/"+filename+".txt","r")
        
        for line in file:
            lol = line.split()
            lolol = (int(lol[0]),int(lol[1]),int(lol[2]),int(lol[3]))
            
            blockList.append(pygame.Rect(lolol))  
        file.close()

        return blockList
    else:
        return blockList



def mapping():
    
    file = open("maps/mapping.txt","r")
    carte = []
    for line in file:
        lol = line.split()
        lolol = (int(lol[0]),int(lol[1]),int(lol[2]),int(lol[3]))
            
        carte.append(pygame.Rect(lolol))
    file.close()
    return carte
