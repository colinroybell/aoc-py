from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2025_03(DayBase):
    YEAR = "2025"
    DAY = "03"
    PREFIX = "ec"


def part_1(input, part=1):
    text = next(input_generator(input))
    crates = [int(x) for x in text.split(",")]
    crates.sort()
    current = 0
    total = 0
    count = 0
    for c in crates:
        if c > current:
            total += c
            current = c
            count += 1
        if part == 2 and count == 20:
            break
    return total


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    text = next(input_generator(input))
    crates = [int(x) for x in text.split(",")]
    d = defaultdict(int)
    count = 0
    for c in crates:
        d[c] += 1
        count = max(count, d[c])
    return count


if __name__ == "__main__":
    Run_2025_03().run_cmdline()
