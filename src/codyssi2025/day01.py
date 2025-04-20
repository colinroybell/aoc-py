from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_01(DayBase):
    YEAR = "2025"
    DAY = "01"
    PREFIX = "codyssi"


def part_1(input, part=1):
    first_num = None
    nums = []
    corrections = None
    digit = None
    for line in input_generator(input):
        if "+" in line or "-" in line:
            corrections = line
        else:
            n = int(line)
            if part == 3:
                if not digit:
                    digit = n
                    continue
                else:
                    n = digit * 10 + n
                    digit = None
            if first_num == None:
                first_num = n
            else:
                nums.append(n)

    offset = first_num
    print(first_num, nums)
    if part == 1:
        signs_gen = (s for s in corrections)
    else:
        signs_gen = (s for s in reversed(corrections))
    for (n, sign) in zip((n for n in nums), signs_gen):
        if sign == "+":
            offset += n
        else:
            offset -= n
    return offset


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2025_01().run_cmdline()
