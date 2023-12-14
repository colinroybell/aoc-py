from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2023_14(DayBase):
    YEAR = "2023"
    DAY = "14"


def part_a(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    score = 0
    for x in range(width):
        last_gap = 0
        for y in range(height):
            c = grid.get(Vec2d(x, y))
            if c == "#":
                print("set last_gap", y + 1)
                last_gap = y + 1
            elif c == "O":
                print("place at", x, last_gap)
                score += height - last_gap
                last_gap += 1
    return score


def loading_score(grid):
    score = 0
    for x in range(width):
        for y in range(height):
            if c == "O":
                score += height - y
    return score


def part_b(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)

    round = 0
    cache = []

    while 1:
        cache_entry = []
        score = 0
        for x in range(width):
            for y in range(height):
                c = grid.get(Vec2d(x, y))
                if c == "O":
                    cache_entry.append((x, y))
                    score += height - y
        cache_entry.append(score)
        cache.append(cache_entry)
        for r in range(round):
            if cache_entry == cache[r]:
                e = ((1000000000 - r) % (round - r)) + r
                return cache[e][-1]

        # print('N')
        for x in range(width):
            last_gap = 0
            for y in range(height):
                c = grid.get(Vec2d(x, y))
                if c == "#":
                    last_gap = y + 1
                elif c == "O":
                    # print(x,last_gap)
                    if last_gap != y:
                        grid.set(Vec2d(x, last_gap), "O")
                        grid.set(Vec2d(x, y), ".")
                    last_gap += 1
        # print('W')
        # W
        for y in range(height):
            last_gap = 0
            for x in range(width):
                c = grid.get(Vec2d(x, y))
                if c == "#":
                    last_gap = x + 1
                elif c == "O":
                    # print(last_gap,y)
                    if last_gap != x:
                        grid.set(Vec2d(last_gap, y), "O")
                        grid.set(Vec2d(x, y), ".")
                    last_gap += 1
        # print('S')

        # S
        for x in range(width):
            last_gap = height - 1
            for y in range(height - 1, -1, -1):
                c = grid.get(Vec2d(x, y))
                if c == "#":
                    last_gap = y - 1
                elif c == "O":
                    # print(x,y, 'to',x,last_gap)
                    if last_gap != y:
                        grid.set(Vec2d(x, last_gap), "O")
                        grid.set(Vec2d(x, y), ".")
                    last_gap -= 1
        # E
        # print('E')
        for y in range(height):
            last_gap = width - 1
            for x in range(width - 1, -1, -1):
                c = grid.get(Vec2d(x, y))
                if c == "#":
                    last_gap = x - 1
                elif c == "O":
                    # print(last_gap,y)
                    if last_gap != x:
                        grid.set(Vec2d(last_gap, y), "O")
                        grid.set(Vec2d(x, y), ".")
                    last_gap -= 1
        round += 1


if __name__ == "__main__":
    Run_2023_14().run_cmdline()
