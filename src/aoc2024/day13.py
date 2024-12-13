from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2024_13(DayBase):
    YEAR = "2024"
    DAY = "13"


def part_a(input, part_b=False):
    num_re = re.compile(r"(\d+).+?(\d+)")
    state = 0
    cost = 0
    for line in input_generator(input):
        if state < 3:
            m = num_re.search(line)
            assert m
            x = int(m.group(1))
            y = int(m.group(2))
            if state == 0:
                x1 = x
                y1 = y
            elif state == 1:
                x2 = x
                y2 = y
            else:
                if part_b:
                    x += 10000000000000
                    y += 10000000000000
                delta = x1 * y2 - x2 * y1
                a = y2 * x - x2 * y
                b = -y1 * x + x1 * y
                if a % delta == 0 and b % delta == 0:
                    a //= delta
                    b //= delta
                    cost += a * 3 + b
        state = (state + 1) % 4
    return cost


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2024_13().run_cmdline()
