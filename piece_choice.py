import pygame
import sys

# Inicializando Pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu de Tabuleiro")

# Fonte e tamanho do texto
font = pygame.font.SysFont(None, 40)

def draw_board(size):
    # Dividir o tamanho em linhas e colunas
    rows, cols = map(int, size.split('x'))

    # Calcula o tamanho do tabuleiro
    board_size = 300 + 2 * (rows-1)

    # Calcular o tamanho dos quadrados
    square_size = board_size // rows

    # Calcula a margem para centralizar o tabuleiro
    margin_x = WIDTH // 2 - board_size // 2
    margin_y = 250

    # Desenhar o tabuleiro
    pygame.draw.rect(screen, "white", (margin_x, margin_y, board_size, board_size))
    pygame.draw.rect(screen, "black", (margin_x, margin_y, board_size, board_size),2)
    for row in range(rows - 1):
        pygame.draw.line(screen, "black", (margin_x, (margin_y + (row + 1) * square_size)), (margin_x + board_size - 1, (margin_y + (row + 1) * square_size)), 2)
    for col in range(cols - 1):
        pygame.draw.line(screen, "black", ((margin_x + (col + 1) * square_size), margin_y), ((margin_x + (col + 1) * square_size), margin_y + board_size - 1), 2)

    return margin_x, margin_y, square_size, rows, cols

def draw_piece(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, piece_color,size):
    rows, cols = map(int, size.split('x'))
    board_size = 300 + 2 * (rows-1)
    pygame.draw.rect(screen, piece_color, ((margin_x + col_clicked * square_size), (margin_y + row_clicked * square_size), square_size+2, square_size+2))
    pygame.draw.rect(screen, "black", (margin_x, margin_y, board_size, board_size),2)
    for row in range(rows - 1):
        pygame.draw.line(screen, "black", (margin_x, (margin_y + (row + 1) * square_size)), (margin_x + board_size - 1, (margin_y + (row + 1) * square_size)), 2)
    for col in range(cols - 1):
        pygame.draw.line(screen, "black", ((margin_x + (col + 1) * square_size), margin_y), ((margin_x + (col + 1) * square_size), margin_y + board_size - 1), 2)

def choose_board():
    run = True
    selected_size = "4x4"
    while run:
        screen.fill("light blue")
        title_text = font.render("Escolha o tamanho do tabuleiro:", True, "black")
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

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

        mx,my = pygame.mouse.get_pos()
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
                put_pieces()

        # Desenhar o tabuleiro
        if selected_size:
            draw_board(selected_size)

        pygame.display.update()

def put_pieces():
    run = True
    selected_piece = None
    while run:
        screen.fill("light blue")  # light blue color

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

        mx,my = pygame.mouse.get_pos()
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

        margin_x, margin_y, square_size, rows, cols = draw_board("6x6")

        if selected_piece:
            col_clicked = (mx - margin_x) // square_size
            row_clicked = (my - margin_y) // square_size
            if 0 <= col_clicked < cols and 0 <= row_clicked < rows:
                piece_color = None
                if selected_piece == "Peça 1":
                    piece_color = "red"
                elif selected_piece == "Peça 2":
                    piece_color = "yellow"
                elif selected_piece == "Peça 3":
                    piece_color = "black"
                draw_piece(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, piece_color,"6x6")
        
        pygame.display.update()

choose_board()
