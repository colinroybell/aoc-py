from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.maths import lcm


class Run_2020_13(DayBase):
    YEAR = "2020"
    DAY = "13"


def part_a(input):
    line = next(input_generator(input))
    val = int(line)
    base = int(line)
    for line in input_generator(input):
        intervals = line.split(",")
        earliest = 1e6 * base
        score = 0
        for interval in intervals:
            if interval == "x":
                continue
            t = int(interval)
            time = t * ((base + t - 1) // t)
            if time < earliest:
                earliest = time
                score = (time - base) * t
    return score


def part_b(input):
    line = next(input_generator(input))
    # ignore first line
    for line in input_generator(input):
        intervals = line.split(",")
    t = 0
    div = 1
    constraints = []
    for i, string in enumerate(intervals):
        if string == "x":
            continue
        interval = int(string)
        constraints.append((interval, i))
        while t % interval != (interval - i) % interval:
            t += div
        div = lcm(div, interval)
        for j in constraints:
            assert t % j[0] == (j[0] - j[1]) % j[0]
    return t


if __name__ == "__main__":
    Run_2020_13().run_cmdline()
