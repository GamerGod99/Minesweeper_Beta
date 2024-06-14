import random

# https://minesweeper.us/saper/


IMG = {
    "NO_0": " ",
    "NO_1": "1",
    "NO_2": "2",
    "NO_3": "3",
    "NO_4": "4",
    "NO_5": "5",
    "NO_6": "6",
    "NO_7": "7",
    "NO_8": "8",

    "NO_9": "*",
    "EXPLOSION": "#",
    "NOT_MINE": "X",

    "COVERED": "\u2586",
    "CLICKED": " ",
    "FLAGGED": "\u2691",
}


class Tile:
    COVERED = 0
    CLICKED = 1
    FLAGGED = 2

    EXPLOSION = 3
    NOT_MINE = 4
    MINE = 9

    def __init__(self, y, x, value, state) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.state = state

    def __repr__(self) -> str:
        if self.state == self.COVERED:
            return IMG["COVERED"]
        elif self.state == self.CLICKED:
            return IMG[f"NO_{self.value}"]
        elif self.state == self.FLAGGED:
            return IMG["FLAGGED"]
        elif self.state == self.EXPLOSION:
            return IMG["EXPLOSION"]
        elif self.state == self.NOT_MINE:
            return IMG["NOT_MINE"]
        return ""


class Minesweeper:
    around = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1), ]

    def __init__(self, sizeY, sizeX, mines):
        self.sizeY = sizeY
        self.sizeX = sizeX
        self.mines = mines
        self.moves = 0
        self.flags = mines
        self.covered = sizeY * sizeX
        self.history = []
        self.plane = self.__plant()

    def __repr__(self):
        return '\n' + '\n'.join('\t' + ' '.join(str(tile) for tile in row) for row in self.plane) + '\n'

    def __plant(self):
        random.shuffle(mines := [Tile.MINE for i in range(self.mines)] + [0] * (self.sizeX * self.sizeY - self.mines))

        plane = []

        for y in range(self.sizeY):
            tmp = []
            for x in range(self.sizeX):
                tmp.append(Tile(y, x, mines[y * self.sizeY + x], Tile.COVERED))
            plane.append(tmp)

        for y in range(self.sizeY):
            for x in range(self.sizeX):
                if plane[y][x].value != Tile.MINE:
                    n_mines = 0
                    for step_y, step_x in self.around:
                        if 0 <= (y_around := y + step_y) < self.sizeY and 0 <= (x_around := x + step_x) < self.sizeX:
                            n_mines += plane[y_around][x_around].value == Tile.MINE
                    plane[y][x].value = n_mines
        return plane

    def check_around(self, y, x):
        game_over = 0
        if 0 <= x < self.sizeX and 0 <= y < self.sizeY:  # If chosen coords are part of the plane
            tile = self.plane[y][x]
            if tile.state == Tile.COVERED:
                if tile.value == 0:
                    self.change_state(tile, Tile.CLICKED)
                    self.covered -= 1
                    for step_y, step_x in self.around:
                        self.check_around(y + step_y, x + step_x)  # Checks the tiles around chosen tile.
                elif 0 < tile.value < 9:
                    self.change_state(tile, Tile.CLICKED)
                    self.covered -= 1
                else:  # Tile is a mine
                    game_over = self.game_over(y, x)
        return game_over

    def game_over(self, y, x):
        self.change_state(self.plane[y][x], Tile.EXPLOSION)
        self.covered -= 1

        for y in range(self.sizeY):
            for x in range(self.sizeX):
                tile = self.plane[y][x]
                if tile.value == Tile.MINE and tile.state == Tile.COVERED:
                    self.change_state(tile, Tile.CLICKED)
                    self.covered -= 1
                # if tile.value == Tile.MINE and tile.state == Tile.FLAGGED:
                #     tile.state == Tile.FLAGGED
                if tile.value != Tile.MINE and tile.state == Tile.FLAGGED:
                    self.change_state(tile, Tile.NOT_MINE)
                    self.covered -= 1
        return 1

    def change_state(self, tile, new_state):
        tile.state = new_state
        self.history.append(tile)

    def click(self, y, x, btn):
        game_over = 0
        tile = self.plane[y][x]
        self.history.clear()
        if btn == 3:
            if tile.state == Tile.COVERED:
                if self.moves < 1:
                    game_over = self.check_around(y, x)
                    self.moves += 1
                else:
                    self.change_state(tile, Tile.FLAGGED)
                    self.covered -= 1
                    self.flags -= 1
            elif tile.state == Tile.CLICKED:
                pass
            elif tile.state == Tile.FLAGGED:
                self.change_state(tile, Tile.COVERED)
                self.covered += 1
                self.flags += 1
        elif btn == 1:
            if tile.state == Tile.COVERED:
                game_over = self.check_around(y, x)
                self.moves += 1
            elif tile.state == Tile.CLICKED:
                pass
            elif tile.state == Tile.FLAGGED:
                pass
        if self.flags >= 0 and (self.mines - self.flags + self.covered) == self.mines:
            game_over = 2

        return game_over


def print_plant(m):
    print('\n' + '\n'.join(
        '\t' + ' '.join(str(tile.value if tile.value < 9 else "*") for tile in row) for row in m.plane) + '\n')


if __name__ == "__main__":
    ms = Minesweeper(10, 10, 10)

    print_plant(ms)
    print(ms)
    print('\t' * 4 + f"Moves: {ms.moves}" + '\n' + '\t' * 4 + f"Flags: {ms.flags}")

    while True:
        user_in = input("\ty x b = ")
        if user_in == "": break
        user_y, user_x, btn = map(int, user_in.split())
        if ms.click(user_y, user_x, btn):
            print(ms)
            print('\t' * 4 + f"Moves: {ms.moves}" + '\n' + '\t' * 4 + f"Flags: {ms.flags}")
            break

        print('\t' * 4 + f"Moves: {ms.moves}" + '\n' + '\t' * 4 + f"Flags: {ms.flags}")
        print(ms)
