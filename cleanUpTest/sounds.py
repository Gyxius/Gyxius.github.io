import pygame
pygame.mixer.init(22050, -16, 2, 1024)
hit_sound = pygame.mixer.Sound("Sounds/HitSlice.ogg")
death_sound = pygame.mixer.Sound("Sounds/dead.ogg")
intro_sound = pygame.mixer.music.load("Sounds/Intro.ogg")
