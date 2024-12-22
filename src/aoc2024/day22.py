from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_22(DayBase):
    YEAR = "2024"
    DAY = "22"


def next_number(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return n


def part_a(input):
    total = 0
    for line in input_generator(input):
        n = int(line)
        for _ in range(2000):
            n = next_number(n)
        total += n
    return total


def score(secrets, changes):
    print(secrets, changes)
    total = 0
    for i, n in enumerate(secrets):
        diffs = [None, None, None, None]
        last = None
        for s in range(2000):
            n = next_number(n)
            price = n % 10
            for j in range(3):
                diffs[j] = diffs[j + 1]
            if s > 0:
                diffs[3] = price - last
            if 288 < s < 292:
                print(s, diffs, changes)
            last = price
            if diffs == changes:
                print("found {} at pos {} price {}".format(i, s, price))
                total += price
                break
    return total


def part_b(input):
    secrets = []
    points = {}

    for line in input_generator(input):
        n = int(line)

        this_points = {}
        diffs = [None, None, None, None]
        for s in range(2000):
            n = next_number(n)
            price = n % 10
            for j in range(3):
                diffs[j] = diffs[j + 1]
            if s > 0:
                diffs[3] = price - last
            last = price
            t = tuple(diffs)
            if s >= 4 and t not in this_points:
                this_points[t] = price
        for d, v in this_points.items():
            if d not in points:
                points[d] = 0
            points[d] += v
    max = 0
    for d, v in points.items():
        if v > max:
            max = v

    return max


if __name__ == "__main__":
    Run_2024_22().run_cmdline()
