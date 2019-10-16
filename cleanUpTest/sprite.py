import pygame

class spritesheet():
    def __init__(self,filename,cols,rows):
        self.sheet = pygame.image.load(filename)
        self.cols = cols
        self.rows = rows
        self.totalCells = cols*rows

        self.rect = self.sheet.get_rect()
        self.w = self.cellWidth = self.rect.width/cols
        self.h = self.cellHeight = self.rect.height/rows

    def getSprite(self,move):
        self.move = move
        down = (0,self.h*0,self.w,self.h)
        left =(0,self.h*1,self.w,self.h)
        right =(0,self.h*2,self.w,self.h)
        up =(0,self.h*3,self.w,self.h)

        if (self.move==0):
            return down
        if (self.move==1):
            return left
        if (self.move==2):
            return right
        if (self.move==3):
            return up
