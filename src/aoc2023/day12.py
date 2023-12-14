from utils.day_base import DayBase
from utils.data_input import input_generator
from functools import lru_cache


class Run_2023_12(DayBase):
    YEAR = "2023"
    DAY = "12"


@lru_cache(maxsize=None)
def recurse(line, pattern):
    # print('   ',line, pattern)
    if pattern == []:
        # print('void', 1)
        return 1
    while line and line[0] == ".":
        line = line[1:]
    required_length = sum(pattern) + len(pattern) - 1
    # print(len(line), 'v', required_length)
    if len(line) < required_length:
        # print('insufficient')
        return 0
    if line[0] == "#":
        ok = True
        for i in range(1, pattern[0]):
            if line[i] == ".":
                # print('fail', i)
                ok = False
        if not ok:
            return 0
        if len(pattern) == 1:
            for i in range(pattern[0], len(line)):
                if line[i] == "#":
                    # print('excess hash')
                    return 0
            # print(line, pattern, 'end case', 1)
            return 1
        else:
            if line[pattern[0]] != "#":
                value = recurse(line[pattern[0] + 1 :], pattern[1:])
                # print(line, pattern, 'case 1', value)
            else:
                # print(line, pattern, 'case 1 fail hash', 0)
                value = 0
            return value
    else:
        case_dot = recurse(line[1:], pattern)
        case_hash = recurse("#" + line[1:], pattern)
        # print(line, pattern, 'dot', case_dot, 'hash', case_hash)
        return case_dot + case_hash


def part_a(input):
    total = 0
    for line in input_generator(input):
        fields = line.split()
        pattern = [int(n) for n in fields[1].split(",")]
        count = recurse(fields[0], tuple(pattern))
        total += count
        print("result", count, total)
    return total


def part_b(input):
    total = 0
    for line in input_generator(input):
        fields = line.split()
        pattern = [int(n) for n in fields[1].split(",")]

        string = (
            fields[0]
            + "?"
            + fields[0]
            + "?"
            + fields[0]
            + "?"
            + fields[0]
            + "?"
            + fields[0]
        )
        pattern = pattern + pattern + pattern + pattern + pattern
        count = recurse(string, tuple(pattern))
        total += count
        print("result", count, total)
    return total


if __name__ == "__main__":
    Run_2023_12().run_cmdline()
