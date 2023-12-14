from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2023_13(DayBase):
    YEAR = "2023"
    DAY = "13"


def horiz_try(grid, width, height, x, fail_target):
    cols = min(x, width - x)
    fail_count = 0
    for i in range(0, cols):
        for j in range(0, height):
            if grid.get(Vec2d(x + i, j)) != grid.get(Vec2d(x - 1 - i, j)):
                fail_count += 1
                if fail_count > fail_target:
                    return False
    return fail_count == fail_target


def vert_try(grid, width, height, y, fail_target):
    rows = min(y, height - y)
    fail_count = 0
    for j in range(0, rows):
        for i in range(0, width):
            if grid.get(Vec2d(i, y + j)) != grid.get(Vec2d(i, y - 1 - j)):
                fail_count += 1
                if fail_count > fail_target:
                    return False
    return fail_count == fail_target


def score(lines, part_b):
    if not part_b:
        fail_count = 0
    else:
        fail_count = 1
    grid = Grid2d()
    print(lines)
    (width, height) = grid.read_from_hash_dot_list(lines)
    for x in range(1, width):
        if horiz_try(grid, width, height, x, fail_count):
            return x
    for y in range(1, height):
        if vert_try(grid, width, height, y, fail_count):
            return 100 * y
    assert 0


def part_a(input, part_b=False):
    lines = []
    total = 0
    for line in input_generator(input):
        if line != "":
            lines.append(line)
        else:
            total += score(lines, part_b)
            print(total)
            lines = []
    total += score(lines, part_b)
    return total


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_13().run_cmdline()
