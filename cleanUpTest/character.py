""" This file contains the superclass character and the subclasses monsters and players
"""
import pygame

class Character(object):
    """ Basis for the players and all NPC characters """
    def __init__(self, id_character):
        """ Each character has a sprite and a unique id number """
        self.id = id_character
        self.posx = 0
        self.posy = 0
        self.life = 100
        self.Fx = 0
        self.Fy = 0
        self.position = 0 # it is the initial position of the sprite with 0 being bottom, 1 left, 2 right, and 3 top
        
    def set_sprite(self,image):
        """ The method takes the link such as '002.png' and loads it """
        self.image = pygame.image.load(image)

    def set_crop_image(self,image,rect = (0,0,32,32)):
        """ the method takes a rectangle by default (0,128,32,32), gets the sprite in the form
        of a double list [x][y] and use the crop image """
        tempo2 = self.getsprite(rect)
        tempo = tempo2[self.position][0]    # [0][0] is bottom, [1][0]is left etc.
        self.crop_image = self.image.subsurface(tempo)
    

    def get_crop_image(self):
        return self.crop_image
    
    def getposx(self):
        return self.posx
    
    def getposy(self):
        return self.posy

    def getsprite(self,rect00,size = 32):
        """ each sprite contains 8 characters, we just take one character and blit the approriate
        sprite according to the character movement """
        cropdown = (rect00,(rect00[0] + size,rect00[1],rect00[2],rect00[3]),(rect00[0] + 2*size,rect00[1],rect00[2],rect00[3]))
        cropleft = ((rect00[0],rect00[1] + size ,rect00[2],rect00[3]),(rect00[0] + size,rect00[1] + size ,rect00[2],rect00[3]),(rect00[0] + 2*size,rect00[1] + size,rect00[2],rect00[3]))
        cropright = ((rect00[0],rect00[1] + 2*size ,rect00[2],rect00[3]),(rect00[0] + size,rect00[1] + 2*size ,rect00[2],rect00[3]),(rect00[0] + 2*size,rect00[1] + 2*size,rect00[2],rect00[3]))
        cropup = ((rect00[0],rect00[1] + 3*size ,rect00[2],rect00[3]),(rect00[0] + size,rect00[1] + 3*size ,rect00[2],rect00[3]),(rect00[0] + 2*size,rect00[1] + 3*size,rect00[2],rect00[3]))
        crop = (cropdown,cropleft,cropright,cropup)
        return crop

    def get_rect(self):
        return pygame.Rect(self.posx,self.posy,32,32)
    def get_Frect(self):
        return pygame.Rect(self.Fx,self.Fy,32,32)
    
    
class Player(Character):
    """ The class contains all the methods and attributes for the player """
    def __init__(self, pseudo, id_character):
        Character.__init__(self, id_character)
        self.pseudo = pseudo
        
class Monster(Character):
    """ The class contains all the methods and attributes for the player """
    def __init__(self, pseudo, id_character):
        Character.__init__(self, id_character)
        self.pseudo = pseudo
