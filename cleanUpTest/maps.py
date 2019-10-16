import pygame
from setting import*
from collisionBlocks import*

class maps():
    
    
    def __init__(self,background):
        self.name = background
        self.background = pygame.image.load("maps/"+background+".png").convert()
        self.posx= 0
        self.posy= 0
        
    def render(self):
        screen.blit(self.background, (self.posx, self.posy))

    def set_posx(self,number):
        self.posx -= number
    def set_posy(self,number):
        self.posy -= number
        
    def get_background(self):
        return self.name
    def set_background(self,newBack):
        self.name = newBack
        self.background = pygame.image.load("maps/"+newBack+".png")

    def get_blocks(self):
        return listes(self.name)


class village():

    def __init__(self,boss,maps, posx, posy):
        self.boss = boss
        self.maps = maps
        self.rect = (posx-(32*5),posy-(32*3),32*11,32*7)
        #self.money = money
        #self.people = people

    def get_position(self):
        return (self.posx, self.posy)
    def get_rect(self):
        return self.rect
    def show(self):
        pygame.draw.rect(self.maps,(255,0,0),self.rect)
        
