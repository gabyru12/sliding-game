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

def draw_menu(selected_piece):
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

def draw_board(size):
    # Dividir o tamanho em linhas e colunas
    rows, cols = map(int, size.split('x'))

    # Calcular o tamanho dos quadrados
    square_size = min((WIDTH - 40) // cols, (HEIGHT - 250 - 40) // rows)

    # Calcula o tamanho do tabuleiro
    board_size = min((WIDTH -40), (HEIGHT - 250 - 40))

    # Calcula a margem para centralizar o tabuleiro
    margin_x = (WIDTH - board_size) // 2
    margin_y = 250 + (HEIGHT - 250 - board_size) // 2

    # Desenhar o tabuleiro
    pygame.draw.rect(screen, "white", (margin_x, margin_y, board_size, board_size))
    for row in range(rows - 1):
        pygame.draw.line(screen, "black", (margin_x, margin_y + (row + 1) * square_size), (margin_x + board_size, margin_y + (row + 1) * square_size), 2)
    for col in range(cols - 1):
        pygame.draw.line(screen, "black", (margin_x + (col + 1) * square_size, margin_y), (margin_x + (col + 1) * square_size, margin_y + board_size), 2)

    return margin_x, margin_y, square_size, rows, cols

def draw_piece(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, piece_color):
    pygame.draw.rect(screen, piece_color, ((margin_x + col_clicked * square_size)+1, (margin_y + row_clicked * square_size)+1, square_size, square_size))

def main():
    selected_piece = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    button_x_start = (WIDTH - 3 * 150 - 2 * 50) // 2
                    if button_x_start <= mouse_pos[0] <= button_x_start + 150 and 150 <= mouse_pos[1] <= 200:
                        selected_piece = "Peça 1"
                    elif button_x_start + 200 <= mouse_pos[0] <= button_x_start + 350 and 150 <= mouse_pos[1] <= 200:
                        selected_piece = "Peça 2"
                    elif button_x_start + 400 <= mouse_pos[0] <= button_x_start + 550 and 150 <= mouse_pos[1] <= 200:
                        selected_piece = "Peça 3"

        draw_menu(selected_piece)

        margin_x, margin_y, square_size, rows, cols = draw_board("5x5")

        if selected_piece:
            mouse_pos = pygame.mouse.get_pos()
            col_clicked = (mouse_pos[0] - margin_x) // square_size
            row_clicked = (mouse_pos[1] - margin_y) // square_size
            if 0 <= col_clicked < cols and 0 <= row_clicked < rows:
                piece_color = None
                if selected_piece == "Peça 1":
                    piece_color = "red"
                elif selected_piece == "Peça 2":
                    piece_color = "yellow"
                elif selected_piece == "Peça 3":
                    piece_color = "black"
                draw_piece(screen, square_size, margin_x, margin_y, col_clicked, row_clicked, piece_color)

        pygame.display.flip()

if __name__ == "__main__":
    main()
