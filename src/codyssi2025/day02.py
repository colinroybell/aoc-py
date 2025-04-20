from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_02(DayBase):
    YEAR = "2025"
    DAY = "02"
    PREFIX = "codyssi"


def part_1(input, part=1):
    params = {}
    nums = []
    for line in input_generator(input):
        fields = line.split()
        if len(fields) == 0:
            continue
        elif len(fields) == 1:
            nums.append(int(line))
        else:
            params[fields[1][0]] = int(fields[-1])
    if part == 3:
        best = None
        for n in nums:
            score = pow(n, params["C"]) * params["B"] + params["A"]
            if score < 15000000000000:
                if best == None or n > best:
                    best = n
        return best

    if part == 1:
        nums.sort()
        base = nums[(len(nums) - 1) // 2]
    else:
        base = sum([n if n % 2 == 0 else 0 for n in nums])
    score = pow(base, params["C"]) * params["B"] + params["A"]
    return score


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2025_02().run_cmdline()
