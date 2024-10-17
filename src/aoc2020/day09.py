from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_09(DayBase):
    YEAR = "2020"
    DAY = "09"


def is_sum_of(n, array):
    size = len(array)
    for i in range(0, size):
        for j in range(i + 1, size):
            if n == array[i] + array[j]:
                return 1
    return 0


def part_a(input, count=25):
    array = []
    for line in input_generator(input):
        array.append(int(line))
    for i in range(count, len(array)):
        if not is_sum_of(array[i], array[i - count : i]):
            return array[i]
    return 0


def part_b(input, count=25):
    array = []
    for line in input_generator(input):
        array.append(int(line))
    total = part_a(input, count)
    start = 0
    finish = 0
    sum_ = 0
    while sum_ != total:
        if sum_ <= total:
            sum_ += array[finish]
            finish += 1
            assert finish <= len(array)
        else:
            sum_ -= array[start]
            start += 1
    return min(array[start:finish]) + max(array[start:finish])


if __name__ == "__main__":
    Run_2020_09().run_cmdline()
