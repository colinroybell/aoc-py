from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict
from utils.vec_2d import Vec2d


class Run_2024_08(DayBase):
    YEAR = "2024"
    DAY = "08"


def in_grid(pos, width, height):
    return 0 <= pos.x < width and 0 <= pos.y < height


def part_a(input, part_b=False):
    part_a = not part_b
    nodes = defaultdict(lambda: [])
    y = 0
    for line in input_generator(input):
        width = len(line)
        for x in range(width):
            c = line[x]
            if c != ".":
                nodes[c].append(Vec2d(x, y))
        y += 1

    height = y
    antinodes = set()
    for code, locations in nodes.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                loc1 = locations[i]
                loc2 = locations[j]
                diff = loc1 - loc2

                if part_a:
                    pos1 = loc1 + diff
                    pos2 = loc2 - diff
                    if in_grid(pos1, width, height):
                        antinodes.add(pos1)
                    if in_grid(pos2, width, height):
                        antinodes.add(pos2)

                if part_b:
                    pos = loc1
                    while in_grid(pos, width, height):
                        antinodes.add(pos)
                        pos += diff
                    pos = loc2
                    while in_grid(pos, width, height):
                        antinodes.add(pos)
                        pos -= diff
    return len(antinodes)


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2024_08().run_cmdline()
