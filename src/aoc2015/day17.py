from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_17(DayBase):
    YEAR = "2015"
    DAY = "17"


def part_a(input, target=150):
    counts = [0 for x in range(0, target + 1)]
    counts[0] = 1
    for line in input_generator(input):
        size = int(line)
        for i in range(target, size - 1, -1):
            counts[i] = counts[i] + counts[i - size]
        print(counts)
    return counts[target]


def part_b(input, target=150):
    counts = [[0] for x in range(0, target + 1)]
    counts[0][0] = 1
    for line in input_generator(input):
        size = int(line)
        for i in range(target, size - 1, -1):
            for j in range(len(counts[i - size])):
                if len(counts[i]) < j + 2:
                    counts[i].append(counts[i - size][j])
                else:
                    counts[i][j + 1] += counts[i - size][j]
        print(counts)
    j = 0
    while counts[target][j] == 0:
        j += 1

    return counts[target][j]


if __name__ == "__main__":
    Run_2015_17().run_cmdline()
