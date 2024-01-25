from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_05(DayBase):
    YEAR = "2017"
    DAY = "05"


def part_a(input, part_b=False):
    n = [int(line) for line in input_generator(input)]
    count = 0
    pos = 0
    length = len(n)
    while pos < length:
        offset = n[pos]
        if part_b and offset >= 3:
            n[pos] -= 1
        else:
            n[pos] += 1
        pos += offset
        count += 1
    return count


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_05().run_cmdline()
