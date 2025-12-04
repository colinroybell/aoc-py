from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2025_20(DayBase):
    YEAR = "2025"
    DAY = "20"
    PREFIX = "ec"


def part_1(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings_generator(input_generator(input))
    total = 0
    for x in range(width):
        for y in range(height):
            p = Vec2d(x, y)
            ph = Vec2d(x + 1, y)
            pv = Vec2d(x, y + 1)
            if grid.get(p) == "T":
                if grid.get(ph) == "T":
                    total += 1
                if (x - y) % 2 and grid.get(pv) == "T":
                    total += 1
    return total


def transform(pos, width):
    # Double transform as we've implemented it as 120 clockwise, whereas we
    # need 120 anticlockwise to work ot where we are on the original after a
    # jump
    x = pos.x - pos.y
    y = pos.y
    oldpos = pos
    pos = Vec2d(width - 1 - x // 2 - x % 2 - 2 * y, x // 2)
    x = pos.x - pos.y
    y = pos.y
    oldpos = pos
    pos = Vec2d(width - 1 - x // 2 - x % 2 - 2 * y, x // 2)
    return pos


def orig_pos(pos, width, steps):
    while steps % 3 != 0:
        pos = transform(pos, width)
        steps += 1
    return pos


def part_2(input, part=2):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings_generator(input_generator(input))
    for x in range(width):
        for y in range(height):
            p = Vec2d(x, y)
            if grid.get(p) == "S":
                start = p
    queue = [(0, start)]
    grid.set(start, "T")
    while queue:
        (steps, pos) = queue[0]
        queue = queue[1:]
        if grid.get(pos) == "E":
            return steps
        if grid.get(pos) != "T":
            continue
        grid.set(pos, ".")
        if part == 3:
            pos = transform(pos, width)
            queue.append((steps + 1, pos))

        queue.append((steps + 1, pos + Vec2d(1, 0)))
        queue.append((steps + 1, pos + Vec2d(-1, 0)))
        if (pos.x - pos.y) % 2:
            queue.append((steps + 1, pos + Vec2d(0, 1)))
        else:
            queue.append((steps + 1, pos + Vec2d(0, -1)))
    assert 0, "not found E"


def part_3(input):
    return part_2(input, part=3)


def notes():
    """
    OK, but we've implemented the transform the wrong way around!"""


if __name__ == "__main__":
    Run_2025_20().run_cmdline()
