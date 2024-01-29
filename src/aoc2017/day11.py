from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_11(DayBase):
    YEAR = "2017"
    DAY = "11"


def dist(n, ne):
    if n > 0 and ne > 0:
        return n + ne
    elif n < 0 and ne < 0:
        return -(n + ne)
    else:
        return max(abs(n), abs(ne))


def part_a(input, part_b=False):
    part_a = not part_b

    n = 0
    ne = 0
    max_ = 0
    for dir in next(input_generator(input)).split(","):
        if dir == "n":
            n += 1
        elif dir == "ne":
            ne += 1
        elif dir == "se":
            ne += 1
            n -= 1
        elif dir == "s":
            n -= 1
        elif dir == "sw":
            ne -= 1
        elif dir == "nw":
            n += 1
            ne -= 1

        d = dist(n, ne)
        max_ = max(max_, d)

    if part_a:
        return d
    else:
        return max_


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_11().run_cmdline()
