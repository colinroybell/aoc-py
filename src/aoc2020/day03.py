from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_03(DayBase):
    YEAR = "2020"
    DAY = "03"


def read_grid(input):
    grid = [x.strip() for x in input_generator(input)]
    return grid


def count_grid(grid, xstep, ystep):
    count = 0
    x = 0
    y = 0
    width = len(grid[0])
    while y < len(grid):
        if grid[y][x] == "#":
            count += 1
        x = (x + xstep) % width
        y += ystep

    return count


def part_a(input):
    grid = read_grid(input)
    return count_grid(grid, 3, 1)


def part_b(input):
    grid = read_grid(input)
    return (
        count_grid(grid, 1, 1)
        * count_grid(grid, 3, 1)
        * count_grid(grid, 5, 1)
        * count_grid(grid, 7, 1)
        * count_grid(grid, 1, 2)
    )


if __name__ == "__main__":
    Run_2020_03().run_cmdline()
