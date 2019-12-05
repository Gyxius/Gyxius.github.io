""" This file contains the superclass character and the subclasses monsters and players
"""
import pygame

class Character(object):
    """ Basis for the players and all NPC characters """
    def __init__(self, id_character, sprite):
        """ Each character has a sprite and a unique id number """
        self.id = id_character
        self.sprite = sprite
        self.posx = 300 # We are assuming that the spawning is on positon (300,300)
        self.posy = 300
        self.life = 100
        
class Player(Character):
    """ The class contains all the methods and attributes for the player """
    def __init__(self, pseudo, id_character, sprite):
        Character.__init__(self, id_character, sprite)
        self.pseudo = pseudo

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
