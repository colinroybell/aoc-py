from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2021_15(DayBase):
    YEAR = "2021"
    DAY = "15"


def part_a(input, part_b=False):
    grid = Grid2d(None)
    (width, height) = grid.read_from_file(input)

    if part_b:
        for x in range(width, 5 * width):
            for y in range(0, height):
                pos_from = Vec2d(x - width, y)
                pos_to = Vec2d(x, y)
                val = grid.get(pos_from) + 1
                if val > 9:
                    val = 1
                grid.set(pos_to, val)
        for x in range(0, 5 * width):
            for y in range(height, 5 * height):
                pos_from = Vec2d(x, y - height)
                pos_to = Vec2d(x, y)
                val = grid.get(pos_from) + 1
                if val > 9:
                    val = 1
                grid.set(pos_to, val)
        width *= 5
        height *= 5

    start = Vec2d(0, 0)
    end = Vec2d(width - 1, height - 1)
    val_grid = Grid2d(None)
    to_process = PriorityQueue()
    to_process.put((0, start))
    val_grid.set(start, 0)

    while not to_process.empty():
        (cost, pos) = to_process.get()
        if cost > val_grid.get(pos):
            # We've already got a better cost for this square
            continue
        for v in pos.get_adjacent_orthogonal():
            if v not in grid:
                continue
            trial_cost = cost + grid.get(v)
            current_cost = val_grid.get(v)
            if current_cost == None or trial_cost < current_cost:
                val_grid.set(v, trial_cost)
                to_process.put((trial_cost, v))
    return val_grid.get(end)


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_15().run_cmdline()
