from utils.day_base import DayBase
from utils.data_input import input_generator
from math import ceil


class Run_2025_04(DayBase):
    YEAR = "2025"
    DAY = "04"
    PREFIX = "ec"


def part_1(input, part=1):
    gears = []
    for line in input_generator(input):
        gears.append(int(line))
    if part == 1:
        return (2025 * gears[0]) // gears[-1]
    else:
        return ceil((10000000000000 * gears[-1]) / gears[0])


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    first = None
    last = None
    mul = 1
    for line in input_generator(input):
        if not first:
            first = int(line)
        if "|" in line:
            a, b = [int(n) for n in line.split("|")]
            assert b % a == 0
            mul *= b // a
        else:
            last = int(line)

    return (100 * first * mul) // last


if __name__ == "__main__":
    Run_2025_04().run_cmdline()
