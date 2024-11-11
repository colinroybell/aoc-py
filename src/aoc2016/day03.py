from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2016_03(DayBase):
    YEAR = "2016"
    DAY = "03"


def is_triangle(vals):
    vals = vals + vals
    for i in range(3):
        if vals[i] + vals[i + 1] <= vals[i + 2]:
            return False
    else:
        return True


def part_a(input):
    count = 0
    for line in input_generator(input):
        vals = [int(s) for s in line.split()]
        if is_triangle(vals):
            count += 1
    return count


def part_b(input):
    count = 0
    tri = [[] for _ in range(3)]
    for line in input_generator(input):
        vals = [int(s) for s in line.split()]
        for i in range(3):
            tri[i].append(vals[i])
            if len(tri[i]) == 3:
                if is_triangle(tri[i]):
                    count += 1
                tri[i] = []
    return count


if __name__ == "__main__":
    Run_2016_03().run_cmdline()
