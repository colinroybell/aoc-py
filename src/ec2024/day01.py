from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_01(DayBase):
    YEAR = "2024"
    DAY = "01"
    PREFIX = "ec"


def part_1(input, part=1):
    costs = {"A": 0, "B": 1, "C": 3, "D": 5}
    line = next(input_generator(input))
    cost = 0
    for i in range(0, len(line), part):
        creatures = line[i : i + part]
        count = 0
        for c in creatures:
            if c != "x":
                cost += costs[c]
                count += 1

        if count > 1:
            cost += (count - 1) * count
    return cost


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2024_01().run_cmdline()
