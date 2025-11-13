from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2025_06(DayBase):
    YEAR = "2025"
    DAY = "06"
    PREFIX = "ec"


def part_1(input, part=1):
    if part == 1:
        restrict = "a"
    else:
        restrict = None
    line = next(input_generator(input))
    mentors = defaultdict(int)
    count = 0
    for c in line:
        if c.isupper():
            mentors[c.lower()] += 1
        else:
            if restrict and c not in restrict:
                continue
            count += mentors[c]
    return count


def part_2(input):
    return part_1(input, part=2)


def part_3(input, repeats=1000, limit=1000):
    line = next(input_generator(input))
    count = 0

    # Initially misread the problem, and just went left again, so fixed by doing a
    # L-R pass and a R-L pass.

    # Two rounds, one to pick up what happens first time round the loop, and second to pick up
    # wraparounds for subsequent runs. Assumes length of string is more than limit.
    for flip in range(2):
        mentors = defaultdict(int)
        cache = [None] * (limit + 1)
        pos = 0
        for round in range(2):
            for c in line:
                old = cache[pos]
                if old and old.isupper():
                    mentors[old.lower()] -= 1
                if c.isupper():
                    mentors[c.lower()] += 1
                else:
                    if round == 0:
                        count += mentors[c]
                    else:
                        count += mentors[c] * (repeats - 1)

                    # print(line,c,pos,count)
                cache[pos] = c
                pos = (pos + 1) % (limit + 1)
        line = line[::-1]  # reverse
    return count


if __name__ == "__main__":
    Run_2025_06().run_cmdline()
