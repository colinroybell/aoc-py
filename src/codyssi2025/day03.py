from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_03(DayBase):
    YEAR = "2025"
    DAY = "03"
    PREFIX = "codyssi"


def part_1(input):
    total = 0
    for line in input_generator(input):
        fields = line.split()
        for f in fields:
            nums = f.split("-")
            total += int(nums[1]) - int(nums[0]) + 1
            print(nums, total)
    return total


def part_2(input):
    total = 0
    for line in input_generator(input):
        fields = line.split()
        n = []
        for f in fields:
            nums = f.split("-")
            n.append([int(nums[0]), int(nums[1])])
        if n[0][1] < n[1][0] or n[1][1] < n[0][0]:
            # disjoint
            total += n[1][1] - n[1][0] + 1
            total += n[0][1] - n[0][0] + 1
        else:
            total += max(n[0][1], n[1][1]) - min(n[0][0], n[1][0]) + 1
        print(total, n)
    return total


def part_3(input):
    best = 0
    lastSet = None
    for line in input_generator(input):
        thisSet = set()
        fields = line.split()
        n = []
        for f in fields:
            nums = f.split("-")
            for n in range(int(nums[0]), int(nums[1]) + 1):
                thisSet.add(n)
        if lastSet:
            combined = thisSet.union(lastSet)
            best = max(best, len(combined))
        lastSet = thisSet
    return best


if __name__ == "__main__":
    Run_2025_03().run_cmdline()
