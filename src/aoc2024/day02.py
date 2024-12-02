from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_02(DayBase):
    YEAR = "2024"
    DAY = "02"


def is_safe(nums):
    diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    maxdiff = max(diffs)
    mindiff = min(diffs)
    if mindiff >= 1 and maxdiff <= 3 or mindiff >= -3 and maxdiff <= -1:
        return True
    else:
        return False


def part_a(input):
    safe = 0
    for line in input_generator(input):
        nums = [int(n) for n in line.split()]
        if is_safe(nums):
            safe += 1
    return safe


def part_b(input):
    count = 0
    for line in input_generator(input):
        safe = False
        nums = [int(n) for n in line.split()]
        if is_safe(nums):
            safe = True
        else:
            for remove in range(len(nums)):
                remove_nums = nums.copy()
                remove_nums.pop(remove)
                if is_safe(remove_nums):
                    safe = True
                    break
        if safe:
            count += 1

    return count


if __name__ == "__main__":
    Run_2024_02().run_cmdline()
