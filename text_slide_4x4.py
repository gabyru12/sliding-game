import pygame
import sys

pygame.init()

width = 500
height = 700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("slide game")
font = pygame.font.SysFont(None,40)

def game():
    run = True
    game_screen_rect = pygame.Rect(width/2-400/2,250,400,400)
    CELL_SIZE = 100
    GRID_SIZE = 4
    clock = pygame.time.Clock()
    red_rect = pygame.Rect((width/2-400/2,250,100,100))
    speed = 1
    movement_left,movement_right,movement_up,movement_down = False,False,False,False
    direction = ["left","right","up","down"]
    while run:
        screen.fill("light blue")
        clock.tick(1800)
        game_screen = pygame.draw.rect(screen,"white",game_screen_rect,0,0)
        red = pygame.draw.rect(screen,"red",red_rect)
        pygame.draw.rect(screen,"white",red_rect,5)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        main_menu()
                    if event.key == pygame.K_a:
                        movement_left = True
                    if event.key == pygame.K_d:
                        movement_right = True
                    if event.key == pygame.K_w:
                        movement_up = True
                    if event.key == pygame.K_s:
                        movement_down = True
        #horizontal lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(screen, "black", (50, 250+i * CELL_SIZE), (width-50, 250+i * CELL_SIZE))
        #vertical lines
        for j in range(1, GRID_SIZE):
            pygame.draw.line(screen, "black", (50+j * CELL_SIZE, 250), (50+j * CELL_SIZE, height-50))
        
        if red_rect.x-speed < game_screen_rect.x:
            movement_left = False
        if red_rect.x+100+speed > game_screen_rect.x+400:
            movement_right = False
        if red_rect.y-speed < game_screen_rect.y:
            movement_up = False
        if red_rect.y+100+speed > game_screen_rect.y+400:
            movement_down = False
        #se A e D ou W e S forem clicadas ele vai ficar num loop 1-1 = 0 e ficar parado horizontal ou verticalmente
        if movement_left == True: 
            red_rect.x -= speed
        if movement_right == True: 
            red_rect.x += speed
        if movement_up == True:
            red_rect.y -= speed
        if movement_down == True:
            red_rect.y += speed

        pygame.display.update()

game()
