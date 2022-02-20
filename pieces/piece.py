import pygame
from pygame import Surface

from config.setup import BLACK, SQUARE_SIZE, RED_PIECE, BLACK_PIECE, RED_KING, BLACK_KING


class Piece:
    __row: int
    __col: int
    __color: tuple[int]
    __direction: int
    __x: int
    __y: int
    __king: bool

    def __init__(self, row: int, col: int, color: tuple[int]):
        self.__row = row
        self.__col = col
        self.__color = color
        self.__king = False
        self.__direction = 1 if color == BLACK else 0
        self.__image = BLACK_PIECE if color == BLACK else RED_PIECE
        self.calculate_position()

    def calculate_position(self) -> None:
        self.__x = self.__col * SQUARE_SIZE + SQUARE_SIZE / 6
        self.__y = self.__row * SQUARE_SIZE + SQUARE_SIZE / 6

    def get_position(self) -> tuple[int, int]:
        return self.__x, self.__y

    def get_index(self) -> tuple[int, int]:
        return self.__row, self.__col

    def move(self, index: tuple[int, int]) -> None:
        self.__row, self.__col = index
        self.calculate_position()

    def get_color(self) -> tuple[int]:
        return self.__color

    def make_king(self):
        self.__king = True
        self.__image = BLACK_KING if self.__color == BLACK else RED_KING

    def is_king(self) -> bool:
        return self.__king

    def draw(self) -> None:
        win = pygame.display.get_surface()
        win.blit(self.__image, self.get_position())

    def get_valid_moves(self, board: list) -> list[tuple[int, int]]:
        valid_moves = []

        if self.is_king():
            ...
        else:
            ...

        return valid_moves

    def __str__(self):
        return f"Piece(row: {self.__row}, col: {self.__col}, color: {self.__color})"
