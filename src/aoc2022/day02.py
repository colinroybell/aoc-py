from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2022_02(DayBase):
    YEAR = "2022"
    DAY = "02"


def score(a, b):
    diff = (b - a + 3) % 3
    win = {1: 6, 2: 0, 0: 3}
    return win[diff] + b


def find_option(a, b):
    return ((a + b + 1 - 1) % 3) + 1


def part_a(input, part_b=False):
    total = 0
    for line in input_generator(input):
        them = ord(line[0]) - ord("A") + 1
        us = ord(line[2]) - ord("X") + 1
        if part_b:
            print(them, us)
            us = find_option(them, us)
            print(us)
        total += score(them, us)
    return total


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2022_02().run_cmdline()
