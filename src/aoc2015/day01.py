import sys
from utils.data_input import input_generator


def part_a(input, part_b=False):
    floor = 0
    count = 1
    for line in input_generator(input):
        for char in line:
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1
            if part_b and floor == -1:
                return count
            count += 1
    assert not part_b
    return floor


def part_b(input):
    return part_a(input, part_b=True)


def entry():
    if "a" in sys.argv:
        print(part_a("data/aoc2015/day01.txt"))
    if "b" in sys.argv:
        print(part_b("data/aoc2015/day01.txt"))


if __name__ == "__main__":
    entry()
