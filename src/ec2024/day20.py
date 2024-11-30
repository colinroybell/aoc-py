from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_20(DayBase):
    YEAR = "2024"
    DAY = "20"
    PREFIX = "ec"


# Goal is to reach one of the points in row 20 with minimum .
def part_1(input):
    grid = Grid2d()
    width, height = grid.read_from_file_strings(input)
    assert grid.get(Vec2d(15, 0)) == "S"
    starts = [(15, 1100)]
    # score is drop from
    for y in range(2, 22, 2):
        new_starts = []
        for x in range(width):
            c = grid.get(Vec2d(x, y))
            if c == "-" or c == "+":
                best = None
                for xx, s in starts:
                    score = s - 2 * (abs(x - xx) + 2)
                    if best == None or score > best:
                        best = score
                if c == "-":
                    best = best - 1
                else:
                    best = best + 2
                new_starts.append((x, best))
        starts = new_starts
        print(y, starts)
    best = None
    for _, s in starts:
        if best == None or s > best:
            best = s
    return best


def part_2(input):
    assert 0, "not implemented"


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2024_20().run_cmdline()
