from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2021_07(DayBase):
    YEAR = "2021"
    DAY = "07"


def part_a(input, part_b=False):
    line = next(input_generator(input))
    words = line.split(",")
    buckets = defaultdict(int)
    min_ = None
    max_ = None
    for word in words:
        v = int(word)
        buckets[v] += 1
    min_ = min(buckets.keys())
    max_ = max(buckets.keys())
    best_score = None
    for pos in range(min_, max_ + 1):
        score = 0
        for loc, count in buckets.items():
            d = abs(pos - loc)
            if part_b == False:
                score += d * count
            else:
                score += d * (d + 1) // 2 * count
        if best_score == None or score < best_score:
            best_score = score
    return best_score


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2021_07().run_cmdline()
