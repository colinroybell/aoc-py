from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2025_04(DayBase):
    YEAR = "2025"
    DAY = "04"


def part_a(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings_generator(input_generator(input))

    total = 0
    for x in range(width):
        for y in range(height):
            p = Vec2d(x, y)
            if grid.get(p) == "@":
                adj = p.get_adjacent_with_diagonals()
                count = 0
                for a in adj:
                    if grid.get(a) == "@":
                        count += 1
                    if count == 4:
                        break
                else:
                    total += 1
    return total


def part_b(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings_generator(input_generator(input))
    neighbours = Grid2d()

    remove_list = []
    for x in range(width):
        for y in range(height):
            p = Vec2d(x, y)
            if grid.get(p) == "@":
                adj = p.get_adjacent_with_diagonals()
                count = 0
                for a in adj:
                    if grid.get(a) == "@":
                        count += 1
                neighbours.set(p, count)
                if count < 4:
                    remove_list.append(p)

    remove_count = 0
    while remove_list:
        p = remove_list.pop()
        remove_count += 1
        neighbours.unset(p)

        adj = p.get_adjacent_with_diagonals()
        for a in adj:
            count = neighbours.get(a)
            if count:
                count -= 1
                neighbours.set(a, count)
                if count == 3:
                    remove_list.append(a)
    return remove_count


if __name__ == "__main__":
    Run_2025_04().run_cmdline()
