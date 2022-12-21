from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2022_06(DayBase):
    YEAR = "2022"
    DAY = "06"


def marker_position(string, count):
    pos = count
    while 1:
        substring = string[pos - count : pos]
        if len(set(substring)) == count:
            return pos
        pos += 1


def part_a(input):
    line = next(input_generator(input))
    return marker_position(line, 4)


def part_b(input):
    line = next(input_generator(input))
    return marker_position(line, 14)


if __name__ == "__main__":
    Run_2022_06().run_cmdline()
