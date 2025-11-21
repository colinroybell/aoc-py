from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from utils.grid_2d import Grid2d
from collections import namedtuple


class Run_2025_12(DayBase):
    YEAR = "2025"
    DAY = "12"
    PREFIX = "ec"


def part_1(input, part=1):
    grid = Grid2d()
    width, height = grid.read_from_file_strings(input, make_int=True)

    count = 0
    stack = []
    stack.append(Vec2d(0, 0))
    if part == 2:
        stack.append(Vec2d(width - 1, height - 1))
    while stack:
        pos = stack.pop()
        this_value = grid.get(pos)
        if this_value == None:
            continue
        # print("Trying ",pos)
        for p in pos.get_adjacent_orthogonal():
            adj_value = grid.get(p)
            if adj_value != None and adj_value <= this_value:
                stack.append(p)
                # print("Adding",p,"via",adj_value,"<",this_value)
        count += 1
        grid.set(pos, None)
    return count


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    """The obvious way - find possible top points each round and see which is best.
    There ought to be a method of doing it with some sort of hierarchy so we don't keep having
    to search large chunks of the grid multiple times, but can't see a sensible way of handling this yet.

    Vague thought: from the 9s search from 8s down. If we have a 6 adjacent, we can go through the supernodes of it and see if the 8 is already in there? Or we do a per-level search, building a list of ids at each stage?
    """
    grid = Grid2d()
    width, height = grid.read_from_file_strings(input, make_int=True)

    score = 0
    for round in range(3):
        # print("round {}".format(round))
        best_count = 0
        best_group = {}
        done = Grid2d()
        for x in range(width):
            for y in range(height):
                pos = Vec2d(x, y)
                # First pass: reject if we're NULL (done on previous round), done (done on this round) or we have an adjacent higher value
                this_value = grid.get(pos)
                if this_value == None:
                    continue
                if done.get(pos):
                    continue

                for p in pos.get_adjacent_orthogonal():
                    adj_value = grid.get(p)
                    if adj_value != None and adj_value > this_value:
                        break
                else:
                    # print("trying from {}".format(pos))
                    count = 0
                    stack = [pos]
                    group = set()
                    while stack:
                        pos = stack.pop()
                        if pos in group:
                            continue
                        group.add(pos)
                        done.set(pos, True)
                        count += 1
                        this_value = grid.get(pos)
                        for p in pos.get_adjacent_orthogonal():
                            adj_value = grid.get(p)
                            if adj_value != None and adj_value <= this_value:
                                stack.append(p)
                    if count > best_count:
                        best_count = count
                        best_group = group
        score += best_count
        for p in best_group:
            grid.set(p, None)
    return score


if __name__ == "__main__":
    Run_2025_12().run_cmdline()
