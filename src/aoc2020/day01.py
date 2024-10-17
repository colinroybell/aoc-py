from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_01(DayBase):
    YEAR = "2020"
    DAY = "01"


def part_a(input):
    entry = set()
    for line in input_generator(input):
        val = int(line)
        entry.add(val)
        inverse = 2020 - val
        if inverse in entry:
            return val * inverse
    return 0


def part_b(input):
    entry = set()
    pairs = {}
    for line in input_generator(input):
        val = int(line)
        for e in entry:
            pairs[val + e] = val * e
        entry.add(val)
        inverse = 2020 - val
        if inverse in pairs:
            return val * pairs[inverse]
    return 0


if __name__ == "__main__":
    Run_2020_01().run_cmdline()
