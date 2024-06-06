import pygame
from Minesweeper import Minesweeper, Tile
from settings import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

ms = Minesweeper(COLS, ROWS, AMOUNT_MINES)

board_surface = pygame.Surface((WIDTH, HEIGHT))
for col in range(COLS):
    for row in range(ROWS):
        tile = ms.plane[col][row]
        if tile.state == Tile.COVERED:
            board_surface.blit(tile_unknown, (col * TILESIZE, row * TILESIZE))
        elif tile.state == Tile.CLICKED:
            board_surface.blit(tile_numbers[tile.value], (col * TILESIZE, row * TILESIZE))

screen.blit(board_surface, (0, 0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)


