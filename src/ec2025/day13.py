from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import deque


class Run_2025_13(DayBase):
    YEAR = "2025"
    DAY = "13"
    PREFIX = "ec"


def part_1(input):
    n = [1]
    for line in input_generator(input):
        n.append(int(line))

    count = len(n)
    pos = 2025 % count
    if pos == 0:
        return n[0]
    elif pos <= count / 2:
        return n[pos * 2 - 1]
    else:
        return n[(count - pos) * 2]


# Pinched this from another solution - looks like a good methodology to adopt.
def parse2(input):
    return [
        (int(start), int(end))
        for start, end in (line.strip().split("-") for line in input_generator(input))
    ]


def part_2(input, part=2):
    count = 1
    right = True
    rights = []
    lefts = []
    for line in input_generator(input):
        (a, b) = line.split("-")
        a = int(a)
        b = int(b)
        assert a < b
        count += b - a + 1
        # Have to insert a direction, which is why pair became a third to add a direction
        if right:
            pair = (a, b - a + 1, 1)
            rights = rights + [pair]
        else:
            pair = (b, b - a + 1, -1)
            lefts = [pair] + lefts
        right = not right
    nums = [(1, 1, 0)] + rights + lefts
    if part == 2:
        pos = 20252025 % count
    else:
        pos = 202520252025 % count
    for (start, num, dir) in nums:
        if pos < num:
            return start + pos * dir
        else:
            pos -= num


def part_3(input):
    return part_2(input, part=3)


if __name__ == "__main__":
    Run_2025_13().run_cmdline()
