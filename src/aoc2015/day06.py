from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
import re


class Run_2015_06(DayBase):
    YEAR = "2015"
    DAY = "06"


def part_a(input, part_b=False):
    part_a = not part_b
    parse_re = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")
    grid = Grid2d(0)
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        cmd = m.group(1)
        xmin = int(m.group(2))
        ymin = int(m.group(3))
        xmax = int(m.group(4))
        ymax = int(m.group(5))
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                p = Vec2d(x, y)
                if part_a:
                    if cmd == "turn on":
                        grid.set(p, 1)
                    elif cmd == "turn off":
                        grid.set(p, 0)
                    else:
                        current_val = grid.get(p)
                        if current_val == None:
                            current_val = 0
                        grid.set(p, 1 - current_val)
                else:
                    current_val = grid.get(p)
                    if current_val == None:
                        current_val = 0
                    if cmd == "turn on":
                        current_val += 1
                    elif cmd == "turn off":
                        if current_val > 0:
                            current_val -= 1
                    else:
                        current_val += 2
                    grid.set(p, current_val)
    if part_a:
        return grid.count_non_zero()
    else:
        return grid.sum()


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2015_06().run_cmdline()
