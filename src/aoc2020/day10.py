from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_10(DayBase):
    YEAR = "2020"
    DAY = "10"


def part_a(input):
    volts = [0]
    for line in input_generator(input):
        volts.append(int(line))
    volts.sort()
    volts.append(volts[-1] + 3)
    dc = [0] * 4
    for i in range(0, len(volts) - 1):
        diff = volts[i + 1] - volts[i]
        assert diff > 0 and diff < 4
        dc[diff] += 1
    return dc[1] * dc[3]


def part_b(input):
    volts = [0]
    for line in input_generator(input):
        volts.append(int(line))
    volts.sort()
    volts.append(volts[-1] + 3)
    count = [0] * len(volts)
    count[0] = 1
    for i in range(1, len(volts)):
        j = 1
        while j <= i and volts[i] - volts[i - j] <= 3:
            count[i] += count[i - j]
            j += 1
    return count[-1]


if __name__ == "__main__":
    Run_2020_10().run_cmdline()
