import pygame
import sys

pygame.init()

width = 500
height = 700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("slide game")
font = pygame.font.SysFont(None,40)

def play():
    run = True
    while run:
        click = False
        mx,my = pygame.mouse.get_pos()
        screen.fill("light blue")

        play_rec = pygame.draw.rect(screen,"grey",(width/2-50,height/2-25,100,50), 0,30)
        play_border = pygame.draw.rect(screen,"black",(width/2-50,height/2-25,100,50), 5, 30)
        play = font.render("Play",1,"black")
        screen.blit(play, (width/2 - play.get_width()/2,height/2 - play.get_height()/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if play_rec.collidepoint(mx,my):
            play_border = pygame.draw.rect(screen,"yellow",(width/2-50,height/2-25,100,50), 5, 30)
            if click == True:
                run = False
                main_menu()

        pygame.display.update()

def main_menu():
    run = True
    while run:
        screen.fill("light blue") 
        click = False
        mx,my = pygame.mouse.get_pos()
        
        title_rec = pygame.draw.rect(screen,"grey",(0,100-30,500,50), 0, 0)
        title_border = pygame.draw.rect(screen,"black",(-5,100-30,510,50), 5, 0)
        title = font.render("Main menu",1,"black")
        screen.blit(title, (width/2 - title.get_width()/2,70+25 - title.get_height()/2))
        
        start_rec = pygame.draw.rect(screen,"grey",(width/2-50,200,100,50), 0, 0)
        start_border = pygame.draw.rect(screen,"black",(width/2-50,200,100,50), 5, 5)
        start = font.render("Start",1,"black")
        screen.blit(start, (width/2 - start.get_width()/2,200+25 - start.get_height()/2))
        
        exit_rec = pygame.draw.rect(screen,"grey",(width/2-50,300,100,50), 0, 0)
        exit_border = pygame.draw.rect(screen,"black",(width/2-50,300,100,50), 5, 5)
        _exit = font.render("Exit",1,"black")
        screen.blit(_exit, (width/2 - _exit.get_width()/2,300+25 - start.get_height()/2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if start_rec.collidepoint(mx,my):
            start_border = pygame.draw.rect(screen,"yellow",(width/2-50,200,100,50), 5, 5)
            if click == True:
                run = False
                game()
        if exit_rec.collidepoint(mx,my):
            exit_border = pygame.draw.rect(screen,"yellow",(width/2-50,300,100,50), 5, 5)
            if click == True:
                run = False
                quit()
                exit()
                
        pygame.display.update()

def game():
    run = True
    clock = pygame.time.Clock()
    red_rect = pygame.Rect((100,100,50,50))
    speed = 1
    movement_right,movement_down = False,False
    while run:
        screen.fill("light blue")
        clock.tick(1800)
        red = pygame.draw.rect(screen,"red",red_rect)
        yellow = pygame.draw.rect(screen, "yellow", (400,100,50,50))
        yellow_border = pygame.draw.rect(screen, "light blue", (400,100,50,50),5,0)
        screen.blit(font.render("Use W and D to move",1,"black"),(50,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    main_menu()
                if event.key == pygame.K_d:
                    movement_right = True
                if event.key == pygame.K_s:
                    movement_down = True
        if pygame.Rect.colliderect(red,yellow_border):
            movement_right = False
        if movement_right:
            red_rect.x += speed
        if movement_down:
            red_rect.y += speed
        pygame.display.update()

play()
