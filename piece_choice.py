import pygame
import sys

# Inicializando Pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu de Tabuleiro")

selected_size = "4x4"

# Fonte e tamanho do texto
font = pygame.font.SysFont(None, 40)

def play():
    run = True
    while run:
        click = False
        mx,my = pygame.mouse.get_pos()
        screen.fill("light blue")
        play_width,play_height = 120,60
        play_rec = pygame.draw.rect(screen,"grey",(WIDTH/2-play_width//2,HEIGHT/2-play_height//2,play_width,play_height), 0)
        play_border = pygame.draw.rect(screen,"black",(WIDTH/2-play_width//2,HEIGHT/2-play_height//2,play_width,play_height), 5)
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
            play_border = pygame.draw.rect(screen,"yellow",(WIDTH/2-play_width//2,HEIGHT/2-play_height//2,play_width,play_height), 5)
            if click == True:
                run = False
                choose_board(selected_size)

        pygame.display.update()

def draw_board(size,board,mx,my):
    # Dividir o tamanho em linhas e colunas
    rows, cols = map(int, size.split('x'))

    # Calcula o tamanho do tabuleiro
    board_size = 300 + 2 * (rows-1) 

    # Calcular o tamanho dos quadrados
    square_size = 300 / rows

    # Calcula a margem para centralizar o tabuleiro
    margin_x = WIDTH // 2 - board_size // 2
    margin_y = 250

    col_clicked = int((mx - margin_x) // square_size)
    row_clicked = int((my - margin_y) // square_size)

    # Desenhar o tabuleiro
    pygame.draw.rect(screen, "white", (margin_x, margin_y, board_size, board_size))
    for row in range(rows - 1):
        pygame.draw.line(screen, "black", (margin_x, (margin_y + (row + 1) * square_size + row * 2)), (margin_x + board_size - 1, (margin_y + (row + 1) * square_size + row * 2)), 2)
    for col in range(cols - 1):
        pygame.draw.line(screen, "black", ((margin_x + (col + 1) * square_size + col * 2), margin_y), ((margin_x + (col + 1) * square_size + col * 2), margin_y + board_size - 1), 2)

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col][0] == "1":
                pygame.draw.rect(screen, "red", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))
            if board[row][col][0] == "2":
                pygame.draw.rect(screen, "yellow", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))
            if board[row][col] == "3":
                pygame.draw.rect(screen, "black", ((margin_x + col * (square_size + 2)), (margin_y + row * (square_size + 2)), square_size, square_size))

    pygame.draw.rect(screen, "black", (margin_x, margin_y, board_size, board_size),2)


    return margin_x, margin_y, square_size, rows, cols, board_size

def draw_piece(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, piece_color,size):
    rows, cols = map(int, size.split('x'))
    board_size = 300 + 2 * (rows-1)
    pygame.draw.rect(screen, piece_color, ((margin_x + col_clicked * (square_size + 2)), (margin_y + row_clicked * (square_size + 2)), square_size, square_size))
    pygame.draw.rect(screen, "black", (margin_x, margin_y, board_size, board_size),2)
    
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

        button_4x4 = pygame.Rect(button_x_start, button_y, button_width, button_height)
        pygame.draw.rect(screen, "gray", button_4x4)
        pygame.draw.rect(screen, "black", button_4x4,2)
        text_4x4 = font.render("4x4", True, "black")
        screen.blit(text_4x4, (button_x_start + button_width // 2 - text_4x4.get_width() // 2, button_y + button_height // 2 - text_4x4.get_height() // 2))

        button_5x5 = pygame.Rect(button_x_start + button_width + 50, button_y, button_width, button_height)
        pygame.draw.rect(screen, "gray", button_5x5)
        pygame.draw.rect(screen, "black", button_5x5,2)
        text_5x5 = font.render("5x5", True, "black")
        screen.blit(text_5x5, (button_x_start + button_width + 50 + button_width // 2 - text_5x5.get_width() // 2, button_y + button_height // 2 - text_5x5.get_height() // 2))

        button_6x6 = pygame.Rect(button_x_start + 2 * (button_width + 50), button_y, button_width, button_height)
        pygame.draw.rect(screen, "gray", button_6x6)
        pygame.draw.rect(screen, "black", button_6x6,2)
        text_6x6 = font.render("6x6", True, "black")
        screen.blit(text_6x6, (button_x_start + 2 * (button_width + 50) + button_width // 2 - text_6x6.get_width() // 2, button_y + button_height // 2 - text_6x6.get_height() // 2))

        button_next = pygame.Rect(WIDTH - (button_width + 25), HEIGHT - (button_height + 25), button_width, button_height)
        pygame.draw.rect(screen, "green", button_next)
        pygame.draw.rect(screen, "black", button_next,2)
        text_next = font.render("Next", True, "black")
        screen.blit(text_next, (WIDTH - (button_width + 25) + button_width // 2 - text_next.get_width() // 2,HEIGHT - (button_height + 25) + button_height // 2 - text_next.get_height() // 2))

        if button_x_start <= mx <= button_x_start + 100 and 150 <= my <= 150 + button_height:
            pygame.draw.rect(screen, "light gray", button_4x4)
            pygame.draw.rect(screen, "black", button_4x4,2)
            screen.blit(text_4x4, (button_x_start + button_width // 2 - text_4x4.get_width() // 2, button_y + button_height // 2 - text_4x4.get_height() // 2))
        elif button_x_start + button_width + 50 <= mx <= button_x_start + button_width + 50 + button_width and 150 <= my <= 150 + button_height:
            pygame.draw.rect(screen, "light gray", button_5x5)
            pygame.draw.rect(screen, "black", button_5x5,2)
            screen.blit(text_5x5, (button_x_start + button_width + 50 + button_width // 2 - text_5x5.get_width() // 2, button_y + button_height // 2 - text_5x5.get_height() // 2))
        elif button_x_start + 2 * (button_width + 50) <= mx <= button_x_start + 2 * (button_width +50) + button_width and 150 <= my <= 150 + button_height:
            pygame.draw.rect(screen, "light gray", button_6x6)
            pygame.draw.rect(screen, "black", button_6x6,2)
            screen.blit(text_6x6, (button_x_start + 2 * (button_width + 50) + button_width // 2 - text_6x6.get_width() // 2, button_y + button_height // 2 - text_6x6.get_height() // 2))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if click:
            if button_x_start <= mx <= button_x_start + 100 and 150 <= my <= 150 + button_height:
                selected_size = "4x4"
            elif button_x_start + button_width + 50 <= mx <= button_x_start + button_width + 50 + button_width and 150 <= my <= 150 + button_height:
                selected_size = "5x5"
            elif button_x_start + 2 * (button_width + 50) <= mx <= button_x_start + 2 * (button_width +50) + button_width and 150 <= my <= 150 + button_height:
                selected_size = "6x6"
            elif WIDTH - (button_width + 25) <= mx <= WIDTH - (button_width + 25) + button_width and HEIGHT - (button_height + 25) <= my <= HEIGHT - (button_height + 25) + button_height:
                run = False
                put_pieces(selected_size)

        # Desenhar o tabuleiro
        if selected_size:
            draw_board(selected_size,board,mx,my)

        pygame.display.update()

def put_pieces(selected_size):
    run = True
    selected_piece = None
    board_lenght = int(selected_size[0])
    board = [["0" for _ in range(board_lenght)]for _ in range(board_lenght)]
    piece_color = None
    while run:
        screen.fill("light blue")  # light blue color
        
        mx,my = pygame.mouse.get_pos()

        # Texto do título
        title_text = font.render("Posicione as peças:", True, "black")
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        # Botões para escolher o tipo de peça
        button_width, button_height = 150, 50
        button_y = 150
        button_x_start = (WIDTH - 3 * button_width - 2 * 50) // 2

        button_piece1 = pygame.Rect(button_x_start, button_y, button_width, button_height)
        pygame.draw.rect(screen, "red", button_piece1)
        text_piece1 = font.render("Peça 1", True, "black")
        screen.blit(text_piece1, (button_x_start + button_width // 2 - text_piece1.get_width() // 2, button_y + button_height // 2 - text_piece1.get_height() // 2))

        button_piece2 = pygame.Rect(button_x_start + button_width + 50, button_y, button_width, button_height)
        pygame.draw.rect(screen, "yellow", button_piece2)
        text_piece2 = font.render("Peça 2", True, "black")
        screen.blit(text_piece2, (button_x_start + button_width + 50 + button_width // 2 - text_piece2.get_width() // 2, button_y + button_height // 2 - text_piece2.get_height() // 2))

        button_piece3 = pygame.Rect(button_x_start + 2 * (button_width + 50), button_y, button_width, button_height)
        pygame.draw.rect(screen, "black", button_piece3)
        text_piece3 = font.render("Peça 3", True, "white")
        screen.blit(text_piece3, (button_x_start + 2 * (button_width + 50) + button_width // 2 - text_piece3.get_width() // 2, button_y + button_height // 2 - text_piece3.get_height() // 2))

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    choose_board()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if click:
            button_x_start = (WIDTH - 3 * 150 - 2 * 50) // 2
            if button_x_start <= mx <= button_x_start + 150 and 150 <= my <= 200:
                selected_piece = "Peça 1"
            elif button_x_start + 200 <= mx <= button_x_start + 350 and 150 <= my <= 200:
                selected_piece = "Peça 2"
            elif button_x_start + 400 <= mx <= button_x_start + 550 and 150 <= my <= 200:
                selected_piece = "Peça 3"

        margin_x, margin_y, square_size, rows, cols, board_size = draw_board(selected_size,board,mx,my)

        if selected_piece:
            col_clicked = int((mx - margin_x) // square_size)
            row_clicked = int((my - margin_y) // square_size)
            if 0 <= col_clicked < cols and 0 <= row_clicked < rows:
                if selected_piece == "Peça 1":
                    piece_color = "red"
                elif selected_piece == "Peça 2":
                    piece_color = "yellow"
                elif selected_piece == "Peça 3":
                    piece_color = "black"
                draw_piece(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, piece_color,selected_size)
            if click:
                if margin_x <= mx <= margin_x + board_size and margin_y <= my <= margin_y + board_size:
                    if piece_color == "red":
                        board[row_clicked][col_clicked] = "1"
                    if piece_color == "yellow":
                        board[row_clicked][col_clicked] = "2"
                    if piece_color == "black":
                        board[row_clicked][col_clicked] = "3"

    
        pygame.display.update()

play()
