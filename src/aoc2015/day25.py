from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2015_25(DayBase):
    YEAR = "2015"
    DAY = "25"


def locate(row, column):
    round = row + column
    round -= 2
    return (round * (round + 1)) // 2 + column


def lookup(row, column):

    count = locate(row, column) - 1
    base = 20151125
    mul = 252533
    mod = 33554393

    print(count)

    total = 1
    while count:
        if count % 2:
            total = (total * mul) % mod
        mul = (mul * mul) % mod
        count //= 2

    return (total * base) % mod


def part_a(input):
    parse_re = re.compile(r".*row (\d+).*column (\d+)")

    m = parse_re.match(next(input_generator(input)))
    row = int(m.group(1))
    column = int(m.group(2))

    for r in range(1, 7):
        for c in range(1, 7):
            print(r, c, lookup(r, c))

    return lookup(row, column)


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2015_25().run_cmdline()
