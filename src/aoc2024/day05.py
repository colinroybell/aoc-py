from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2024_05(DayBase):
    YEAR = "2024"
    DAY = "05"


def part_a(input):
    rules = []
    in_rules = True
    generator = input_generator(input)
    while 1:
        line = next(generator)
        if line == "":
            break
        rules.append(line.split("|"))

    total = 0
    for line in generator:
        pages = line.split(",")
        lookup = {page: pos for pos, page in enumerate(pages)}
        print(lookup)
        for r in rules:
            if r[0] in lookup and r[1] in lookup and lookup[r[1]] < lookup[r[0]]:
                break
        else:
            print(int(pages[len(pages) // 2]))
            total += int(pages[len(pages) // 2])
    return total


def part_b(input):
    rules = defaultdict(lambda: set())
    in_rules = True
    generator = input_generator(input)
    while 1:
        line = next(generator)
        if line == "":
            break
        nums = [int(n) for n in line.split("|")]
        rules[nums[0]].add(nums[1])

    total = 0
    for line in generator:
        pages = [int(n) for n in line.split(",")]

        new_round = True
        done_swap = False

        while new_round:
            new_round = False
            for i in range(len(pages) - 1):
                p0 = pages[i]
                p1 = pages[i + 1]
                if p1 not in rules[p0]:
                    new_round = True
                    done_swap = True
                    pages[i] = p1
                    pages[i + 1] = p0
        if done_swap:
            print(int(pages[len(pages) // 2]))
            total += int(pages[len(pages) // 2])
    return total


if __name__ == "__main__":
    Run_2024_05().run_cmdline()
