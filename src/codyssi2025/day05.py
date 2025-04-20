from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
import re


class Run_2025_05(DayBase):
    YEAR = "2025"
    DAY = "05"
    PREFIX = "codyssi"


def part_1(input):
    parse_re = re.compile(r"\((.+),(.+)\)")
    distances = []
    home = Vec2d(0, 0)
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        island = Vec2d(int(m.group(1)), int(m.group(2)))
        distances.append(home.manhattan(island))

    return max(distances) - min(distances)


def orth_closest(i, j):
    return i.x < j.x or (i.x == j.x and i.y < j.y)


def part_2(input, part=2):
    parse_re = re.compile(r"\((.+),(.+)\)")
    distances = []
    islands = set()
    home = Vec2d(0, 0)
    best = None
    closest = None
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        island = Vec2d(int(m.group(1)), int(m.group(2)))
        islands.add(island)

    total = 0
    base = home
    count = 0
    while len(islands):
        count += 1
        best = None
        closest = None
        for island in islands:
            d = base.manhattan(island)
            if (
                best == None
                or d < best
                or (d == best and orth_closest(island, closest))
            ):
                best = d
                closest = island
                print(best, closest, island)
        if part == 2 and count == 2:
            return best

        total += best

        islands.remove(closest)
        base = closest

    return total


def part_3(input):
    return part_2(input, part=3)


if __name__ == "__main__":
    Run_2025_05().run_cmdline()
