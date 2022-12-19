from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2022_01(DayBase):
    YEAR = "2022"
    DAY = "01"


def part_a(input, part_b=False):
    calories = []
    total = 0
    for line in input_generator(input):
        if line:
            total += int(line)
        else:
            calories.append(total)
            total = 0
    calories.append(total)
    if not part_b:
        return max(calories)
    else:
        calories.sort()
        return sum(calories[-3:])


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2022_01().run_cmdline()
