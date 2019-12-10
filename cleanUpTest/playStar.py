""" 

Still work to be done, same bug
(can't repeat the astar function otherwise it freezes the screen)

Download the file and press o to test the function
You can move the player around before pressing o

"""

import pygame
from random import random


pygame.init()

## CONSTANTES
WIDTH = 800
HEIGHT = 640

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

i=0
cols=50
rows=50

WSIZE = WIDTH/cols
HSIZE = HEIGHT/rows
grid = []

# Heuristics = distance between current position to the target's position
def heuristics(a,b):
    dist = abs(a.col-b.col)+ abs(a.row-b.row)
    return int(dist)
    
class Character():
    
    def __init__(self,x,y):
        self.posx = x
        self.posy = y
        self.w = WSIZE
        self.h = HSIZE
        
##        not working ????
##        self.col = int(self.posx/self.w)
##        self.row = int(self.posy/self.h)
        
        self.vel = 2
        

    def get_rect(self):
        return pygame.Rect(self.posx,self.posy,self.w,self.h)
    
    
    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,0),(self.posx,self.posy,self.w,self.h))
            

    def aStar(self,grid,end):

        start = grid[int(self.posx/self.w)][int(self.posy/self.h)]
        openSet = []
        closedSet = []
        start.wall=False
        end.wall=False
        
        openSet.append(start)
        #if openSet is not empty
        while len(openSet) > 0:

            # the best road is the one with the lowest f value
            best = 0
            for i in range(len(openSet)):
                if openSet[i].f < openSet[best].f:
                    best = i
            current = openSet[best]
            
            openSet.remove(current)
            neighbors = current.neighbors
            
            
            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                # check if each neighbor is not inside closedSet and not a wall
                if (neighbor not in closedSet) and not(neighbor.wall):
                    # g represent the distance between the current position and the starting position
                    # +1 because each position moves by one cell at the time so the distance increase only by 1
                    tempG = current.g+1
                    if neighbor in openSet:
                        if tempG < neighbor.g:
                            neighbor.g = tempG
                    else :
                        neighbor.g = tempG
                        openSet.append(neighbor)
                        
                    neighbor.h = heuristics(neighbor,end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.optimal = current
                    
            closedSet.append(current)

    ##        for item in openSet:
    ##            item.draw(GREEN)
    ##            
    ##        for item in closedSet:
    ##            item.draw(RED)
                

            # arrived to the target
            if current == end:
                path = []
                temp = current
                path.append(temp)
                # as long as the current best position has a previous position
                # store the best path into path
                while(temp.optimal):
                    path.append(temp.optimal)
                    temp = temp.optimal
                    
                return path
                break

            

class noeux:
    def __init__(self,col,row):
        self.f = 0
        self.g = 0
        self.h = 0
        self.col = col
        self.row = row
        self.neighbors = []
        self.wall=False
        self.optimal = 0

        # Setting random walls(change value between 0 to 1)
        if(random()<0.2):
            self.wall=True

            
    def draw(self,color):
        pygame.draw.rect(screen,(color),[WSIZE*self.col,HSIZE*self.row,WSIZE,HSIZE])
        

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

        # Checking diagonals
##        if i > 0 and j > 0 :
##            self.neighbors.append(cell[i-1][j-1])
##        if i < cols-1 and j > 0 :
##            self.neighbors.append(cell[i+1][j-1])
##        if i < cols-1 and j < rows-1 :
##            self.neighbors.append(cell[i+1][j+1])
##        if i > 0 and j < rows-1 :
##            self.neighbors.append(cell[i-1][j+1])



# Setting the map
for column in range(cols):
    grid.append([])
    for row in range(rows):
        grid[column].append(noeux(column,row))

# Adding neighbors
for column in range(cols):
    for row in range(rows):
        grid[column][row].addNeighbors(grid)


        

    

##Starting point
start = grid[0][0]
##Objectif point
end = grid[cols-1][rows-1]

a=0

clock = pygame.time.Clock() 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.flip()
display=True
player = Character(0,0)
pygame.key.set_repeat(1,50)
screen.fill(WHITE)
while display:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            display = False

        if event.type == pygame.K_ESCAPE:
            display = False

            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.posx += player.vel
        if keys[pygame.K_LEFT]:
            player.posx -= player.vel
        if keys[pygame.K_UP]:
            player.posy -= player.vel
        if keys[pygame.K_DOWN]:
            player.posy += player.vel
            
        if keys[pygame.K_o]:
            pygame.time.wait(1000)
            nice = player.aStar(grid,end)
            

    screen.fill(WHITE)
    # check if the variable 'nice' exist
    if 'nice' in locals():
        if nice is not None:
            for item in nice:
                item.draw(BLUE)


    player.draw(screen)
    
    for column in range(cols):
        for row in range(rows):
            pygame.draw.rect(screen,(BLACK),[WSIZE*column,HSIZE*row,WSIZE,HSIZE],1)
            if(grid[column][row].wall):
                pygame.draw.rect(screen,(BLACK),[WSIZE*column,HSIZE*row,WSIZE,HSIZE])

    pygame.display.update()
    
    clock.tick(30)


pygame.quit()
