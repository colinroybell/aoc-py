from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_07(DayBase):
    YEAR = "2024"
    DAY = "07"


def recurse(part_b, target, list):
    last = list[-1]
    rest = list[0:-1]
    if rest == []:
        return target == last
    if target % last == 0 and recurse(part_b, target // last, rest):
        return True
    if part_b and target > last and str(target).endswith(str(last)):
        if recurse(part_b, int(str(target)[0 : -len(str(last))]), rest):
            return True
    if target > last and recurse(part_b, target - last, rest):
        return True
    return False


def part_a(input, part_b=False):
    total = 0
    for line in input_generator(input):
        target, nums = line.split(":")
        target = int(target)
        list = [int(n) for n in nums.split()]
        if recurse(part_b, target, list):
            total += target
    return total


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2024_07().run_cmdline()
