from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_03(DayBase):
    YEAR = "2024"
    DAY = "03"
    PREFIX = "ec"


def part_1(input, part=1):
    grid = Grid2d()
    grid.read_from_hash_dot_file(input)
    (_, _, width, height) = grid.get_dimensions()
    depth = 1
    change = True
    count = 0
    dirs = "URDL"
    while change:
        change = False
        for x in range(width):
            for y in range(height):
                pos = Vec2d(x, y)
                print(pos)
                cur_depth = grid.get(pos)
                if cur_depth:
                    if depth == 1:
                        count += 1
                        change = True
                    elif cur_depth == depth - 1:
                        ok = True
                        if part == 1:
                            adjs = pos.get_adjacent_orthogonal()
                        else:
                            adjs = pos.get_adjacent_with_diagonals()
                        for adj in adjs:
                            adj_depth = grid.get(adj)
                            if adj_depth == None or adj_depth < depth - 1:
                                ok = False
                                break
                        if ok:
                            grid.set(pos, depth)
                            count += 1
                            change = True
        depth += 1
    return count


def part_2(input):
    return part_1(input)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2024_03().run_cmdline()
