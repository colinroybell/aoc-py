from utils.day_base import DayBase
from utils.data_input import input_generator
from math import sqrt, ceil


class Run_2026_01(DayBase):
    YEAR = "2026"
    DAY = "01"
    PREFIX = "ec"


def extras(part, n):
    if part == 1:
        root = ceil(sqrt(n))
        return root * root - n
    elif part == 2:
        size = max(2, ceil(n / 4))
        return size * 4 - n
    elif part == 3:
        root = ceil(sqrt(n + 1))
        if root % 2 == 0:
            root += 1
        return root * root - 1 - n


def part_1(input, part=1):
    generator = input_generator(input)
    line = next(generator)
    counts = line.split(",")
    required = 0
    for c in counts:
        n = int(c)
        root = ceil(sqrt(n))
        required += extras(part, n)
    return required


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2026_01().run_cmdline()
