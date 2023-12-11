from utils.day_base import DayBase
from utils.data_input import input_generator
from math import prod


class Run_2023_02(DayBase):
    YEAR = "2023"
    DAY = "02"


def part_a(input, part_b=False):
    part_a = not part_b
    colours = ["red", "green", "blue"]
    max_a = [12, 13, 14]
    total = 0
    for line in input_generator(input):
        ok = True
        max_b = [0, 0, 0]
        parts = line.split(":")
        id = int(parts[0][5:])
        shows = parts[1].split("; ")
        for show in shows:
            reveals = show.split(", ")
            for reveal in reveals:
                # print (reveal, reveal.split(' '))
                (n, colour) = reveal.split(" ")[-2:]
                count = int(n)
                pos = colours.index(colour)
                # part a test
                if count > max_a[pos]:
                    ok = False
                # part b
                max_b[pos] = max(max_b[pos], count)
        if part_a:
            if ok:
                total += id
        if part_b:
            print(max_b, prod(max_b))
            total += prod(max_b)
    return total


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_02().run_cmdline()
