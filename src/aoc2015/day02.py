from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2015_02(DayBase):
    YEAR = "2015"
    DAY = "02"


def score(d_in, function):
    d = [int(s) for s in d_in]
    d.sort()
    return function(d)


def part_a(input, part_b=False):
    if not part_b:
        score_function = (
            lambda d: 2 * (d[0] * d[1] + d[0] * d[2] + d[1] * d[2]) + d[0] * d[1]
        )
    else:
        score_function = lambda d: 2 * (d[0] + d[1]) + d[0] * d[1] * d[2]
    total = 0
    for line in input_generator(input):
        d = line.split("x")
        total += score(d, score_function)
    return total


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2015_02().run_cmdline()
