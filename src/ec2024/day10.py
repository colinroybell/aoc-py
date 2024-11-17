from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_10(DayBase):
    YEAR = "2024"
    DAY = "10"
    PREFIX = "ec"


def grid_solve(grid, x_offset, y_offset, part):
    size = 8
    update = False
    for y in range(2, 6):
        for x in range(2, 6):
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
                        update = True
                        break
                else:
                    assert 0, "not found {} {}".format(x, y)
    return update


def grid_score(grid, x_offset, y_offset):
    count = 0
    score = 0
    for y in range(2, 6):
        for x in range(2, 6):
            s = grid.get(Vec2d(x + x_offset, y + y_offset))
            value = ord(s) - 64
            assert value > 0 and value <= 26, "out of range"
            count += 1
            score += count * value
    return score


def grid_word(grid, x_offset, y_offset):
    word = ""
    for y in range(2, 6):
        for x in range(2, 6):
            s = grid.get(Vec2d(x + x_offset, y + y_offset))
            word += s
    return word


def part_1(input, part=1):
    grid = Grid2d()
    size = 8
    (x_max, y_max) = grid.read_from_file_strings(input, stop_at_blank=False)
    print(x_max, y_max)
    word = ""
    score = 0
    for y_offset in range(0, y_max + 1, 9):
        for x_offset in range(0, x_max + 1, 9):
            grid_solve(grid, x_offset, y_offset, part)
            score += grid_score(grid, x_offset, y_offset)
            word += grid_word(grid, x_offset, y_offset)

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
