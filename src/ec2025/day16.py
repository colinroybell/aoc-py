from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_16(DayBase):
    YEAR = "2025"
    DAY = "16"
    PREFIX = "ec"


def part_1(input):
    line = next(input_generator(input))
    divs = [int(n) for n in line.split(",")]
    return sum([90 // d for d in divs])


def part_2(input):
    line = next(input_generator(input))
    blocks = [0] + [int(n) for n in line.split(",")]
    mult = 1
    for i in range(len(blocks)):
        if blocks[i]:
            assert blocks[i] == 1
            mult *= i
            for j in range(i, len(blocks), i):
                blocks[j] -= 1
    return mult


def blocks_per_length(divs, length):
    return sum([length // d for d in divs])


def part_3(input, blocks=202520252025000):
    line = next(input_generator(input))
    sample = [0] + [int(n) for n in line.split(",")]
    divs = []
    for i in range(len(sample)):
        if sample[i]:
            assert sample[i] == 1
            divs.append(i)
            for j in range(i, len(sample), i):
                sample[j] -= 1

    length = 1
    while blocks_per_length(divs, length) <= blocks:
        length *= 2

    minimum = length // 2
    maximum = length
    while maximum - minimum > 1:
        mid = (minimum + maximum) // 2
        if blocks_per_length(divs, mid) <= blocks:
            minimum = mid
        else:
            maximum = mid
    return minimum


if __name__ == "__main__":
    Run_2025_16().run_cmdline()
