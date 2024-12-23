from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2024_23(DayBase):
    YEAR = "2024"
    DAY = "23"


def part_a(input):
    connections = defaultdict(lambda: set())
    for line in input_generator(input):
        c0 = line[0:2]
        c1 = line[3:5]
        connections[c0].add(c1)
        connections[c1].add(c0)

    count = 0
    for c0, conn in connections.items():
        for c1 in conn:
            if c0 < c1:
                intersect = conn.intersection(connections[c1])
                for c2 in intersect:
                    if c1 < c2:
                        print(c0, c1, c2)
                        if c0[0] == "t" or c1[0] == "t" or c2[0] == "t":
                            count += 1
    return count


def recurse(connections, existing):
    if existing == []:
        new_c = connections.keys()
    else:
        new_c = connections[existing[0]]
        for e in existing[1:]:
            new_c = new_c.intersection(connections[e])

    best = ",".join(existing)
    for c in new_c:
        if existing and c < existing[-1]:
            continue
        pw = recurse(connections, existing + [c])
        if len(pw) > len(best):
            best = pw
    return best


def part_b(input):
    connections = defaultdict(lambda: set())
    for line in input_generator(input):
        c0 = line[0:2]
        c1 = line[3:5]
        connections[c0].add(c1)
        connections[c1].add(c0)

    return recurse(connections, [])


if __name__ == "__main__":
    Run_2024_23().run_cmdline()
