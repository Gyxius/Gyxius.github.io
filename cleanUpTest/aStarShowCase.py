import pygame
from random import random


pygame.init()

## CONSTANTES
WIDTH = 1024
HEIGHT = 640

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

i=0
cols=WIDTH//32
rows=HEIGHT//32

WSIZE = WIDTH/cols
HSIZE = HEIGHT/rows
grid = []


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
        if(random()<0.3):
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



# Setting the map
for column in range(cols):
    grid.append([])
    for row in range(rows):
        grid[column].append(noeux(column,row))

# Adding neighbors
for column in range(cols):
    for row in range(rows):
        grid[column][row].addNeighbors(grid)


# Heuristics = distance between current position to the target's position
def heuristics(a,b):
    dist = abs(a.col-b.col)+ abs(a.row-b.row)
    return int(dist)

def aStar(start,end):

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

        for item in openSet:
            item.draw(GREEN)
            
        for item in closedSet:
            item.draw(RED)
            

        path = []
        temp = current
        path.append(temp)
        # as long as the current best position has a previous position
        # store the best path into path
        while(temp.optimal):
            path.append(temp.optimal)
            temp = temp.optimal
        for item in path:
            item.draw(BLUE)

        # arrived to the target
        if current == end:
            print("Arrived!")
            break
        
        

        pygame.display.update()

    

##Starting point
start = grid[0][rows-1]
##Objectif point
end = grid[cols-1][0]


clock = pygame.time.Clock() 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.flip()
display=True

screen.fill(WHITE)

while display:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    display = False
                if event.key == pygame.K_UP:
                    aStar(start,end)
                
    
    

                    
    for column in range(cols):
        for row in range(rows):
            pygame.draw.rect(screen,(BLACK),[WSIZE*column,HSIZE*row,WSIZE,HSIZE],1)
            if(grid[column][row].wall):
                pygame.draw.rect(screen,(BLACK),[WSIZE*column,HSIZE*row,WSIZE,HSIZE])


    pygame.display.update()
    
    clock.tick(30)


pygame.quit()
