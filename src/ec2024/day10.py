from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_10(DayBase):
    YEAR = "2024"
    DAY = "10"
    PREFIX = "ec"


# TODO: abstract out grid solver component and grid score component


def part_1(input, part=1):
    grid = Grid2d()
    size = 8
    (x_max, y_max) = grid.read_from_file_strings(input, stop_at_blank=False)
    print(x_max, y_max)
    word = ""
    score = 0
    for y_offset in range(0, y_max + 1, 9):
        for x_offset in range(0, x_max + 1, 9):
            count = 0
            print(y_offset, x_offset)
            for y in range(size):
                for x in range(size):
                    if grid.get(Vec2d(x + x_offset, y + y_offset)) == ".":
                        verts = []
                        for yy in range(size):
                            s = grid.get(Vec2d(x + x_offset, yy + y_offset))
                            if s != "." and s != "*":
                                verts.append(s)
                        for xx in range(size):
                            s = grid.get(Vec2d(xx + x_offset, y + y_offset))
                            if s in verts:
                                grid.set(Vec2d(x + x_offset, y + y_offset), s)
                                word += s
                                count += 1
                                score += count * (ord(s) - 64)
                                break
                        else:
                            assert 0, "not found {} {}".format(x, y)
    if part == 1:
        return word
    else:
        return score


def part_2(input):
    return part_1(input, 2)


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2024_10().run_cmdline()
