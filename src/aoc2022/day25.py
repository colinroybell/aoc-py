from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2022_25(DayBase):
    YEAR = "2022"
    DAY = "25"


digits = "=-012"


def from_snafu(string):
    total = 0
    for d in string:
        v = digits.index(d) - 2
        total = 5 * total + v
    return total


def to_snafu(value):
    string = ""
    while value:
        d = ((value + 2) % 5) - 2
        value -= d
        value //= 5
        string = digits[d + 2] + string
    return string


def part_a(input):
    total = 0
    for line in input_generator(input):
        val = from_snafu(line)
        print(line, val)
        total += val
    return to_snafu(total)


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2022_25().run_cmdline()
