from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2021_12(DayBase):
    YEAR = "2021"
    DAY = "12"


def recurse(route, paths, second_cave, part_b):
    loc = route[-1]
    if loc == "end":
        return 1
    routes = 0
    for cave in paths[loc]:
        limit = 1
        if part_b and not second_cave and cave != "start" and cave != "end":
            limit = 2
        if route.count(cave) < limit or cave.upper() == cave:
            second_cave_sub = second_cave
            if route.count(cave) == 1 and not cave.upper() == cave:
                assert not second_cave_sub
                second_cave_sub = True
            route.append(cave)
            routes += recurse(route, paths, second_cave_sub, part_b)
            route.pop()
    return routes


def part_a(input, part_b=False):
    paths = defaultdict(lambda: [])
    for line in input_generator(input):
        (f, t) = line.split("-")
        paths[f].append(t)
        paths[t].append(f)

    route = ["start"]
    print(paths)
    return recurse(route, paths, False, part_b)


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_12().run_cmdline()
