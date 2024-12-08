from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2016_09(DayBase):
    YEAR = "2016"
    DAY = "09"


def decompression_length(string):
    match_re = re.compile(r"(.*?)\((\d+)x(\d+)\)(.*)")

    output = 0
    while 1:
        m = match_re.match(string)
        if not m:
            output += len(string)
            break
        output += len(m.group(1))
        length = int(m.group(2))
        count = int(m.group(3))
        rem = m.group(4)
        output += length * count
        string = rem[length:]
    return output


def apply_mults(length, mults):
    pass


def decompression_length2(string):
    return 0
    match_re = re.compile(r"(.*?)\((\d+)x(\d+)\)(.*)")
    mults = []
    output = 0
    while 1:
        m = match_re.match(string)
        if not m:
            output += apply_mults(len(string), mults)
            break


def part_a(input):
    total = 0
    for line in input_generator(input):
        total += decompression_length(line)
    return total


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2016_09().run_cmdline()
