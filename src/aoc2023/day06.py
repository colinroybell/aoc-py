from utils.day_base import DayBase
from utils.data_input import input_generator
from math import sqrt


class Run_2023_06(DayBase):
    YEAR = "2023"
    DAY = "06"


def part_a(input, part_b=False):
    part_a = not part_b
    generator = input_generator(input)
    if part_a:
        line = next(generator)
        print([n for n in line[10:].split()])
        times = [int(n) for n in line[10:].split()]
        line = next(generator)
        distances = [int(n) for n in line[10:].split()]
    else:
        line = next(generator)
        n = ""
        for c in line[10:]:
            if c.isdigit():
                n += c
        times = [int(n)]
        line = next(generator)
        n = ""
        for c in line[10:]:
            if c.isdigit():
                n += c
        distances = [int(n)]

    prod = 1
    for i in range(len(times)):
        t = times[i]
        d = distances[i]
        d += 1e-6
        s1 = (-t + sqrt(t * t - 4 * d)) / 2
        s2 = (-t - sqrt(t * t - 4 * d)) / 2
        score = int(s1) - int(s2)
        print(score, s1, s2)
        prod *= score
    return prod


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_06().run_cmdline()
