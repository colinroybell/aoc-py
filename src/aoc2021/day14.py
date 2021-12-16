from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2021_14(DayBase):
    YEAR = "2021"
    DAY = "14"


def part_a(input, part_b=False):
    generator = input_generator(input)
    init = next(generator)
    _ = next(generator)
    trans = {}
    for line in generator:
        trans[line[0:2]] = line[-1]

    states = defaultdict(lambda: 0)
    # Look at pairs of successive items, so we have a nice recurrence.
    # The last item remains constant.
    for p in range(len(init) - 1):
        states[init[p : p + 2]] += 1

    count = 10
    if part_b:
        count = 40

    for step in range(count):
        new_states = defaultdict(lambda: 0)
        for s, v in states.items():
            mid = trans[s]
            new_states[s[0] + mid] += v
            new_states[mid + s[1]] += v
        states = new_states

    mols = defaultdict(lambda: 0)
    for s, v in states.items():
        mols[s[0]] += v
    # Add back the last item
    mols[init[-1]] += 1
    counts = [mols[mol] for mol in mols]
    return max(counts) - min(counts)


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_14().run_cmdline()
