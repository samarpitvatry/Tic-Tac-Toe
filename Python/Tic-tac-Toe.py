import pygame
import sys

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def draw_board():
    screen.fill(GREY)
    pygame.draw.rect(screen, WHITE, (PADDING, PADDING, WIDTH - 2 * PADDING, HEIGHT - 2 * PADDING))
    for row in range(BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (PADDING, PADDING + row * SQUARE_SIZE), (WIDTH - PADDING, PADDING + row * SQUARE_SIZE), 2)
    for col in range(BOARD_COLS):
        pygame.draw.line(screen, BLACK, (PADDING + col * SQUARE_SIZE, PADDING), (PADDING + col * SQUARE_SIZE, HEIGHT - PADDING), 2)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (PADDING + col * SQUARE_SIZE + 20, PADDING + row * SQUARE_SIZE + 20), (PADDING + (col + 1) * SQUARE_SIZE - 20, PADDING + (row + 1) * SQUARE_SIZE - 20), 8)
                pygame.draw.line(screen, RED, (PADDING + col * SQUARE_SIZE + 20, PADDING + (row + 1) * SQUARE_SIZE - 20), (PADDING + (col + 1) * SQUARE_SIZE - 20, PADDING + row * SQUARE_SIZE + 20), 8)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLUE, (PADDING + col * SQUARE_SIZE + SQUARE_SIZE // 2, PADDING + row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3, 8)

def mark_square(row, col, player):
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        board[row][col] = 'X' if player == 1 else 'O'
        return True
    return False

def check_winner():
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            draw_winning_line(row, 'horizontal')
            return True

    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            draw_winning_line(col, 'vertical')
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        draw_winning_line(0, 'main_diagonal')
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        draw_winning_line(0, 'anti_diagonal')
        return True

    return False

def draw_winning_line(index, direction):
    if direction == 'horizontal':
        pygame.draw.line(screen, GREEN, (PADDING, PADDING + index * SQUARE_SIZE + SQUARE_SIZE // 2), (WIDTH - PADDING, PADDING + index * SQUARE_SIZE + SQUARE_SIZE // 2), 4)
    elif direction == 'vertical':
        pygame.draw.line(screen, GREEN, (PADDING + index * SQUARE_SIZE + SQUARE_SIZE // 2, PADDING), (PADDING + index * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - PADDING), 4)
    elif direction == 'main_diagonal':
        pygame.draw.line(screen, GREEN, (PADDING + 20, PADDING + 20), (WIDTH - PADDING - 20, HEIGHT - PADDING - 20), 4)
    elif direction == 'anti_diagonal':
        pygame.draw.line(screen, GREEN, (WIDTH - PADDING - 20, PADDING + 20), (PADDING + 20, HEIGHT - PADDING - 20), 4)

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
PADDING = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)

# Initialize the board
board = initialize_board()
player_turn = 1

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
draw_board()

# Main loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] - PADDING
            mouseY = event.pos[1] - PADDING
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if mark_square(clicked_row, clicked_col, player_turn):
                if check_winner():
                    game_over = True
                else:
                    player_turn = 3 - player_turn
                draw_figures()

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
sys.exit()
