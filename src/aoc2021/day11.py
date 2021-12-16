from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2021_11(DayBase):
    YEAR = "2021"
    DAY = "11"


def part_a(input, days=100, part_b=False):
    grid = Grid2d(unset=None)
    (width, height) = grid.read_from_file(input)

    count = 0
    step = 0
    while (not part_b and step < days) or part_b:
        inc_list = []
        flash_list = []
        for x in range(0, width):
            for y in range(0, height):
                inc_list.append(Vec2d(x, y))

        while inc_list:
            v = inc_list.pop()
            if v not in grid or v in flash_list:
                continue
            grid.increment(v)
            if grid.get(v) >= 10:
                count += 1
                grid.set(v, 0)
                inc_list.extend(v.get_adjacent_diagonals())
                flash_list.append(v)
        print(grid)
        step += 1
        if part_b and len(flash_list) == width * height:
            print(step, len(flash_list))
            # all have flashed
            return step

    return count


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_11().run_cmdline()
