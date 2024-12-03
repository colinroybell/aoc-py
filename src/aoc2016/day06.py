from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2016_06(DayBase):
    YEAR = "2016"
    DAY = "06"


def most_common(counts):
    sorted_items = sorted(list(counts.items()), key=lambda x: -x[1])
    return sorted_items[0][0]


def least_common(counts):
    sorted_items = sorted(list(counts.items()), key=lambda x: -x[1])
    return sorted_items[-1][0]


def part_a(input, part_b=False):
    part_a = not part_b
    counts = []
    for line in input_generator(input):
        if counts == []:
            counts = [defaultdict(lambda: 0) for _ in range(len(line))]
        for i, c in enumerate(line):
            counts[i][c] += 1

    output = ""
    for i in range(len(counts)):
        if part_a:
            output += most_common(counts[i])
        else:
            output += least_common(counts[i])
    return output


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2016_06().run_cmdline()
