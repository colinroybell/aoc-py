from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_04(DayBase):
    YEAR = "2025"
    DAY = "04"
    PREFIX = "codyssi"


def part_1(input):
    total = 0
    for line in input_generator(input):
        for c in line:
            total += ord(c) - 64
    return total


def part_2(input):
    total = 0
    for line in input_generator(input):
        length = len(line)
        keep = length // 10
        for c in line[:keep] + line[-keep:]:
            total += ord(c) - 64
        remain = str(length - keep * 2)
        for c in remain:
            total += ord(c) - 48
    return total


def part_3(input):
    total = 0
    for line in input_generator(input):
        line += "$"
        current = None
        count = 0
        for c in line:
            if c != current:
                if current:
                    total += ord(current) - 64
                    for cc in str(count):
                        total += ord(cc) - 48
                current = c
                count = 0
            count += 1
    return total


if __name__ == "__main__":
    Run_2025_04().run_cmdline()
