import pygame
from Minesweeper import Minesweeper, Tile
from settings import *


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

ms = Minesweeper(COLS, ROWS, AMOUNT_MINES)

board_surface = pygame.Surface((WIDTH, HEIGHT))


def draw():
    for y in range(COLS):
        for x in range(ROWS):
            tile = ms.plane[y][x]
            if tile.state == Tile.COVERED:
                board_surface.blit(tile_unknown, (x * TILESIZE, y * TILESIZE))
            elif tile.state == Tile.CLICKED:
                board_surface.blit(tile_numbers[tile.value], (x * TILESIZE, y * TILESIZE))
            elif tile.state == Tile.EXPLOSION:
                board_surface.blit(tile_exploded, (x * TILESIZE, y * TILESIZE))
            elif tile.state == Tile.NOT_MINE:
                board_surface.blit(tile_not_mine, (x * TILESIZE, y * TILESIZE))
            elif tile.state == Tile.FLAGGED:
                board_surface.blit(tile_flag, (x * TILESIZE, y * TILESIZE))
    screen.blit(board_surface, (0, 0))


draw()

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            ms.click(my // TILESIZE, mx // TILESIZE, event.button)
            draw()
            pygame.display.flip()
