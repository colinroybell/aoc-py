from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2021_01(DayBase):
    YEAR = "2021"
    DAY = "01"


def part_a(input):
    last = None
    count = 0
    for line in input_generator(input):
        val = int(line)
        if last and val > last:
            count += 1
        last = val
    return count


def part_b(input):
    window = []
    last = None
    count = 0
    for line in input_generator(input):
        val = int(line)
        window.append(val)
        if len(window) == 3:
            sum_ = sum(window)
            print(sum_, window)
            if last and sum_ > last:
                count += 1
            last = sum_
            window.pop(0)
    return count


if __name__ == "__main__":
    Run_2021_01().run_cmdline()
