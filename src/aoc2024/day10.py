from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_10(DayBase):
    YEAR = "2024"
    DAY = "10"


def part_a(input, part_b=False):
    grid = Grid2d()
    heads_grid = Grid2d()
    counts = Grid2d()
    nums = [[] for _ in range(10)]
    width, height = grid.read_from_file(input)
    for y in range(height):
        for x in range(width):
            p = Vec2d(x, y)
            v = grid.get(p)
            if v != None:
                nums[v].append(p)
            counts.set(p, 0)
            heads_grid.set(p, set())

    total = 0
    for round in range(9, -1, -1):
        for v in nums[round]:
            if round == 9:
                count = 1
                heads = set([v])
            else:
                count = counts.get(v)
                heads = heads_grid.get(v)
            if round == 0:
                if part_b:
                    total += count
                else:
                    total += len(heads)
            else:
                adjs = v.get_adjacent_orthogonal()
                for a in adjs:
                    if grid.get(a) == round - 1:
                        val = counts.get(a) + count
                        counts.set(a, val)
                        pre_heads = heads_grid.get(a)
                        pre_heads.update(heads)
                        heads_grid.set(a, pre_heads)
    return total


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2024_10().run_cmdline()
