
# -*- coding: utf-8 -*-
"""

@author: Antoine

Copyright (C) 2019,

Created on 09/13/2019

"""
import pygame
from maps import*

def loginTest():


    log = maps("log")
    logg = maps("logg")
    button = pygame.image.load("maps/connexion.png")
    font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
    prompt = font.render('how are you called ? : ', True, (0,0,0))
    prompt_rect = prompt.get_rect(center=(288, 320))
    user_input_value = ""
    user_input = font.render(user_input_value, True, (144,255,0))
    user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
    pygame.display.flip()
    
    small = True
    
    while small:
        
        for event in pygame.event.get():
            
            posClick = pygame.mouse.get_pos()
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 288<=posClick[0]<=512 and 352<=posClick[1]<=448:
                    small = False
            if event.type == pygame.KEYDOWN:
                
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    small = False
                    break
                elif event.key == pygame.K_BACKSPACE:
                    user_input_value = user_input_value[:-1]
                else:
                    user_input_value += event.unicode
            user_input = font.render(user_input_value, True, (144,255,0))
            user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
            
            if 288<=posClick[0]<=512 and 352<=posClick[1]<=448:
                maps.render(logg)
            else:
                maps.render(log)
            screen.blit(button, (288,352))
        screen.blit(prompt, prompt_rect)
        screen.blit(user_input, user_input_rect)
        
        pygame.display.update()

    return user_input_value 
        
        
