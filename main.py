import pygame
from Minesweeper import Minesweeper, Tile
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H1 + H2))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def board(self):
        self.ms = Minesweeper(COLS, ROWS, AMOUNT_MINES)
        self.score_surface = pygame.Surface((W, H1))
        self.board_surface = pygame.Surface((W, H2))
        self.draw()
        pygame.display.flip()

    def draw(self):
        self.score_surface.fill(BACKGROUND_COLOR)
        self.score_surface.blit(button_off, (X_RESET_BUTTON, Y_RESET_BUTTON))
        self.nr_flags = pygame.font.Font.render(pygame.font.SysFont("mono", FONT_SIZE), f"{self.ms.flags:>03}", True, (255, 0, 0))
        self.time_text = pygame.font.Font.render(pygame.font.SysFont("mono", FONT_SIZE), "000", True, (255, 0, 0))
        self.score_surface.blit(self.nr_flags, (20, (H1 - FONT_SIZE) // 2))
        self.score_surface.blit(self.time_text, (W - self.time_text.get_width() - 20, (H1 - FONT_SIZE) // 2))
        self.screen.blit(self.score_surface, (0, 0))

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
        self.screen.blit(self.board_surface, (0, H1))

    def run(self):
        mouse_on = True
        game_on = True
        while game_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if (X_RESET_BUTTON <= mx < (X_RESET_BUTTON + W_RESET_BUTTON)) and (Y_RESET_BUTTON <= my < (Y_RESET_BUTTON + H_RESET_BUTTON)):
                        game_on = False
                        break
                    elif mouse_on and H1 <= my < H1 + H2:
                        if self.ms.click((my - H1) // TILESIZE, mx // TILESIZE, event.button):
                            mouse_on = False
                    self.draw()
                    pygame.display.flip()


if __name__ == "__main__":
    while True:
        game = Game()
        game.board()
        game.run()
