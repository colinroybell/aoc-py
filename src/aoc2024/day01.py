from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2024_01(DayBase):
    YEAR = "2024"
    DAY = "01"


def part_a(input):
    lists = [[] for _ in range(2)]
    for line in input_generator(input):
        nums = [int(n) for n in line.split()]
        for i in range(2):
            lists[i].append(nums[i])
    for i in range(2):
        lists[i].sort()

    total = 0
    for i, v in enumerate(lists[0]):
        total += abs(v - lists[1][i])
    return total


def part_b(input):
    lists = [[] for _ in range(2)]
    for line in input_generator(input):
        nums = [int(n) for n in line.split()]
        for i in range(2):
            lists[i].append(nums[i])
    counts = defaultdict(lambda: 0)
    for v in lists[1]:
        counts[v] += 1
    total = 0
    for v in lists[0]:
        total += v * counts[v]
    return total


if __name__ == "__main__":
    Run_2024_01().run_cmdline()
