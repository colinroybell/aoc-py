from utils.day_base import DayBase
from utils.data_input import input_generator

# TODO: work out how to import relatively
from aoc2017.knothash import knothash


class Run_2017_14(DayBase):
    YEAR = "2017"
    DAY = "14"


def part_a(input):
    line = next(input_generator(input))
    count = 0
    for i in range(128):
        key = line + "-" + str(i)
        hash = knothash(key)
        for j in range(32):
            digit = int(hash[j], 16)
            for bit in range(4):
                if digit & (1 << bit):
                    count += 1
    return count


rets = []


def recurse(i, j):
    if i >= 0 and i <= 127 and j >= 0 and j <= 127 and rets[i][j]:
        rets[i][j] = False
        recurse(i - 1, j)
        recurse(i + 1, j)
        recurse(i, j - 1)
        recurse(i, j + 1)


def part_b(input):
    line = next(input_generator(input))
    count = 0

    for i in range(128):
        key = line + "-" + str(i)
        hash = knothash(key)
        bits = []
        for j in range(32):
            digit = int(hash[j], 16)
            for bit in range(3, -1, -1):
                bits.append(digit & (1 << bit))
        rets.append(bits)

    for i in range(128):
        for j in range(128):
            if rets[i][j]:
                count += 1
                recurse(i, j)
    return count


if __name__ == "__main__":
    Run_2017_14().run_cmdline()
