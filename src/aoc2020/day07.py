from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_07(DayBase):
    YEAR = "2020"
    DAY = "07"


def parse_file(input):
    down = {}
    up = {}
    for line in input_generator(input):
        fields = line.split()
        bag = fields[0] + " " + fields[1]
        pos = 4
        down[bag] = []
        while (pos + 3) < len(fields):
            count = int(fields[pos])
            subbag = fields[pos + 1] + " " + fields[pos + 2]
            if bag in down:
                down[bag].append((count, subbag))
            else:
                down[bag] = [(count, subbag)]
            if bag not in up:
                up[bag] = []
            if subbag in up:
                up[subbag].append((count, bag))
            else:
                up[subbag] = [(count, bag)]
            pos += 4
    return (down, up)


def compute_holders(up, bag):
    holders = set()
    holders.add(bag)
    for (count, superbag) in up[bag]:
        ret = compute_holders(up, superbag)
        holders = holders.union(ret)
    return holders


# note: caching the answers would be more efficient, but for our
# case it runs more or less instantly anyway
def compute_held(down, bag):
    total = 1
    for (count, subbag) in down[bag]:
        total += count * compute_held(down, subbag)
    return total


def part_a(input):
    (down, up) = parse_file(input)
    holders = compute_holders(up, "shiny gold")
    return len(holders) - 1


def part_b(input):
    (down, up) = parse_file(input)
    held = compute_held(down, "shiny gold")
    return held - 1


if __name__ == "__main__":
    Run_2020_07().run_cmdline()
