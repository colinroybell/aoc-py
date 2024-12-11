from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_11(DayBase):
    YEAR = "2024"
    DAY = "11"


def next_n(n):
    if n == 0:
        return [1]
    s = str(n)
    if len(s) % 2 == 0:
        h = len(s) // 2
        return [int(s[:h]), int(s[h:])]
    return [n * 2024]


def recurse(n, blinks, cache):
    if blinks == 0:
        return 1
    pair = (n, blinks)
    if pair in cache:
        return cache[pair]
    nexts = next_n(n)
    count = sum([recurse(num, blinks - 1, cache) for num in nexts])
    cache[pair] = count
    return count


def part_a(input, blinks=25):
    cache = {}
    total = 0
    for line in input_generator(input):
        nums = [int(n) for n in line.split()]
        for n in nums:
            total += recurse(n, blinks, cache)
    return total


def part_b(input):
    return part_a(input, blinks=75)


if __name__ == "__main__":
    Run_2024_11().run_cmdline()
