from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
import re


class Run_2021_05(DayBase):
    YEAR = "2021"
    DAY = "05"


def part_a(input, part_b=False):
    parse_re = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    grid = Grid2d()
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        x1 = int(m.group(1))
        y1 = int(m.group(2))
        x2 = int(m.group(3))
        y2 = int(m.group(4))

        if x1 != x2 and y1 != y2 and not part_b:
            continue

        def dir(v1, v2):
            if v2 > v1:
                return 1
            elif v2 < v1:
                return -1
            else:
                return 0

        dx = dir(x1, x2)
        dy = dir(y1, y2)
        len = max(abs(x2 - x1), abs(y2 - y1))

        for p in range(0, len + 1):
            grid.increment(Vec2d(x1 + p * dx, y1 + p * dy))

    def gtr1(v):
        return v > 1

    return grid.count_function(gtr1)


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2021_05().run_cmdline()
