from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2021_09(DayBase):
    YEAR = "2021"
    DAY = "09"


def lower(a, b):
    return b == None or a < b


def part_a(input):
    grid = Grid2d(unset=None)
    (x, y) = grid.read_from_file(input)

    score = 0
    for i in range(0, x):
        for j in range(0, y):
            ok = True
            base = Vec2d((i, j))
            h = grid.get(base)
            for d in "^>v<":
                adj = base.move(d)
                if not lower(h, grid.get(adj)):
                    ok = False
            if ok:
                print("starting from {}".format(base))
                score += 1 + h
    return score


def floodfill(base, grid):
    h = grid.get(base)
    count = 1
    grid.set(base, None)
    for d in "^>v<":
        adj = base.move(d)
        adj_h = grid.get(adj)
        if adj_h and adj_h < 9 and lower(h, adj_h):
            count += floodfill(adj, grid)
    return count


def part_b(input):
    grid = Grid2d(unset=None)
    (x, y) = grid.read_from_file(input)

    basin_sizes = []
    score = 0
    for i in range(0, x):
        for j in range(0, y):
            if grid.get(Vec2d((i, j))) == None:
                continue
            ok = True
            base = Vec2d((i, j))
            print("trying {}".format(base))
            h = grid.get(base)
            for d in "^>v<":
                adj = base.move(d)
                if not lower(h, grid.get(adj)):
                    ok = False
            if ok and h < 9:
                print("starting from {}".format(base))
                basin_sizes.append(floodfill(base, grid))
    basin_sizes.sort()
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


if __name__ == "__main__":
    Run_2021_09().run_cmdline()
