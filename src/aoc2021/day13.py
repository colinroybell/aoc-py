from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
import re


class Run_2021_13(DayBase):
    YEAR = "2021"
    DAY = "13"


def part_a(input, part_b=False):
    grid = Grid2d(unset=0)

    width = 0
    height = 0

    generator = input_generator(input)
    for line in generator:
        if not line:
            break
        coords = line.split(",")
        x = int(coords[0])
        y = int(coords[1])
        grid.set(Vec2d((x, y)), 1)
        if x >= width:
            width = x + 1
        if y >= height:
            height = y + 1

    fold_re = re.compile(r"fold along (.)=(\d+)")
    for line in generator:
        m = fold_re.match(line)
        print(line)
        assert m
        dir = m.group(1)
        val = int(m.group(2))

        if dir == "y":
            for x in range(0, width):
                for y in range(val + 1, height):
                    pos = Vec2d((x, y))
                    pos_ref = Vec2d((x, 2 * val - y))
                    if grid.get(pos):
                        grid.unset(pos)
                        grid.set(pos_ref, 1)
            height = val
        else:
            for x in range(val + 1, width):
                for y in range(0, height):
                    pos = Vec2d((x, y))
                    pos_ref = Vec2d((2 * val - x, y))
                    if grid.get(pos):
                        grid.unset(pos)
                        grid.set(pos_ref, 1)
            width = val
        if not part_b:
            return grid.count_non_zero()
    print(width, height)
    print(grid.to_hash_dot(width, height))
    return grid.to_hash_dot(width, height)


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_13().run_cmdline()
