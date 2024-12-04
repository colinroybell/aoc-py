from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_04(DayBase):
    YEAR = "2024"
    DAY = "04"


def part_a(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    dirs = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            if x or y:
                dirs.append(Vec2d(x, y))
    string = "XMAS"
    count = 0
    for y in range(height):
        for x in range(width):
            c = grid.get(Vec2d(x, y))
            if c != string[0]:
                continue
            for d in dirs:
                pos = Vec2d(x, y)
                for p in range(1, len(string)):
                    pos += d
                    c = grid.get(pos)
                    if c != string[p]:
                        break
                else:
                    count += 1
    return count


def part_b(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    dirs = []
    for y in range(-1, 2, 2):
        for x in range(-1, 2, 2):
            dirs.append(Vec2d(x, y))

    count = 0
    for y in range(height):
        for x in range(width):
            c = grid.get(Vec2d(x, y))
            if c == "A":
                string = ""
                for d in dirs:
                    pos = Vec2d(x, y) + d
                    c = grid.get(pos)
                    if c == None:
                        c = "."
                    string += c
                if (
                    string == "MMSS"
                    or string == "MSMS"
                    or string == "SSMM"
                    or string == "SMSM"
                ):
                    count += 1
    return count


if __name__ == "__main__":
    Run_2024_04().run_cmdline()
