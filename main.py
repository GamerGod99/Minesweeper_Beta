import pygame
from Minesweeper import Minesweeper, Tile
from settings import *


class Timer:
    def __init__(self):
        self._start = 0
        self._run = False
        self._last = 0

    def start(self):
        if not self._run:
            self._run = True
            self._start = pygame.time.get_ticks()

    def current(self):
        current_time = (pygame.time.get_ticks() - self._start)//1000
        return current_time if self._run else self._last

    def stop(self):
        self._last = self.current()
        self._run = False


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H1 + H2))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.reset_button = button_off

    def board(self):
        self.ms = Minesweeper(COLS, ROWS, AMOUNT_MINES)
        self.t = Timer()
        self.score_surface = pygame.Surface((W, H1))
        self.board_surface = pygame.Surface((W, H2))
        self.font = pygame.font.SysFont("mono", FONT_SIZE)
        self.draw()
        pygame.display.flip()

    def draw(self):
        self.score_surface.fill(BACKGROUND_COLOR)
        self.score_surface.blit(self.reset_button, (X_RESET_BUTTON, Y_RESET_BUTTON))
        self.nr_flags = pygame.font.Font.render(self.font, f"{self.ms.flags:03}", True, (255, 0, 0))
        self.time_text = pygame.font.Font.render(self.font, f"{self.t.current():03}", True, (255, 0, 0))
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
                        self.t.start()
                        if button := self.ms.click((my - H1) // TILESIZE, mx // TILESIZE, event.button):
                            mouse_on = False
                            self.t.stop()
                            match button:
                                case 1:
                                    self.reset_button = button_x
                                case 2:
                                    self.reset_button = button_win
                                case _:
                                    self.reset_button = button_off
            self.draw()
            pygame.display.flip()


if __name__ == "__main__":
    while True:
        game = Game()
        game.board()
        game.run()
