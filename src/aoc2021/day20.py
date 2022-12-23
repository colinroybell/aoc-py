from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2021_20(DayBase):
    YEAR = "2021"
    DAY = "20"


def part_a(input, steps=2):
    generator = input_generator(input)
    lookup = next(generator)
    print(lookup)
    _ = next(generator)
    grid = Grid2d()
    (x_end, y_end) = grid.read_from_generator(generator)
    x_start, y_start = 0, 0
    general = 0
    for step in range(steps):
        count = 0
        new_grid = Grid2d()
        # TODO: make these changes after the run and use the Vec2d bounding box logic to simplify code
        x_start -= 1
        y_start -= 1
        x_end += 1
        y_end += 1
        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                val = 0
                for ym in range(-1, 2):
                    for xm in range(-1, 2):
                        val *= 2
                        pixel = grid.get(Vec2d(x + xm, y + ym))
                        if (
                            x + xm < x_start + 1
                            or x + xm >= x_end - 1
                            or y + ym < y_start + 1
                            or y + ym >= y_end - 1
                        ):
                            pixel = general
                        if pixel == None:
                            pixel = 0
                        val += pixel
                if lookup[val] == "#":
                    new_grid.set(Vec2d(x, y), 1)
                    count += 1
                # print("{},{} val {}, count {}".format(x,y,val,count))

        grid = new_grid
        if lookup[0] == "#":
            general = 1 - general
        # print(grid.to_hash_dot(x_end,y_end,x_start=x_start,y_start=y_start))
    return count


def part_b(input):
    return part_a(input, steps=50)


if __name__ == "__main__":
    Run_2021_20().run_cmdline()
