from utils.day_base import DayBase
from utils.data_input import input_generator
from math import prod
import re


class Run_2025_06(DayBase):
    YEAR = "2025"
    DAY = "06"


def part_a(input):
    lists = []
    first = True
    total = 0
    for line in input_generator(input):
        while line[0] == " ":
            line = line[1:]
        fields = re.split(r"\s+", line)
        # print(fields)
        if fields[0].isdigit():
            nums = [int(n) for n in fields]
            for i, n in enumerate(nums):
                if first:
                    lists.append([n])
                else:
                    lists[i].append(n)
            first = False
        else:
            # print(lists)
            for i, symbol in enumerate(fields):
                if symbol == "+":
                    term = sum(lists[i])
                else:
                    assert symbol == "*"
                    term = prod(lists[i])

                total += term
                # print(term,total)
    return total


def part_b(input):
    lines = [line for line in input_generator(input)]
    maxlen = max(len(line) for line in lines)
    for i, line in enumerate(lines):
        lines[i] = lines[i].ljust(maxlen, " ")
    nums = lines[:-1]
    symbols = lines[-1]
    total = 0
    symbol = None
    term = 0

    for i in range(len(symbols)):

        num = "".join([j[i] for j in nums])
        # print(num)
        if symbol == None:
            symbol = symbols[i]
            if symbol == "+":
                term = 0
            else:
                term = 1
        if not num.isspace():
            # print("not space",num)
            n = int(num)
            if symbol == "+":
                term += n
            else:
                term *= n
            # print(n,term)
        else:
            total += term
            symbol = None
    total += term
    return total


def notes():
    """
    Rather hacky - sure this can be tidied up considerably.
    """


if __name__ == "__main__":
    Run_2025_06().run_cmdline()
