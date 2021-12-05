from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2021_03(DayBase):
    YEAR = "2021"
    DAY = "03"


def part_a(input):
    counts = []
    first = True
    for line in input_generator(input):
        for pos in range(0, len(line)):
            if first:
                counts.append(defaultdict(int))
            bit = line[pos]
            counts[pos][bit] += 1
        first = False
    gamma = ""
    epsilon = ""
    for c in counts:
        print(c)
        gamma += max(c, key=c.get)
        epsilon += min(c, key=c.get)
    return int(gamma, 2) * int(epsilon, 2)


def oxygen_bit(counts):
    diff = counts["1"] - counts["0"]
    if diff >= 0:
        return "1"
    else:
        return "0"


def co2_bit(counts):
    diff = counts["1"] - counts["0"]
    if diff >= 0:
        return "0"
    else:
        return "1"


def recurse(entries, function):
    if len(entries) == 1:
        return entries[0]
    counts = defaultdict(int)
    for e in entries:
        counts[e[0]] += 1
    bit = function(counts)
    entries_reduced = [e[1:] for e in entries if e[0] == bit]
    return bit + recurse(entries_reduced, function)


def part_b(input):
    entries = []
    for line in input_generator(input):
        entries.append(line)
    oxygen = recurse(entries, oxygen_bit)
    co2 = recurse(entries, co2_bit)
    return int(oxygen, 2) * int(co2, 2)


if __name__ == "__main__":
    Run_2021_03().run_cmdline()
