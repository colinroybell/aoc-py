from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2025_14(DayBase):
    YEAR = "2025"
    DAY = "14"
    PREFIX = "ec"


def part_1(input, part=1):
    grid = Grid2d()
    (width, height) = grid.read_from_hash_dot_list(input_generator(input))
    # print(width,height)

    total = 0
    cache = []
    cum_cache = [0]
    rounds = 10
    if part == 2:
        rounds = 2025
    cache.append(str(grid))
    for count in range(1, rounds + 1):
        print("round", count)
        newgrid = Grid2d()
        for x in range(width):
            for y in range(height):
                pos = Vec2d(x, y)
                count = 0
                matches = []
                if grid.get(pos):
                    count += 1
                    matches.append(pos)
                for p in pos.get_adjacent_diagonals():
                    if grid.get(p):
                        count += 1
                        matches.append(p)
                if count % 2 == 0:
                    newgrid.set(pos, 1)
                    total += 1
        grid = newgrid
        rep = str(grid)
        for i in range(count):
            if rep == cache[i]:
                # TODO: utility function to compute number based on repeats - this is same as something we did in ecst01/day1
                rounds -= count
                loops = rounds // (count - i)
                remainder = rounds - loops * (count - i)
                return (
                    total
                    + loops * (total - cum_cache[i])
                    + cum_cache[i + remainder]
                    - cum_cache[i]
                )
        cache.append(rep)
        cum_cache.append(total)
    return total


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2025_14().run_cmdline()
