from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_06(DayBase):
    YEAR = "2025"
    DAY = "06"
    PREFIX = "codyssi"


def count_alpha(c):
    return 1 if c.isalpha() else 0


def alpha_score(c):
    if not c.isalpha():
        return 0
    if c.isupper():
        return ord(c) - 64 + 26
    else:
        return ord(c) - 96


def part_1(input, part=1):
    line = next(input_generator(input))

    if part == 1:
        fn = count_alpha
    else:
        fn = alpha_score

    return sum(fn(c) for c in line)


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    line = next(input_generator(input))

    total = 0
    last_score = 0
    for c in line:
        score = alpha_score(c)
        if score == 0:
            score = ((last_score * 2 - 6) % 52) + 1
        total += score
        print(c, score)
        last_score = score
    return total


if __name__ == "__main__":
    Run_2025_06().run_cmdline()
