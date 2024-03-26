class Button():
    def __init__(self,x,y,width,height,text,color,border_color):
        self.x,self.y = x,y
        self.width,self.height = width,height
        self.text = text
        self.color = color
        self.border_color = border_color
    def getrect(self):
        return pygame.Rect((self.x,self.y,self.width,self.height))
    def draw(self):
        pygame.draw.rect(screen,self.color,getrect(self),0,5)
        pygame.draw.rect(screen,self.border_color,getrect(self),5,5)
        txt = font.render(self.txt,1,black)
        screen.blit(txt,(self.x-txt.get_width()/2,self.y-txt.get_height()/2))

class Board:
    def __init__(self,x,y,width,height,grid_size,cell_size,boxes,listpos):
        self.x,self.y = x,y
        self.width,self.height = width,height
        self.grid_size = grid_size
        self.cell_size = cell_size
        boxn = 1
        self.list = []
        for i in range(4):
            self.list.append(list(listpos[i*4:i*4+4]))
        if boxes == 1:
            box1 = None
        elif boxes == 2:
            box1 = None
            box2 = None
        else:
            box1 = None
            box2 = None
            box3 = None

    def getrect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)

    def draw(self):
        pygame.draw.rect(screen,"white",getrect(self))
        for i in range(1,self.grid_size):
            #horizontal line
            pygame.draw.line(screen,"black",(self.x,i * self.cell_size + self.y),(self.x+self.width,i * self.cell_size + self.y))
            #vertical line
            pygame.draw.line(screen,"black",(i * self.cell_size + self.x,self.y),(i * self.cell_size + self.x,self.y+self.height))
        for i in self.list:
            for j in self.list[i]:
                if j==1:
                    if boxn == 1:
                        box1 = pygame.Rect((self.x+j*100,self.y+i*100,self.cell_size,self.cell_size))
                        pygame.draw.rect(screen,"red",box1)
                        boxn += 1
                    elif boxn == 2:
                        box2 = pygame.Rect((self.x+j*100,self.y+i*100,self.cell_size,self.cell_size))
                        pygame.draw.rect(screen,"red",box2)
                        boxn += 1
                    else:
                        box3 = pygame.Rect((self.x+j*100,self.y+i*100,self.cell_size,self.cell_size))
                        pygame.draw.rect(screen,"red",box3)


#O resto ainda não importa

class Box:
    def __init__(self,x,y,width,height):
        self.x,self.y = x,y
        self.width,self.height = width,height
        self.dir = direction
    def getrect(self):
        return pygame.Rect((self.x,self.y,self.width,self.height))
    def draw(self):
        pass

    def collide(self,other):
        if pygame.Rect.colliderect(getrect(self),getrect(other)):
            if getrect(self).x < getrect(other).x:
                movement_right = False
            if getrect(self).x > getrect(other).x:
                movement_left = False
            if getrect(self).y < getrect(other).y:
                movement_down = False
            if getrect(self).y > getrect(other).y:
                movement_up = False
    def handle_movement(self):
        if movement_left == True: 
            getrect(self).x -= 1
        if movement_right == True: 
            getrect(self).x += 1
        if movement_up == True:
            getrect(self).y -= 1
        if movement_down == True:
            getrect(self).y += 1

class Obstacle(Box):
    pass
