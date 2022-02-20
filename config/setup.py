import pygame

pygame.init()

# GAME VARIABLES
HEIGHT = WIDTH = 1200
ROW = COL = 8
FPS = 60
SQUARE_SIZE = WIDTH / COL
PIECE_SIZE = SQUARE_SIZE * 2 / 3

pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checker")

# RGB COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)

# IMAGES
BOARD = pygame.image.load("assets/board.png").convert_alpha()
BOARD = pygame.transform.scale(BOARD, (WIDTH, HEIGHT))

RED_PIECE = pygame.image.load("assets/red_piece.png").convert_alpha()
RED_PIECE = pygame.transform.scale(RED_PIECE, (PIECE_SIZE, PIECE_SIZE))

RED_KING = pygame.image.load("assets/red_king.png").convert_alpha()
RED_KING = pygame.transform.scale(RED_KING, (PIECE_SIZE, PIECE_SIZE))

BLACK_PIECE = pygame.image.load("assets/black_piece.png").convert_alpha()
BLACK_PIECE = pygame.transform.scale(BLACK_PIECE, (PIECE_SIZE, PIECE_SIZE))

BLACK_KING = pygame.image.load("assets/black_king.png").convert_alpha()
BLACK_KING = pygame.transform.scale(BLACK_KING, (PIECE_SIZE, PIECE_SIZE))
