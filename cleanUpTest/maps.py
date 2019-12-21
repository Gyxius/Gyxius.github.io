from random import random
from constants import *


class maps():

    def __init__(self,col,row):
        self.f = 0
        self.g = 0
        self.h = 0
        self.posx = 0
        self.posy = 0
        self.col = col
        self.row = row
        self.neighbors = []
        self.wall = False
        self.optimal = 0

        # Setting random walls(change value between 0 to 1)
        if(random()<0.3):
            self.wall=True

    def draw(self,color):
       pygame.draw.rect(screen,(color),[WIDTH*self.col,HEIGHT*self.row,WIDTH,HEIGHT])
    

    def addNeighbors(self,cell):
        i = self.col
        j = self.row
        if i < cols-1:
            self.neighbors.append(cell[i+1][j])
        if i > 0 :
            self.neighbors.append(cell[i-1][j])
        if j < rows-1:
            self.neighbors.append(cell[i][j+1])
        if j > 0:
            self.neighbors.append(cell[i][j-1])

def mapInit():
    # Initialise each cells
    for column in range(cols):
        grid.append([])
        for row in range(rows):
            grid[column].append(maps(column,row))

    # Adding neighbors
    for column in range(cols):
        for row in range(rows):
            grid[column][row].addNeighbors(grid)

def blockInit():
    blockList = []
    for column in range(cols):
        for row in range(rows):
            if (grid[column][row].wall)==True:
                x=int(WIDTH*grid[column][row].col)
                y=int(HEIGHT*grid[column][row].row)
                blockList.append(pygame.Rect((x,y,WIDTH,HEIGHT)))

    return blockList
