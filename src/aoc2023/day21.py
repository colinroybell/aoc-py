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

# What we are hoping for is a central block and eight parametrised side blocks, all with
# the same i/o pattern (maybe flipped parity), then we can just compute things.
#
# Nicely parametrising the edge cases is going to be helpful.


def process_block(grid, steps, queue):
    count = 0
    current_s = None
    while not queue.empty():
        (s, pos) = queue.get()
        if s != current_s:
            print("current s", s)
            current_s = s
        if grid.get(pos) != ".":
            continue
        grid.set(pos, s)
        if s % 2 == 0:
            count += 1
        if s < steps:
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

    queue = PriorityQueue()
    queue.put((0, Vec2d(start_x, start_y)))

    return process_block(grid, steps, queue)


# NB: code working, but could be faster: we probably compute more rounds than is necessary,
# so ought to combine the grid search with the diff comparison.
# Maybe we extend the grid only when needed as well?
# For the tests, ought to cache the computations.
#
# Currently runs everything in about 90s


def part_b(input, steps=26501365):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    for x in range(width):
        for y in range(height):
            if grid.get(Vec2d(x, y)) == "S":
                start_x = x
                start_y = y
                grid.set(Vec2d(x, y), ".")

    max_rounds = 7  # empirically enough
    for x in range(width):
        for y in range(height):
            c = grid.get(Vec2d(x, y))
            for xb in range(-max_rounds, max_rounds + 1):
                for yb in range(-max_rounds, max_rounds + 1):
                    grid.set(Vec2d(x + xb * width, y + yb * width), c)

    queue = PriorityQueue()
    queue.put((0, Vec2d(start_x, start_y)))

    max_steps = max_rounds * width
    process_block(grid, max_steps, queue)
    counts = [0 for i in range(max_steps + 1)]
    for c in grid.c.values():
        if isinstance(c, int):
            print(c)
            counts[c] += 1

    sigmas = [0 for i in range(max_steps + 1)]
    diffs = []
    base = None
    for i in range(0, max_steps + 1):
        sigmas[i] = counts[i]
        if i >= 2:
            sigmas[i] += sigmas[i - 2]
        if i < width:
            diffs.append(0)
        else:
            diffs.append(
                (sigmas[i] - sigmas[i - 1])
                - (sigmas[i - width] - sigmas[i - width - 1])
            )
            print(i, sigmas[i], counts[i], diffs[i])
            if i >= 2 * width and not base:
                ok = True
                for j in range(i - width + 1, i + 1):
                    if diffs[j] != diffs[j - width]:
                        ok = False
                        break
                if ok:
                    base = i - 2 * width
                    print("Base", base)

    quad_term = (
        sigmas[base + 2 * width] + sigmas[base] - 2 * sigmas[base + width]
    ) // 2
    constant_term = sigmas[base]
    linear_term = sigmas[base + width] - quad_term - constant_term

    for i in range(3):
        print(base + i * width, i * i * quad_term + i * linear_term + constant_term)
    linear_offsets = [0]
    constant_offsets = [0]
    for j in range(1, width):
        constant_offsets.append(sigmas[base + j] - sigmas[base])
        linear_offsets.append(linear_offsets[-1] + diffs[base + j])

    if steps < base:
        return sigmas[steps]
    else:
        b = (steps - base) // width
        k = (steps - base) % width
        return (
            b * b * quad_term
            + b * linear_term
            + constant_term
            + b * linear_offsets[k]
            + constant_offsets[k]
        )


if __name__ == "__main__":
    Run_2023_21().run_cmdline()
