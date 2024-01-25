from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_06(DayBase):
    YEAR = "2017"
    DAY = "06"


def part_a(input, part_b=False):
    part_a = not part_b
    line = next(input_generator(input))
    cache = {}
    banks = [int(n) for n in line.split()]
    length = len(banks)
    count = 0
    while not tuple(banks) in cache:
        cache[tuple(banks)] = count
        count += 1
        max = 0
        max_pos = 0
        for i, val in enumerate(banks):
            if val > max:
                max = val
                max_pos = i

        move = max
        banks[max_pos] = 0
        for i in range(move):
            banks[(max_pos + i + 1) % length] += 1
        print(banks)
    if part_a:
        return count
    else:
        return count - cache[tuple(banks)]


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_06().run_cmdline()
