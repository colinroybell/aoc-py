from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_18(DayBase):
    YEAR = "2020"
    DAY = "18"


import re


def compute_simple(line):
    fields = line.split(" ")
    N = (len(fields) - 1) // 2
    n = int(fields.pop(0))
    for i in range(0, N):
        op = fields.pop(0)
        val = int(fields.pop(0))
        if op == "+":
            n += val
        else:
            n *= val
    return n


def compute_complex(line):
    addition_re = re.compile(r"(.*?)(\d+)\s\+\s(\d+)(.*)")
    while m := addition_re.match(line):
        line = m.group(1) + str(int(m.group(2)) + int(m.group(3))) + m.group(4)
    return compute_simple(line)


def both_parts(input, part):
    bracket_re = re.compile(r"(.*?)\(([^()]+)\)(.*)")
    sum_ = 0
    for line in input_generator(input):
        while m := bracket_re.match(line):
            if part == "a":
                v = compute_simple(m.group(2))
            else:
                v = compute_complex(m.group(2))
            line = m.group(1) + "{}".format(v) + m.group(3)
        if part == "a":
            sum_ += compute_simple(line)
        else:
            sum_ += compute_complex(line)
    return sum_


def part_a(input):
    return both_parts(input, "a")


def part_b(input):
    return both_parts(input, "b")


if __name__ == "__main__":
    Run_2020_18().run_cmdline()
