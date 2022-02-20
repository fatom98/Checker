import pygame
from pygame.time import Clock

from board import Board
from config.setup import SQUARE_SIZE


class Game:
    def __init__(self):
        self.__running: bool = True
        self.__clock: Clock = pygame.time.Clock()
        self.__board = Board()

    def main(self):
        while self.__running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    break

                if event.type == pygame.MOUSEBUTTONUP:
                    index = Game.calculate_index(event.pos)
                    self.__board.select_piece(index)

            self.__board.update()

    @staticmethod
    def calculate_index(pos: tuple[int, int]) -> tuple[int, int]:
        x, y = pos
        row = int(y // SQUARE_SIZE)
        col = int(x // SQUARE_SIZE)

        return row, col


if __name__ == '__main__':
    game = Game()
    game.main()
