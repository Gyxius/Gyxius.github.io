from sprite import*
from maps import*
from collisionBlocks import*
        

class Player():
    
    def __init__(self, pseudo, sprite):
        font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
        
        self.pseudo = pseudo
        self.sprite = sprite
        self.posx = 32
        self.posy = 32
        self.Fx = 32 
        self.Fy = 32
        self.move = 16
        self.surface = (0,0,32,32)
        self.pseudoRect = font.render(self.pseudo, True, (144,255,0))
        self.life = 100
        self.village = 0
        
    def set_move(self,move):
        self.move = move
    def get_pos(self):
        return (self.posx,self.posy)
    def get_rect(self):
        return pygame.Rect(self.posx,self.posy,32,32)
    def get_Frect(self):
        return pygame.Rect(self.Fx,self.Fy,32,32)
    def get_life(self):
        return self.life
    def set_life(self,life):
        self.life += life
    

    def getEvent(self,sheet,ahah,blockList):
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:   ##Croix rouge
                game = False
            
                
            if event.type== pygame.KEYDOWN:    ##Lorsqu'on appuie sur une touche
                if event.key == pygame.K_LEFT:   ##LEFT
                    
                    self.Fx -= self.move
                    if (self.get_Frect().collidelist(blockList)) != -1:# -1 means no collision 
                        self.posx += 0
                        self.Fx = self.posx
                    else:
                        self.posx -= self.move
                        for block in blockList:
                            block[0]= block[0]+16
                        ahah.set_posx(-16)
                    self.surface = sheet.getSprite(1)
                    
                if event.key == pygame.K_RIGHT:  ##RIGHT
                    self.Fx += self.move
                    if (self.get_Frect().collidelist(blockList)) != -1:
                        self.posx += 0
                        self.Fx = self.posx
                    else:
                        self.posx += self.move
                        for block in blockList:
                            block[0]= block[0]-16
                        ahah.set_posx(16)
                    self.surface= sheet.getSprite(2)
                if event.key == pygame.K_UP:     ##UP
                    self.Fy -= self.move
                    if (self.get_Frect().collidelist(blockList)) != -1:
                        self.posy += 0
                        self.Fy = self.posy
                        #if (self.get_Frect().collidelist(houses)) != -1:
                            #print('still not working')
                    else:
                        self.posy -= self.move
                        for block in blockList:
                            block[1]= block[1]+16
                        ahah.set_posy(-16)
                    self.surface=sheet.getSprite(3)
                if event.key == pygame.K_DOWN:   ##DOWN
                    self.Fy += self.move
                    if (self.get_Frect().collidelist(blockList)) != -1:
                        self.posy += 0
                        self.Fy = self.posy
                    else:
                        self.posy += self.move
                        for block in blockList:
                            block[1]= block[1]-16
                        ahah.set_posy(16)
                    self.surface=sheet.getSprite(0)
                    
##                if event.key == pygame.K_g:
##                    self.set_life(-10)
##                    
##                if event.key == pygame.K_h:
##                    self.set_life(10)
                    
                if event.key == pygame.K_t:
                    self.village = village(self.pseudo,ahah,self.posx,self.posy) 

    def draw(self,screen):
        
        if(self.village!=0):
            pygame.draw.rect(screen,(255,0,0),self.village.rect)

        lolol = self.get_pos()
        screen.blit(self.pseudoRect,self.pseudoRect.get_rect(center=(lolol[0]+16,lolol[1]-16)))
        screen.blit(self.sprite.subsurface(self.surface),self.get_pos())
        
                    
                    
##        if self.get_life()>84:
##            pygame.draw.rect(screen,(0,255,0),(32,576,6*32,32))
##        elif self.get_life() <= 0:
##            pygame.draw.rect(screen,(255,0,0),(32,576,0*32,32))
##            self.set_move(0)
##        elif self.get_life() <= 16:
##            pygame.draw.rect(screen,(255,0,0),(32,576,1*32,32))    
##        elif self.get_life() <= 34:
##            pygame.draw.rect(screen,(255,0,0),(32,576,2*32,32))
##        elif self.get_life() <= 50:
##            pygame.draw.rect(screen,(255,140,0),(32,576,3*32,32))
##        elif self.get_life() <= 66:
##            pygame.draw.rect(screen,(255,140,0),(32,576,4*32,32))
##        elif self.get_life()<=84:
##            pygame.draw.rect(screen,(0,255,0),(32,576,5*32,32))

