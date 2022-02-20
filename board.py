import copy
from pprint import pprint

import pygame
from pygame.surface import Surface

from config.setup import COL, ROW, BOARD, BLACK, WHITE, FPS
from pieces.piece import Piece


class Board:
    def __init__(self):
        self.__win: Surface = pygame.display.get_surface()
        self.__clock = pygame.time.Clock()
        self.__selected_piece: Piece = None
        self.__board_array: list = [[0 for _ in range(COL)] for _ in range(ROW)]
        self.create_board()

    def draw_board(self):
        self.__win.blit(BOARD, (0, 0))

    def update(self) -> None:
        self.draw_board()

        for row in range(ROW):
            for piece in self.__board_array[row]:
                if piece != 0:
                    piece.draw()

        pygame.display.update()
        self.__clock.tick(FPS)

    def create_board(self) -> None:

        for row in range(1, 8):

            if row == 1 or row == 2:
                for col in range(COL):
                    self.__board_array[row][col] = Piece(row, col, BLACK)

            elif row == 3 or row == 4 or row == 5:
                continue

            elif row == 6 or row == 7:
                for col in range(COL):
                    self.__board_array[row][col] = Piece(row, col, WHITE)

    def move_piece(self, index: tuple[int, int]) -> None:

        if index in self.__selected_piece.get_valid_moves(self.__board_array[:]):
            next_row, next_col = index
            current_row, current_col = self.__selected_piece.get_index()

            self.__board_array[next_row][next_col] = 0
            self.__board_array[current_row][current_col], self.__board_array[next_row][next_col] = self.__board_array[next_row][next_col], self.__board_array[current_row][
                current_col]
            self.__selected_piece.move(index)

    def select_piece(self, index: tuple[int, int]):
        piece = self.get_piece(index)

        if self.__selected_piece is None:

            if piece != 0:
                self.__selected_piece = piece
        else:

            if piece == 0 or piece.get_color() != self.__selected_piece.get_color():
                self.move_piece(index)
                self.__selected_piece = None

    def get_piece(self, index: tuple[int, int]) -> Piece:
        row, col = index
        return self.__board_array[row][col]
