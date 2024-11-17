from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_09(DayBase):
    YEAR = "2024"
    DAY = "09"
    PREFIX = "ec"


# TODO: refactor and tidy up


def part_1(input):
    offsets = [0, 1, 2, 1, 2, 1, 2, 3, 4, 3]
    total = 0
    for line in input_generator(input):
        target = int(line)
        beetles = (target // 10) + offsets[target % 10]
        print(beetles)
        total += beetles
    return total


def part_2(input):
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    targets = [int(line) for line in input_generator(input)]
    maximum = max(targets)
    counts = [0 for _ in range(maximum + 1)]
    for b in range(1, maximum + 1):
        best = None
        for s in stamps:
            if s <= b:
                c = counts[b - s] + 1
                if best == None or c < best:
                    best = c
        print(b, c)
        counts[b] = best
    return sum(counts[t] for t in targets)


def part_3(input):
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    targets = [int(line) for line in input_generator(input)]
    maximum = max(targets)
    diff = 100
    length = maximum // 2 + diff // 2
    counts = [0 for _ in range(length + 1)]
    for b in range(1, length + 1):
        best = None
        for s in stamps:
            if s <= b:
                c = counts[b - s] + 1
                if b == 41:
                    print("t", s, c)
                if best == None or c < best:
                    best = c
        # print(b,c)
        counts[b] = best
    total = 0
    for t in targets:
        best = None
        hs = t // 2
        hl = t - hs
        while hl - hs <= 100:
            score = counts[hs] + counts[hl]
            if best == None or score < best:
                print(hl, hs, score)
                best = score
            hs -= 1
            hl += 1
        total += best
    return total

    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2024_09().run_cmdline()
