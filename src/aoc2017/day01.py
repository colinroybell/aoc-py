from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_01(DayBase):
    YEAR = "2017"
    DAY = "01"


def part_a(input):
    text = next(input_generator(input))
    text += text[0]
    sum_ = 0
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            sum_ += int(text[i])
    return sum_


def part_b(input):
    text = next(input_generator(input))
    sum_ = 0
    h = len(text) // 2
    for i in range(h):
        if text[i] == text[i + h]:
            sum_ += int(text[i])
    sum_ *= 2
    return sum_


if __name__ == "__main__":
    Run_2017_01().run_cmdline()
