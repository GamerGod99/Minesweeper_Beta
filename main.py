import pygame
from Minesweeper import Minesweeper, Tile
from settings import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def board(self):
        self.ms = Minesweeper(COLS, ROWS, AMOUNT_MINES)
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.draw()
        pygame.display.flip()

    def draw(self):
        for y in range(COLS):
            for x in range(ROWS):
                tile = self.ms.plane[y][x]
                if tile.state == Tile.COVERED:
                    self.board_surface.blit(tile_unknown, (x * TILESIZE, y * TILESIZE))
                elif tile.state == Tile.CLICKED:
                    self.board_surface.blit(tile_numbers[tile.value], (x * TILESIZE, y * TILESIZE))
                elif tile.state == Tile.EXPLOSION:
                    self.board_surface.blit(tile_exploded, (x * TILESIZE, y * TILESIZE))
                elif tile.state == Tile.NOT_MINE:
                    self.board_surface.blit(tile_not_mine, (x * TILESIZE, y * TILESIZE))
                elif tile.state == Tile.FLAGGED:
                    self.board_surface.blit(tile_flag, (x * TILESIZE, y * TILESIZE))
        self.screen.blit(self.board_surface, (0, 0))

    def run(self):
        game_over = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN and game_over != 1:
                    mx, my = pygame.mouse.get_pos()

                    game_over = self.ms.click(my // TILESIZE, mx // TILESIZE, event.button)

                    self.draw()
                    pygame.display.flip()


if __name__ == "__main__": #     1212e
    game = Game()
    game.board()
    game.run()
