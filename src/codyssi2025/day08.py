from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2025_08(DayBase):
    YEAR = "2025"
    DAY = "08"
    PREFIX = "codyssi"


def count_alpha(c):
    return 1 if c.isalpha() else 0


def part_1(input):
    total = 0
    for line in input_generator(input):

        fn = count_alpha

        total += sum(fn(c) for c in line)
    return total


def isalphahyphen(c, part=2):
    return c.isalpha() or c == "-" and part == 2


def reduce(line, part=2):
    out = ""
    for c in line:
        if len(out) > 0:
            last = out[-1]
            reduce = False
            if (last.isnumeric() and isalphahyphen(c, part)) or (
                c.isnumeric() and isalphahyphen(last, part)
            ):
                out = out[:-1]
                continue
        out += c
    return out


def part_2(input, part=2):
    total = 0
    for line in input_generator(input):
        line = reduce(line, part)
        total += len(line)
    return total


def part_3(input):
    return part_2(input, part=3)


if __name__ == "__main__":
    Run_2025_08().run_cmdline()
