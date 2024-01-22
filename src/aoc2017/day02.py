from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_02(DayBase):
    YEAR = "2017"
    DAY = "02"


def part_a(input, part_b=False):
    part_a = not part_b
    sum_ = 0
    sum2 = 0
    for line in input_generator(input):
        array = line.split()
        n = []
        for i in array:
            n.append(int(i))

        min_ = int(n[0])
        max_ = int(n[0])
        for i in range(1, len(array)):
            if int(n[i]) > max_:
                max_ = int(n[i])
            if int(n[i]) < min_:
                min_ = int(n[i])
        sum_ += max_ - min_

        if part_b:
            for i in range(0, len(array)):
                for j in range(0, len(array)):
                    if i != j and n[i] % n[j] == 0:
                        sum2 += n[i] // n[j]
    if part_a:
        return sum_
    else:
        return sum2


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_02().run_cmdline()
