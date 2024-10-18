from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_15(DayBase):
    YEAR = "2020"
    DAY = "15"


def run(input, length):
    starting = []
    spoken = []
    last = {}
    for line in input_generator(input):
        n = line.split(",")
        for k in n:
            starting.append(int(k))
    for r in range(0, length):
        if r < len(starting):
            num = starting[r]
        else:
            if spoken[-1] in last:
                num = r - last[spoken[-1]] - 1
            else:
                num = 0
        if r > 0:
            last[spoken[-1]] = r - 1
        spoken.append(num)

    return spoken[-1]


def part_a(input):
    return run(input, 2020)


def part_b(input):
    return run(input, 30000000)


if __name__ == "__main__":
    Run_2020_15().run_cmdline()
