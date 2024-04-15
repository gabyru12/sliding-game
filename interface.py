import pygame
import sys
from levels import levels
from algoritmo import *

# Inicializando Pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Match The Tiles: Sliding Game")

selected_size = "5x5"

# Fonte e tamanho do texto
font = pygame.font.SysFont(None, 40)
font_lower = pygame.font.SysFont(None, 10)

def play():
    run = True
    while run:
        click = False
        mx,my = pygame.mouse.get_pos()
        screen.fill("light blue")
        rec_width,rec_height = 120,60
        play_rec = pygame.draw.rect(screen,"grey",(WIDTH/2-rec_width//2,HEIGHT/2-rec_height//2,rec_width,rec_height), 0)
        play_border = pygame.draw.rect(screen,"black",(WIDTH/2-rec_width//2,HEIGHT/2-rec_height//2,rec_width,rec_height), 5)
        play = font.render("Play",1,"black")
        screen.blit(play, (WIDTH/2 - play.get_width()/2,HEIGHT/2 - play.get_height()/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if play_rec.collidepoint(mx,my):
            play_border = pygame.draw.rect(screen,"yellow",(WIDTH/2-rec_width//2,HEIGHT/2-rec_height//2,rec_width,rec_height), 5)
            if click == True:
                run = False
                main_menu()

        pygame.display.update()

# Escolha entre criar tabuleiro ou jogar os níveis (não implementado)
def main_menu():
    run = True
    while run:
        click = False
        mx,my = pygame.mouse.get_pos()
        screen.fill("light blue")

        #Desenhar o botão "Create your board"
        rec_width,rec_height = 270,60
        board_creator_rec = pygame.draw.rect(screen,"grey",(WIDTH/2-rec_width//2,HEIGHT/3-rec_height//2,rec_width,rec_height), 0)
        board_creator_border = pygame.draw.rect(screen,"black",(WIDTH/2-rec_width//2,HEIGHT/3-rec_height//2,rec_width,rec_height), 5)
        board_creator = font.render("Create your board",1,"black")
        screen.blit(board_creator, (WIDTH/2 - board_creator.get_width()/2,HEIGHT/3 - board_creator.get_height()/2))

        # Desenhar o botão "Levels"
        levels_rec = pygame.draw.rect(screen, "grey", (WIDTH/2 - rec_width//2, HEIGHT/2 - rec_height//2, rec_width, rec_height), 0)
        levels_border = pygame.draw.rect(screen, "black", (WIDTH/2 - rec_width//2, HEIGHT/2 - rec_height//2, rec_width, rec_height), 5)
        levels_text = font.render("Levels", 1, "black")
        screen.blit(levels_text, (WIDTH/2 - levels_text.get_width()/2, HEIGHT/2 - levels_text.get_height()/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        #Verificar clique no botão "Create your board"
        if board_creator_rec.collidepoint(mx,my):
            board_creator_border = pygame.draw.rect(screen,"yellow",(WIDTH/2-rec_width//2,HEIGHT/3-rec_height//2,rec_width,rec_height), 5)
            if click == True:
                run = False
                choose_board(selected_size)

        #Verificar o clique no botão "Levels"
        if levels_rec.collidepoint((mx, my)):
            levels_border = pygame.draw.rect(screen, "yellow", (WIDTH/2 - rec_width//2, HEIGHT/2 - rec_height//2, rec_width, rec_height), 5)
            if click:
                run = False
                show_levels()

        pygame.display.update()

# Escolha entre os níveis de 1 a 30
def show_levels():
    run = True
    while run:
        screen.fill("light blue")
        
        # Desenhar os botões dos níveis
        button_width, button_height = 50, 50
        button_padding = 10
        rows, cols = 6, 5
        start_x = (WIDTH - (cols * (button_width + button_padding))) // 2
        start_y = (HEIGHT - (rows * (button_height + button_padding))) // 2
        level_number = 1
        for row in range(rows):
            for col in range(cols):
                button_rect = pygame.Rect(start_x + col * (button_width + button_padding),
                                          start_y + row * (button_height + button_padding),
                                          button_width, button_height)
                pygame.draw.rect(screen, "grey", button_rect)
                font = pygame.font.Font(None, 36)
                text = font.render(str(level_number), True, "black")
                text_rect = text.get_rect(center=button_rect.center)
                screen.blit(text, text_rect)
                level_number += 1

        # Verificar cliques nos botões dos níveis
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for row in range(rows):
                    for col in range(cols):
                        button_rect = pygame.Rect(start_x + col * (button_width + button_padding),
                                                  start_y + row * (button_height + button_padding),
                                                  button_width, button_height)
                        if button_rect.collidepoint(mx, my):
                            level_number = row * cols + col + 1
                            show_board(levels[level_number - 1])  # Chama a função show_board com o nível selecionado

        pygame.display.update()

# Mostra o tabuleiro do respetivo nível
def show_board(level):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        screen.fill("light blue")

        draw_board1(level)

        pygame.display.update()

#Desenhar tabuleiro dos "Levels"
def draw_board1(board):
    # Dividir o tamanho em linhas e colunas
    rows,cols = len(board),len(board)

    # Calcula o tamanho do tabuleiro
    board_size = 300 + 2 * (rows-1) 
    if rows == 7:
        board_size -= rows-1

    # Calcular o tamanho dos quadrados
    square_size = 300 // rows

    # Calcula a margem para centralizar o tabuleiro
    margin_x = WIDTH // 2 - board_size // 2
    margin_y = HEIGHT // 2 - board_size // 2

    # Desenhar o tabuleiro
    pygame.draw.rect(screen, "white", (margin_x, margin_y, board_size, board_size))
    for row in range(rows - 1):
        pygame.draw.line(screen, "black", (margin_x, (margin_y + (row + 1) * square_size + row * 2)), (margin_x + board_size - 1, (margin_y + (row + 1) * square_size + row * 2)), 2)
    for col in range(cols - 1):
        pygame.draw.line(screen, "black", ((margin_x + (col + 1) * square_size + col * 2), margin_y), ((margin_x + (col + 1) * square_size + col * 2), margin_y + board_size - 1), 2)

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col][0:2] == "1r":
                pygame.draw.rect(screen, "red", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))
            elif board[row][col][0:2] == "1g":
                pygame.draw.rect(screen, "green", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))
            elif board[row][col][0:2] == "1b":
                pygame.draw.rect(screen, "blue", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))
            elif board[row][col][0:2] == "2r":
                pygame.draw.rect(screen, "red", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size),2)
            elif board[row][col][0:2] == "2g":
                pygame.draw.rect(screen, "green", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size),2)
            elif board[row][col][0:2] == "2b":
                pygame.draw.rect(screen, "blue", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size),2)
            elif board[row][col] == "3":
                pygame.draw.rect(screen, "black", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))

    pygame.draw.rect(screen, "black", (margin_x-2, margin_y-2, board_size+4, board_size+4),2)

#Desenhar tabuleiro "Create your board"
def draw_board(size,board,mx,my):
    # Dividir o tamanho em linhas e colunas
    rows, cols = map(int, size.split('x'))

    # Calcula o tamanho do tabuleiro
    board_size = 300 + 2 * (rows-1) 
    if rows == 7:
        board_size -= rows-1

    # Calcular o tamanho dos quadrados
    square_size = 300 // rows

    # Calcula a margem para centralizar o tabuleiro
    margin_x = WIDTH // 2 - board_size // 2
    margin_y = 250

    fake_col_clicked = int(((mx - margin_x) / square_size))
    col_clicked = int(((mx - margin_x - fake_col_clicked * 2) / square_size))
    fake_row_clicked = int(((my - margin_y) / square_size))
    row_clicked = int(((my - margin_y - fake_row_clicked * 2) / square_size))

    # Desenhar o tabuleiro
    pygame.draw.rect(screen, "white", (margin_x, margin_y, board_size, board_size))
    for row in range(rows - 1):
        pygame.draw.line(screen, "black", (margin_x, (margin_y + (row + 1) * square_size + row * 2)), (margin_x + board_size - 1, (margin_y + (row + 1) * square_size + row * 2)), 2)
    for col in range(cols - 1):
        pygame.draw.line(screen, "black", ((margin_x + (col + 1) * square_size + col * 2), margin_y), ((margin_x + (col + 1) * square_size + col * 2), margin_y + board_size - 1), 2)

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col][0:2] == "1r":
                pygame.draw.rect(screen, "red", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))
            elif board[row][col][0:2] == "1g":
                pygame.draw.rect(screen, "green", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))
            elif board[row][col][0:2] == "1b":
                pygame.draw.rect(screen, "blue", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))
            elif board[row][col][0:2] == "2r":
                pygame.draw.rect(screen, "red", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size),2)
            elif board[row][col][0:2] == "2g":
                pygame.draw.rect(screen, "green", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size),2)
            elif board[row][col][0:2] == "2b":
                pygame.draw.rect(screen, "blue", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size),2)
            elif board[row][col] == "3":
                pygame.draw.rect(screen, "black", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))

    pygame.draw.rect(screen, "black", (margin_x-2, margin_y-2, board_size+4, board_size+4),2)

    return margin_x, margin_y, square_size, rows, cols, board_size

# Desenha a peça sem colocá-la
def draw_piece(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, piece_color,size):
    rows, cols = map(int, size.split('x'))
    board_size = 300 + 2 * (rows-1) 
    if rows == 7:
        board_size -= rows-1
    pygame.draw.rect(screen, piece_color, ((margin_x + col_clicked * (square_size + 2)), (margin_y + row_clicked * (square_size + 2)), square_size, square_size))
    pygame.draw.rect(screen, "black", (margin_x-2, margin_y-2, board_size+4, board_size+4),2)

# Desenha o winning point sem colocá-lo
def draw_winning_point(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, winning_point_color, size):
    rows, cols = map(int, size.split('x'))
    board_size = 300 + 2 * (rows-1) 
    if rows == 7:
        board_size -= rows-1
    pygame.draw.rect(screen, "black", (margin_x-2, margin_y-2, board_size+4, board_size+4),2)
    pygame.draw.rect(screen, winning_point_color, ((margin_x + col_clicked * (square_size + 2)), (margin_y + row_clicked * (square_size + 2)), square_size, square_size),2)

# Desenha o obstáculo sem colocá-lo
def draw_obstacle(screen,square_size, margin_x, margin_y, col_clicked, row_clicked,obstacle_color, size):
    rows, cols = map(int, size.split('x'))
    board_size = 300 + 2 * (rows-1) 
    if rows == 7:
        board_size -= rows-1
    pygame.draw.rect(screen, obstacle_color, ((margin_x + col_clicked * (square_size + 2)), (margin_y + row_clicked * (square_size + 2)), square_size, square_size))
    pygame.draw.rect(screen, "black", (margin_x-2, margin_y-2, board_size+4, board_size+4),2)
    
# Escolha do tamanho do tabuleiro
def choose_board(selected_size):
    run = True
    board_size = int(selected_size[0])
    board = [["0" for _ in range(board_size)]for _ in range(board_size)]
    while run:
        screen.fill("light blue")
        title_text = font.render("Escolha o tamanho do tabuleiro:", True, "black")
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))
        
        mx,my = pygame.mouse.get_pos()

        # Botões para escolher o tamanho do tabuleiro
        button_width, button_height = 100, 50
        button_y = 150
        button_x_start = WIDTH // 4

        button_5x5 = pygame.Rect(button_x_start, button_y, button_width, button_height)
        pygame.draw.rect(screen, "gray", button_5x5)
        pygame.draw.rect(screen, "black", button_5x5,2)
        text_5x5 = font.render("5x5", True, "black")
        screen.blit(text_5x5, (button_x_start + button_width // 2 - text_5x5.get_width() // 2, button_y + button_height // 2 - text_5x5.get_height() // 2))

        button_6x6 = pygame.Rect(button_x_start + button_width + 50, button_y, button_width, button_height)
        pygame.draw.rect(screen, "gray", button_6x6)
        pygame.draw.rect(screen, "black", button_6x6,2)
        text_6x6 = font.render("6x6", True, "black")
        screen.blit(text_6x6, (button_x_start + button_width + 50 + button_width // 2 - text_6x6.get_width() // 2, button_y + button_height // 2 - text_6x6.get_height() // 2))

        button_7x7 = pygame.Rect(button_x_start + 2 * (button_width + 50), button_y, button_width, button_height)
        pygame.draw.rect(screen, "gray", button_7x7)
        pygame.draw.rect(screen, "black", button_7x7,2)
        text_7x7 = font.render("7x7", True, "black")
        screen.blit(text_7x7, (button_x_start + 2 * (button_width + 50) + button_width // 2 - text_7x7.get_width() // 2, button_y + button_height // 2 - text_7x7.get_height() // 2))

        button_next = pygame.Rect(WIDTH - (button_width + 25), HEIGHT - (button_height + 25), button_width, button_height)
        pygame.draw.rect(screen, "green", button_next)
        pygame.draw.rect(screen, "black", button_next,2)
        text_next = font.render("Next", True, "black")
        screen.blit(text_next, (WIDTH - (button_width + 25) + button_width // 2 - text_next.get_width() // 2,HEIGHT - (button_height + 25) + button_height // 2 - text_next.get_height() // 2))

        if button_x_start <= mx <= button_x_start + 100 and 150 <= my <= 150 + button_height:
            pygame.draw.rect(screen, "light gray", button_5x5)
            pygame.draw.rect(screen, "black", button_5x5,2)
            screen.blit(text_5x5, (button_x_start + button_width // 2 - text_5x5.get_width() // 2, button_y + button_height // 2 - text_5x5.get_height() // 2))
        elif button_x_start + button_width + 50 <= mx <= button_x_start + button_width + 50 + button_width and 150 <= my <= 150 + button_height:
            pygame.draw.rect(screen, "light gray", button_6x6)
            pygame.draw.rect(screen, "black", button_6x6,2)
            screen.blit(text_6x6, (button_x_start + button_width + 50 + button_width // 2 - text_6x6.get_width() // 2, button_y + button_height // 2 - text_6x6.get_height() // 2))
        elif button_x_start + 2 * (button_width + 50) <= mx <= button_x_start + 2 * (button_width +50) + button_width and 150 <= my <= 150 + button_height:
            pygame.draw.rect(screen, "light gray", button_7x7)
            pygame.draw.rect(screen, "black", button_7x7,2)
            screen.blit(text_7x7, (button_x_start + 2 * (button_width + 50) + button_width // 2 - text_7x7.get_width() // 2, button_y + button_height // 2 - text_7x7.get_height() // 2))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if click:
            if button_x_start <= mx <= button_x_start + 100 and 150 <= my <= 150 + button_height:
                selected_size = "5x5"
            elif button_x_start + button_width + 50 <= mx <= button_x_start + button_width + 50 + button_width and 150 <= my <= 150 + button_height:
                selected_size = "6x6"
            elif button_x_start + 2 * (button_width + 50) <= mx <= button_x_start + 2 * (button_width +50) + button_width and 150 <= my <= 150 + button_height:
                selected_size = "7x7"
            elif WIDTH - (button_width + 25) <= mx <= WIDTH - (button_width + 25) + button_width and HEIGHT - (button_height + 25) <= my <= HEIGHT - (button_height + 25) + button_height:
                run = False
                put_pieces(selected_size)

        # Desenhar o tabuleiro
        if selected_size:
            draw_board(selected_size,board,mx,my)

        pygame.display.update()

# Escolhe a cor da peça
def select_pieces(counter):
    title_text = font.render("Position the pieces:", True, "black")
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

    button_width, button_height = 50, 50
    button_y = 150
    button_x_start = (WIDTH - 3 * button_width - 2 * 50) // 2

    button_piece_red = pygame.Rect(button_x_start, button_y, button_width, button_height)
    pygame.draw.rect(screen, "red", button_piece_red)

    button_piece_green = pygame.Rect(button_x_start + button_width + 50, button_y, button_width, button_height)
    pygame.draw.rect(screen, "green", button_piece_green)

    button_piece_blue = pygame.Rect(button_x_start + 2 * (button_width + 50), button_y, button_width, button_height)
    pygame.draw.rect(screen, "blue", button_piece_blue)

    counter_text = font.render(f"{counter}",True,"black")
    screen.blit(counter_text, (WIDTH - 50,50))

    return button_x_start, button_y, button_width, button_height

# Escolhe a cor do winning point
def select_winning_points(counter_red,counter_green,counter_blue,counter_winning_point_red,counter_winning_point_green,counter_winning_point_blue):
    title_text = font.render("Position the winning points:", True, "black")
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

    button_width, button_height = 50, 50
    button_y = 150
    button_x_start = (WIDTH - 3 * button_width - 2 * 50) // 2

    button_piece_red = pygame.Rect(button_x_start, button_y, button_width, button_height)
    pygame.draw.rect(screen, "red", button_piece_red,3)

    button_piece_green = pygame.Rect(button_x_start + button_width + 50, button_y, button_width, button_height)
    pygame.draw.rect(screen, "green", button_piece_green,3)

    button_piece_blue = pygame.Rect(button_x_start + 2 * (button_width + 50), button_y, button_width, button_height)
    pygame.draw.rect(screen, "blue", button_piece_blue,3)

    if counter_red != 0:
        counter_red_text = font.render(f"{counter_winning_point_red}/{counter_red}",True,"black")
        screen.blit(counter_red_text, (WIDTH - 50,50))
    if counter_green != 0:
        counter_green_text = font.render(f"{counter_winning_point_green}/{counter_green}",True,"black")
        screen.blit(counter_green_text, (WIDTH - 50,100))
    if counter_blue != 0:
        counter_blue_text = font.render(f"{counter_winning_point_blue}/{counter_blue}",True,"black")
        screen.blit(counter_blue_text, (WIDTH - 50,150))

# Seleciona o obstáculo
def select_obstacle():
    title_text = font.render("Position the obstacles:", True, "black")
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

    button_width, button_height = 50, 50
    button_y = 150
    button_x = WIDTH // 2 - 25

    button_obstacle = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, "black", button_obstacle)

# Cria o tabuleiro
def put_pieces(selected_size):
    run = True
    selected_piece = None
    selected_winning_point_red = False
    selected_winning_point_green = False
    selected_winning_point_blue = False
    board_lenght = int(selected_size[0])
    board = [["0" for _ in range(board_lenght)]for _ in range(board_lenght)]

    piece_color = "white"
    winning_point_color = "white"
    obstacle_color = "white"
    draw_piece_flag = True
    draw_finish_flag = False
    draw_obstacle_flag = False
    turn = True

    counter_pieces = 0
    counter_winning_points = 0
    counter_red = 0
    counter_green = 0
    counter_blue = 0
    counter_winning_point_red = 0
    counter_winning_point_green = 0
    counter_winning_point_blue = 0

    piece_positions = []
    winning_point_positions = []
    obstacle_positions = []

    while run:
        screen.fill("light blue")  # light blue color
        mx,my = pygame.mouse.get_pos()
        margin_x, margin_y, square_size, rows, cols, board_size = draw_board(selected_size,board,mx,my)
        fake_col_clicked = int(((mx - margin_x) / square_size))
        col_clicked = int(((mx - margin_x - fake_col_clicked * 2) / square_size)) # dá a coluna de onde está o cursor do rato
        fake_row_clicked = int(((my - margin_y) / square_size))
        row_clicked = int(((my - margin_y - fake_row_clicked * 2) / square_size)) # dá a fila de onde está o cursor do rato
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    choose_board(selected_size)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn:
                    click = True
                    turn = False
            elif event.type == pygame.MOUSEBUTTONUP:
                turn = True

        # Mostra página para colocar obstáculos (if True)
        if draw_obstacle_flag:
            select_obstacle()

            if click:
                if WIDTH - (100 + 25) <= mx <= WIDTH - (100 + 25) + 100 and HEIGHT - (50 + 25) <= my <= HEIGHT - (50 + 25) + 50 and draw_obstacle_flag:
                    draw_obstacle_flag = False
                    run = False
                    algorithm_page(selected_size,board)

                elif WIDTH // 2 - 25 <= mx <= WIDTH // 2 +25 and button_y <= my <= button_y + 50:
                    obstacle_color = "black"
                elif margin_x <= mx <= margin_x + board_size and margin_y <= my <= margin_y + board_size + col_clicked * 2 and obstacle_color == "black" and (row_clicked,col_clicked) not in piece_positions and (row_clicked,col_clicked) not in winning_point_positions and (row_clicked,col_clicked) not in obstacle_positions:
                    board[row_clicked][col_clicked] = "3"
                    obstacle_positions.append((row_clicked,col_clicked))

            if 0 <= col_clicked < cols and 0 <= row_clicked < rows and (row_clicked,col_clicked) not in piece_positions and (row_clicked,col_clicked) not in winning_point_positions and (row_clicked,col_clicked) not in obstacle_positions and obstacle_color != "white":        
                draw_obstacle(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, obstacle_color, selected_size)

        # Mostra página para colocar winning points (if True)
        if draw_finish_flag:
            select_winning_points(counter_red,counter_green,counter_blue,counter_winning_point_red,counter_winning_point_green,counter_winning_point_blue)
            
            if click and WIDTH - (100 + 25) <= mx <= WIDTH - (100 + 25) + 100 and HEIGHT - (50 + 25) <= my <= HEIGHT - (50 + 25) + 50 and draw_finish_flag and counter_winning_points == counter_pieces:
                    draw_finish_flag = False
                    draw_obstacle_flag = True
            # Cross
            if counter_winning_point_red == counter_red:
                pygame.draw.line(screen, "black", (button_x_start, button_y), (button_x_start + button_width, button_y + button_height), 5)
                pygame.draw.line(screen, "black", (button_x_start, button_y + button_height), (button_x_start + button_width, button_y), 5)
            elif click:
                if button_x_start <= mx <= button_x_start + button_width and button_y <= my <= button_y + button_height:
                        winning_point_color = "red"
                elif margin_x <= mx <= margin_x + board_size and margin_y <= my <= margin_y + board_size and winning_point_color == "red" and (row_clicked,col_clicked) not in piece_positions and (row_clicked,col_clicked) not in winning_point_positions:
                    if counter_winning_point_red + 1 == counter_red:
                        winning_point_color = "white"
                    counter_winning_points += 1
                    counter_winning_point_red += 1
                    board[row_clicked][col_clicked] = "2r"+f"{counter_winning_points}"
                    winning_point_positions.append((row_clicked,col_clicked))

            # Cross            
            if counter_winning_point_green == counter_green:
                pygame.draw.line(screen, "black", (button_x_start + button_width + 50, button_y), (button_x_start + button_width + 50 + button_width, button_y + button_height), 5)
                pygame.draw.line(screen, "black", (button_x_start + button_width + 50, button_y + button_height), (button_x_start + button_width + 50 + button_width, button_y), 5)
            elif click:
                if button_x_start + button_width + 50 <= mx <= button_x_start + button_width + 50 + button_width and button_y <= my <= button_y + button_height:
                    winning_point_color = "green"
                elif margin_x <= mx <= margin_x + board_size and margin_y <= my <= margin_y + board_size and winning_point_color == "green" and (row_clicked,col_clicked) not in piece_positions and (row_clicked,col_clicked) not in winning_point_positions:
                    if counter_winning_point_green + 1 == counter_green:
                        winning_point_color = "white"
                    counter_winning_points += 1
                    counter_winning_point_green += 1
                    board[row_clicked][col_clicked] = "2g"+f"{counter_winning_points}"
                    winning_point_positions.append((row_clicked,col_clicked))

            # Cross
            if counter_winning_point_blue == counter_blue:
                pygame.draw.line(screen, "black", (button_x_start + 2 * (button_width + 50), button_y), (button_x_start + 2 * (button_width + 50) + button_width, button_y + button_height), 5)
                pygame.draw.line(screen, "black", (button_x_start + 2 * (button_width + 50), button_y + button_height), (button_x_start + 2 * (button_width + 50) + button_width, button_y), 5)
            elif click:
                if button_x_start + 2 * (button_width + 50) <= mx <= button_x_start + 2 * (button_width + 50) + button_width and button_y <= my <= button_y + button_height:
                    winning_point_color = "blue"
                elif margin_x <= mx <= margin_x + board_size and margin_y <= my <= margin_y + board_size and winning_point_color == "blue" and (row_clicked,col_clicked) not in piece_positions and (row_clicked,col_clicked) not in winning_point_positions:
                    if counter_winning_point_blue + 1 == counter_blue:
                        winning_point_color = "white"
                    counter_winning_points += 1
                    counter_winning_point_blue += 1
                    board[row_clicked][col_clicked] = "2b"+f"{counter_winning_points}"
                    winning_point_positions.append((row_clicked,col_clicked))

            if counter_winning_point_red != counter_red or counter_winning_point_green != counter_green or counter_winning_point_blue != counter_blue and winning_point_color != "white":
                if 0 <= col_clicked < cols and 0 <= row_clicked < rows and (row_clicked,col_clicked) not in piece_positions and (row_clicked,col_clicked) not in winning_point_positions:        
                    draw_winning_point(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, winning_point_color, selected_size)

        # MOstra a página de colocar as peças coloridas
        if draw_piece_flag:
            button_x_start, button_y, button_width, button_height = select_pieces(counter_pieces)

            if click:
                if WIDTH - (100 + 25) <= mx <= WIDTH - (100 + 25) + 100 and HEIGHT - (50 + 25) <= my <= HEIGHT - (50 + 25) + 50 and draw_piece_flag and counter_pieces > 0:
                    draw_piece_flag = False
                    draw_finish_flag = True
                if counter_pieces != 3:
                    if button_x_start <= mx <= button_x_start + button_width and button_y <= my <= button_y + button_height:
                        piece_color = "red"
                    elif button_x_start + button_width + 50 <= mx <= button_x_start + button_width + 50 + button_width and button_y <= my <= button_y + button_height:
                        piece_color = "green"
                    elif button_x_start + 2 * (button_width + 50) <= mx <= button_x_start + 2 * (button_width + 50) + button_width and button_y <= my <= button_y + button_height:
                        piece_color = "blue"
                    if margin_x <= mx <= margin_x + board_size and margin_y <= my <= margin_y + board_size:
                        if piece_color == "red" and (row_clicked,col_clicked) not in piece_positions:
                            counter_pieces += 1
                            counter_red += 1
                            board[row_clicked][col_clicked] = "1r"+f"{counter_pieces}"
                            piece_positions.append((row_clicked,col_clicked))
                        if piece_color == "green" and (row_clicked,col_clicked) not in piece_positions:
                            counter_pieces += 1
                            counter_green += 1
                            board[row_clicked][col_clicked] = "1g"+f"{counter_pieces}"
                            piece_positions.append((row_clicked,col_clicked))
                        if piece_color == "blue" and (row_clicked,col_clicked) not in piece_positions:
                            counter_pieces += 1
                            counter_blue += 1
                            board[row_clicked][col_clicked] = "1b"+f"{counter_pieces}"
                            piece_positions.append((row_clicked,col_clicked))
            # Cross
            if counter_pieces == 3:
                pygame.draw.line(screen, "black", (button_x_start, button_y), (button_x_start + button_width, button_y + button_height), 5)
                pygame.draw.line(screen, "black", (button_x_start, button_y + button_height), (button_x_start + button_width, button_y), 5)

                pygame.draw.line(screen, "black", (button_x_start + button_width + 50, button_y), (button_x_start + button_width + 50 + button_width, button_y + button_height), 5)
                pygame.draw.line(screen, "black", (button_x_start + button_width + 50, button_y + button_height), (button_x_start + button_width + 50 + button_width, button_y), 5)

                pygame.draw.line(screen, "black", (button_x_start + 2 * (button_width + 50), button_y), (button_x_start + 2 * (button_width + 50) + button_width, button_y + button_height), 5)
                pygame.draw.line(screen, "black", (button_x_start + 2 * (button_width + 50), button_y + button_height), (button_x_start + 2 * (button_width + 50) + button_width, button_y), 5)
            else:
                if 0 <= col_clicked < cols and 0 <= row_clicked < rows and (row_clicked,col_clicked) not in piece_positions:
                    draw_piece(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, piece_color,selected_size)

        button_next = pygame.Rect(WIDTH - (100 + 25), HEIGHT - (50 + 25), 100, 50)
        pygame.draw.rect(screen, "green", button_next)
        pygame.draw.rect(screen, "black", button_next,2)
        text_next = font.render("Next", True, "black")
        screen.blit(text_next, (WIDTH - (100 + 25) + 100 // 2 - text_next.get_width() // 2,HEIGHT - (50 + 25) + 50 // 2 - text_next.get_height() // 2))
        pygame.display.update()


# Dá o número de movimentos, os movimentos usados e os diferentes estados do tabuleiro se o tabuleiro tiver solução 
def algorithm_page(selected_size,board):
    run = True
    memo.append(board)
    visited.append(board)
    counter,moves,solution_path = breath_first_search(do_move,used_pieces,list_finish,pos_finish,check_move, pos_pieces,solution_check,board)
    print(f"Counter: {counter}")
    print(f"Moves: {moves}")
    if solution_path != None:
        for i in range(len(solution_path)):
            for row in solution_path[i]:
                print(" ".join(row))
            print("\n")
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    main_menu()

    pygame.display.update()

play()
