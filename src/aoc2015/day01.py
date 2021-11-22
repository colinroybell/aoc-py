import sys
from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_01(DayBase):
    YEAR = "2015"
    DAY = "01"


def part_a(input, part_b=False):
    floor = 0
    count = 1
    for line in input_generator(input):
        for char in line:
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1
            if part_b and floor == -1:
                return count
            count += 1
    assert not part_b
    return floor


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
      Run_2015_01().run_cmdline()
