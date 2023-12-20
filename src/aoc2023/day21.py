from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2023_21(DayBase):
    YEAR = "2023"
    DAY = "21"


# How to do it:
# 1. Process blocks orthogonally, copying over edges (which we represent as array plus offset)
# 2. Then subtract off a minimum value, which means we can cache
# 3. For 5000 case in part b we will need to do some pattern spotting, and this can extend
#    to big case, which we might need to do partly by hand
#
# Parity of steps might flip between blocks which could complicate things


def process_block(grid, steps, queue):
    count = 0
    while not queue.empty():
        (s, pos) = queue.get()
        if grid.get(pos) != ".":
            continue
        grid.set(pos, s)
        if s % 2 == 0:
            count += 1
        if s <= steps:
            vecs = pos.get_adjacent_orthogonal()
            for v in vecs:
                queue.put((s + 1, v))
    return count


def part_a(input, steps=64):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    for x in range(width):
        for y in range(height):
            if grid.get(Vec2d(x, y)) == "S":
                start_x = x
                start_y = y
                grid.set(Vec2d(x, y), ".")
    count = 0
    steps_parity = steps % 2
    queue = PriorityQueue()
    queue.put((0, Vec2d(start_x, start_y)))

    return process_block(grid, steps, queue)


def part_b(input, steps=26501365):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2023_21().run_cmdline()
