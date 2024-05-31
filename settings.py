import pygame
import os

TILESIZE = 25
ROWS = 15
COLS = 15
AMOUNT_MINES = 15
WIDTH = TILESIZE * ROWS
HEIGHT = TILESIZE * COLS
FPS = 60
TITLE = "Minesweeper"

tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileUnknown.png")), (TILESIZE, TILESIZE))

tile_numbers = []
for i in range(9):
    tile_numbers.append(
        pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")), (TILESIZE, TILESIZE)))