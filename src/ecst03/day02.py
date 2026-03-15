from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from collections import namedtuple


class Run_st03_02(DayBase):
    YEAR = "st03"
    DAY = "02"
    PREFIX = "ec"


class GridLimits:
    def __init__(self, x, y):
        self.min_x = x
        self.max_x = x
        self.min_y = y
        self.max_y = y


def update_grids(part, grid, grid_limits, pos):
    print("Setting", pos)
    grid.set(pos, "+")
    if part == 1:
        return
    grid_limits.min_x = min(grid_limits.min_x, pos.x)
    grid_limits.max_x = max(grid_limits.max_x, pos.x)
    grid_limits.min_y = min(grid_limits.min_y, pos.y)
    grid_limits.max_y = max(grid_limits.max_y, pos.y)
    adjs = [
        Vec2d(1, 0),
        Vec2d(1, 1),
        Vec2d(0, 1),
        Vec2d(-1, 1),
        Vec2d(-1, 0),
        Vec2d(-1, -1),
        Vec2d(0, -1),
        Vec2d(1, -1),
    ]
    adj_pos = []
    adj_char = []
    for a in adjs:
        adj_pos.append(pos + a)
        adj_char.append(grid.get(pos + a))
    region_starts = []
    for i in range(8):
        if adj_char[i] == None and adj_char[(i - 1) % 8] != None:
            region_starts.append(adj_pos[i])
    print(adj_pos, adj_char)
    print(grid_limits.min_x, grid_limits.max_x, grid_limits.min_y, grid_limits.max_y)
    if len(region_starts) > 1:
        for r in region_starts:
            block = []
            cands = [r]

            outside = False
            while cands and not outside:
                c = cands.pop()
                if c in block:
                    next
                block.append(c)
                for a in c.get_adjacent_orthogonal():
                    if (
                        a.x < grid_limits.min_x
                        or a.x > grid_limits.max_x
                        or a.y < grid_limits.min_y
                        or a.y > grid_limits.max_y
                    ):
                        outside = True
                    if a not in block and grid.get(a) == None:
                        cands.append(a)
            if not outside:
                print("Surrounded:", block)
                for b in block:
                    grid.set(b, "+")


def part_1(input, part=1):
    start = None
    targets = []
    count_adj = 0
    for y, line in enumerate(input_generator(input)):
        for x, c in enumerate(line):
            if c == "#":
                targets.append(Vec2d(x, y))
            if c == "@":
                start = Vec2d(x, y)

    grid = Grid2d()
    grid_limits = GridLimits(start.x, start.y)
    update_grids(part, grid, grid_limits, start)
    if part == 2:
        for t in targets:
            update_grids(part, grid, grid_limits, t)
    pos = start
    steps = 0
    last_steps = None
    if part < 3:
        dirs = "URDL"
    else:
        dirs = "UUURRRDDDLLL"
    while 1:
        if steps == 10000 or steps == last_steps:
            return 0
        last_steps = steps
        for d in dirs:
            new_pos = pos.move_y_flipped(d)
            if grid.get(new_pos) == None:
                print(d, new_pos)
                pos = new_pos
                steps += 1
                update_grids(part, grid, grid_limits, new_pos)

                pos = new_pos
                if part == 1:
                    if pos == targets[0]:
                        return steps
                else:
                    done = True
                    for t in targets:
                        for a in t.get_adjacent_orthogonal():
                            print(a, grid.get(a))
                            if grid.get(a) == None:
                                done = False
                                break
                        if not done:
                            break
                    else:
                        return steps


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_st03_02().run_cmdline()
