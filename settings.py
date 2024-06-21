import pygame
import os

TILESIZE = 32
ROWS = 15
COLS = 15
AMOUNT_MINES = 40
W = TILESIZE * ROWS
H1 = TILESIZE * 3
H2 = TILESIZE * COLS
FPS = 60
TITLE = "Minesweeper Clone"
BACKGROUND_COLOR = (192, 192, 192)
FONT_SIZE = 60

tile_numbers = []
for i in range(10):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")), (TILESIZE, TILESIZE)))

tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileExploded.png")), (TILESIZE, TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileFlag.png")), (TILESIZE, TILESIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileUnknown.png")), (TILESIZE, TILESIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileNotMine.png")), (TILESIZE, TILESIZE))

X_RESET_BUTTON, Y_RESET_BUTTON = (W - TILESIZE * 2) // 2, (H1 - TILESIZE * 2) // 2
W_RESET_BUTTON, H_RESET_BUTTON = TILESIZE * 2, TILESIZE * 2
button_off = pygame.transform.scale(pygame.image.load(os.path.join("assets", "button_off.png")), (W_RESET_BUTTON, H_RESET_BUTTON))
button_on = pygame.transform.scale(pygame.image.load(os.path.join("assets", "button_on.png")), (W_RESET_BUTTON, H_RESET_BUTTON))
button_o = pygame.transform.scale(pygame.image.load(os.path.join("assets", "button_o.png")), (W_RESET_BUTTON, H_RESET_BUTTON))
button_x = pygame.transform.scale(pygame.image.load(os.path.join("assets", "button_x.png")), (W_RESET_BUTTON, H_RESET_BUTTON))