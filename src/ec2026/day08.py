from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2026_08(DayBase):
    YEAR = "2026"
    DAY = "08"
    PREFIX = "ec"


class Status:
    def __init__(self):
        self.energy = 0
        self.warriors = 0

    def __add__(self, other):
        ret = Status()
        ret.energy = self.energy + other.energy
        ret.warriors = self.warriors + other.warriors
        return ret

    def __repr__(self):
        return f"E {self.energy} W {self.warriors}"


def calc_line(grid, width, height, diff, start, part=1):
    shadow = None
    point = start
    count = Status()
    while 0 <= point.x < width and 0 <= point.y < height:
        if shadow:
            shadow -= 1
        item = grid.get(point)
        if item != None:
            if item > 0 and (shadow == None or item > shadow):
                count.energy += 1
                shadow = item
                if part == 3:
                    if item < 9:
                        grid.set(point, item + 1)
                    else:
                        grid.set(point, -2)
                        count.warriors += 1
            elif item <= 0:
                grid.set(point, item + 1)
        point += diff
    return count


def calc_score(grid, width, height, diff, part):
    count = Status()
    dx = diff.x
    dy = diff.y

    side = (height - 1) // 2
    assert width == 4 * side + 1

    if dx > 0:
        for y in range(0, height):
            if dy == 0 or dy == 1 and y <= side or dy == -1 and y >= side:
                count += calc_line(
                    grid, width, height, diff, Vec2d(abs(y - side), y), part
                )
    if dx < 0:
        for y in range(0, height):
            if dy == 0 or dy == 1 and y <= side or dy == -1 and y >= side:
                count += calc_line(
                    grid, width, height, diff, Vec2d(width - 1 - abs(y - side), y), part
                )
    if dy > 0:
        for x in range(side, 3 * side + 2, 2):
            if dx > 0 and x == side or dx < 0 and x == 3 * side:
                continue  # avoid duplicating corner
            count += calc_line(grid, width, height, diff, Vec2d(x, 0), part)
    if dy < 0:
        for x in range(side, 3 * side + 2, 2):
            if dx > 0 and x == side or dx < 0 and x == 3 * side:
                continue  # avoid duplicating corner
            count += calc_line(grid, width, height, diff, Vec2d(x, height - 1), part)
    return count


def part_1(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file(input)
    return calc_score(grid, width, height, Vec2d(1, 1), part=1).energy


def part_2(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file(input)
    count = Status()
    diffs = [
        Vec2d(1, 1),
        Vec2d(-1, 1),
        Vec2d(-2, 0),
        Vec2d(-1, -1),
        Vec2d(1, -1),
        Vec2d(2, 0),
    ]
    for diff in diffs:
        count += calc_score(grid, width, height, diff, part=2)
    return count.energy


def part_3(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file(input)
    count = Status()
    army_size = 0
    diffs = [
        Vec2d(1, 1),
        Vec2d(-1, 1),
        Vec2d(-2, 0),
        Vec2d(-1, -1),
        Vec2d(1, -1),
        Vec2d(2, 0),
    ]

    round = 1
    while count.warriors < 100000:
        diff = diffs[(round - 1) % 6]
        count += calc_score(grid, width, height, diff, part=3)
        round += 1
    return count.energy


if __name__ == "__main__":
    Run_2026_08().run_cmdline()
