from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_04(DayBase):
    YEAR = "2024"
    DAY = "04"
    PREFIX = "ec"


def part_1(input):
    minimum = None
    sigma = 0
    count = 0
    for line in input_generator(input):
        value = int(line)
        sigma += value
        if count == 0:
            minimum = value
        else:
            minimum = min(minimum, value)
        count += 1
    return sigma - minimum * count


def part_2(input):
    return part_1(input)


def part_3(input):
    minimum = None
    maximum = None
    sigma = 0
    count = 0
    values = []
    for line in input_generator(input):
        value = int(line)
        values.append(value)

    print(values)
    values.sort()
    print(values)
    midpoint = len(values) // 2

    median = values[midpoint]

    for v in values:
        sigma += abs(v - median)
    return sigma


if __name__ == "__main__":
    Run_2024_04().run_cmdline()
