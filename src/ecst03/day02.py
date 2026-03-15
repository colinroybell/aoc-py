from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from collections import namedtuple
import re


class Run_st03_02(DayBase):
    YEAR = "st03"
    DAY = "02"
    PREFIX = "ec"

    NOTES = """

    We find out whether something is enclosed by seeing if we've changed topology, but we then floodfill to the outside to see if it needs removing.
    
    A better approach would be to maintain a list of directions which give each square's route to the outside, and where there's a blockage, do some sort
    of search to find an alternative, flip things to point to that place (or if we can't find one, we know we are enclosed).

    Have a function which generates these based on bounding box of what we already have.

    We can probably do the enclosure of # by the same route - track a route out from those, and kill it if blocked. What we have currently is to search
    every iteration, which is very inefficient.
    
"""


class GridLimits:
    def __init__(self, x, y):
        self.min_x = x
        self.max_x = x
        self.min_y = y
        self.max_y = y


def update_grids(part, grid, grid_limits, pos):
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
                for b in block:
                    grid.set(b, "+")


def part_1(input, part=1, **kwargs):
    start = None
    targets = []
    count_adj = 0
    for y, line in enumerate(input_generator(input)):
        for x, c in enumerate(line):
            if c == "#":
                targets.append(Vec2d(x, y))
            if c == "@":
                start = Vec2d(x, y)

    expected_dirs = []
    if "trace" in kwargs:
        dir_re = re.compile(r"Next.*\[(.)")
        conv = {"↑": "U", "→": "R", "↓": "D", "←": "L"}
        for line in input_generator(kwargs["trace"]):
            m = dir_re.match(line)
            if m:
                char = m.group(1)
                expected_dirs.append(conv[char])

    grid = Grid2d()
    grid_limits = GridLimits(start.x, start.y)
    update_grids(part, grid, grid_limits, start)
    if part > 1:
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
                if expected_dirs:
                    assert d == expected_dirs[steps]
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
                            if grid.get(a) == None:
                                done = False
                                break
                        if not done:
                            break
                    else:
                        return steps


def part_2(input):
    return part_1(input, part=2)


def part_3(input, **kwargs):
    return part_1(input, part=3, **kwargs)


if __name__ == "__main__":
    Run_st03_02().run_cmdline()
