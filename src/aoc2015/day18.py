from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2015_18(DayBase):
    YEAR = "2015"
    DAY = "18"


def part_a(input):
    grid = Grid2d()
    generator = input_generator(input)
    (width, height) = grid.read_from_generator(generator)
    for _ in range(100):
        pass


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2015_18().run_cmdline()
