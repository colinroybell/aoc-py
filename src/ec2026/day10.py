from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d, opposite_direction, rotate_clockwise
from utils.grid_2d import Grid2d


class Run_2026_10(DayBase):
    YEAR = "2026"
    DAY = "10"
    PREFIX = "ec"


class Ghost:
    def __init__(self, pos, dir, counter):
        self.pos = pos
        self.dir = dir
        self.counter = counter

    def advance(self, grid):
        new_pos = self.pos.move_y_flipped(self.dir)
        if grid.get(new_pos) == "#":
            self.dir = rotate_clockwise(self.dir)
            self.counter -= 1
            return 1
        else:
            self.pos = new_pos
            return 0

    def flip(self):
        self.dir = opposite_direction(self.dir)


def part_1(input, part=1, counter=10000):
    grid = Grid2d()
    generator = input_generator(input)
    (width, height) = grid.read_from_file_strings(input)
    print(grid)
    collisions = 0
    ghosts = []
    surviving_ghosts = 0
    for y in range(height):
        for x in range(width):
            pos = Vec2d(x, y)
            char = grid.get(pos)
            if char != "#" and char != ".":
                ghost = Ghost(pos, char, counter)
                ghosts.append(ghost)

    surviving_ghosts = len(ghosts)

    round = 0
    while surviving_ghosts > 0:
        locs = {}
        for n, ghost in enumerate(ghosts):
            if ghost.counter > 0:
                collisions += ghost.advance(grid)
                if ghost.counter == 0:
                    surviving_ghosts -= 1
                else:
                    if ghost.pos in locs:
                        other = locs[ghost.pos]
                        if other != "DONE":
                            ghosts[other].flip()
                            ghosts[other].counter -= 1
                            collisions += 1
                            if ghosts[other].counter == 0:
                                surviving_ghosts -= 1
                        ghost.flip()
                        ghost.counter -= 1
                        locs[ghost.pos] = "DONE"
                        collisions += 1
                        if ghost.counter == 0:
                            surviving_ghosts -= 1
                    else:
                        locs[ghost.pos] = n
        print(f"Round {round} Collisions{collisions}, Ghosts{surviving_ghosts}")
        round += 1
        # for ghost in ghosts:
        #    print(ghost.pos, ghost.dir, ghost.counter)
        if part == 1 and round == 10:
            return collisions
    return round


def part_2(input, counter=10000):
    return part_1(input, part=2, counter=counter)


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2026_10().run_cmdline()
