from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2015_18(DayBase):
    YEAR = "2015"
    DAY = "18"


def corners_on(grid, width, height):
    grid.set(Vec2d(0, 0), 1)
    grid.set(Vec2d(width - 1, 0), 1)
    grid.set(Vec2d(0, height - 1), 1)
    grid.set(Vec2d(width - 1, height - 1), 1)


def part_a(input, part_b=False, steps=100):
    grid = Grid2d()
    generator = input_generator(input)
    (width, height) = grid.read_from_generator(generator)

    for _ in range(steps):
        if part_b:
            corners_on(grid, width, height)
        print(grid.to_hash_dot(width, height))
        new_grid = Grid2d()
        for y in range(height):
            for x in range(width):
                p = Vec2d(x, y)
                current = grid.get(p)
                adj = p.get_adjacent_diagonals()
                count = 0
                for a in adj:
                    if grid.get(a):
                        count += 1
                if count == 3 or current and count == 2:
                    new_grid.set(p, 1)
        grid = new_grid

    if part_b:
        corners_on(grid, width, height)
    count = 0
    for y in range(height):
        for x in range(width):
            if grid.get(Vec2d(x, y)):
                count += 1
    return count


def part_b(input, steps=100):
    return part_a(input, part_b=True, steps=steps)


if __name__ == "__main__":
    Run_2015_18().run_cmdline()
