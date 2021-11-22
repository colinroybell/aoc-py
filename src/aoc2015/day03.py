import sys
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


def part_a(input, part_b=False):
    grid = Grid2d()
    vec = Vec2d((0, 0))
    rvec = Vec2d((0, 0))
    grid.increment(vec)
    if part_b:
        grid.increment(rvec)
    santa = True
    for line in input_generator(input):
        for char in line:
            if santa:
                vec = vec.move(char)
                grid.increment(vec)
                if part_b:
                    santa = False
            else:
                rvec = rvec.move(char)
                grid.increment(rvec)
                santa = True

    return grid.count_non_zero()


def part_b(input):
    return part_a(input, part_b=True)


def entry():
    if "a" in sys.argv:
        print(part_a("data/aoc2015/day03.txt"))
    if "b" in sys.argv:
        print(part_b("data/aoc2015/day03.txt"))


if __name__ == "__main__":
    entry()
