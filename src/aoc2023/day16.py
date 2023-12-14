from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2023_16(DayBase):
    YEAR = "2023"
    DAY = "16"


def update_dir(dir, obj):
    n = "^>v<".index(dir)
    # TODO: y flip problem so
    if obj == "\\":  # should be /
        return [">", "^", "<", "v"][n]
    if obj == "/":  # should be \\
        return ["<", "v", ">", "^"][n]
    if obj == "-":
        return ["<>", ">", "<>", "<"][n]
    if obj == "|":
        return ["^", "^v", "v", "^v"][n]
    assert obj == "."
    return dir


def score(grid, start_point, start_dir):
    grid_out = Grid2d()
    queue = [(start_point, start_dir)]
    while queue:
        (pos, dir) = queue.pop()
        cache = grid_out.get(pos)
        if cache and dir in grid_out.get(pos):
            # Already done
            continue
        grid_out.append(pos, dir)
        pos = pos.move(dir)
        obj = grid.get(pos)
        if obj == None:
            # Off grid
            continue
        new_dirs = update_dir(dir, obj)
        for d in new_dirs:
            queue.append((pos, d))
    # We've included the start position off grid, so remove 1
    return grid_out.count_function(lambda v: 1) - 1


def part_a(input):
    grid = Grid2d()
    grid.read_from_file_strings(input)
    return score(grid, Vec2d(-1, 0), ">")


def part_b(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    maximum = None
    candidates = []

    def candidate_iterator(width, height):
        for x in range(width):
            # TODO: same directional issue
            yield (Vec2d(x, -1), "^")
            yield (Vec2d(x, height), "v")
        for y in range(height):
            yield (Vec2d(-1, y), ">")
            yield (Vec2d(width, y), "<")

    candidates = candidate_iterator(width, height)

    for cand in candidates:
        count = score(grid, cand[0], cand[1])
        print(cand, count)
        if maximum == None or count > maximum:
            maximum = count

    return maximum


if __name__ == "__main__":
    Run_2023_16().run_cmdline()
