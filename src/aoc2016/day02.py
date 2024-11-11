from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from utils.grid_2d import Grid2d


class Run_2016_02(DayBase):
    YEAR = "2016"
    DAY = "02"


def part_a(input, part_b=False):
    grid = Grid2d()
    if not part_b:
        grid.set(Vec2d(0, 0), "1")
        grid.set(Vec2d(1, 0), "2")
        grid.set(Vec2d(2, 0), "3")
        grid.set(Vec2d(0, 1), "4")
        grid.set(Vec2d(1, 1), "5")
        grid.set(Vec2d(2, 1), "6")
        grid.set(Vec2d(0, 2), "7")
        grid.set(Vec2d(1, 2), "8")
        grid.set(Vec2d(2, 2), "9")
        v = Vec2d(1, 1)
    else:
        grid.set(Vec2d(2, 0), "1")
        grid.set(Vec2d(1, 1), "2")
        grid.set(Vec2d(2, 1), "3")
        grid.set(Vec2d(3, 1), "4")
        grid.set(Vec2d(0, 2), "5")
        grid.set(Vec2d(1, 2), "6")
        grid.set(Vec2d(2, 2), "7")
        grid.set(Vec2d(3, 2), "8")
        grid.set(Vec2d(4, 2), "9")
        grid.set(Vec2d(1, 3), "A")
        grid.set(Vec2d(2, 3), "B")
        grid.set(Vec2d(3, 3), "C")
        grid.set(Vec2d(2, 4), "D")
        v = Vec2d(0, 2)

    code = ""
    for line in input_generator(input):
        for c in line:
            cand = v.move_y_flipped(c)
            if grid.get(cand):
                v = cand

        code += grid.get(v)
    return code


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2016_02().run_cmdline()
