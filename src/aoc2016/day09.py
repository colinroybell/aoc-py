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


def multiplier(start, finish, mults, uniform):
    mul = 1
    mul_finish = finish
    while mults and mults[0][1] <= start:
        mults.pop(0)
    for factor, end in mults:
        if end > start:
            if end <= finish:
                assert not uniform
                mul_finish = end
            mul *= factor
    while mults and mults[0][1] <= mul_finish:
        mults.pop(0)
    return (mul, mul_finish)


def decompression_length2(string):
    match_re = re.compile(r"(.*?)\((\d+)x(\d+)\)(.*)")
    mults = []
    output = 0
    base = 0
    while 1:
        m = match_re.match(string)
        if not m:
            done = False
            while len(string) > 0:
                (mul, mul_finish) = multiplier(base, base + len(string), mults, False)
                output += mul * (mul_finish - base)
                string = string[mul_finish - base :]
                base = mul_finish
            break
        string = m.group(1)
        while len(string) > 0:
            (mul, mul_finish) = multiplier(base, base + len(string), mults, False)
            output += mul * (mul_finish - base)
            string = string[mul_finish - base :]
            base = mul_finish
        length = int(m.group(2))
        count = int(m.group(3))
        string_length = len(m.group(2)) + len(m.group(3)) + 3
        mults.append([count, base + length + string_length])
        base += string_length
        string = m.group(4)
    return output


def part_a(input):
    total = 0
    for line in input_generator(input):
        total += decompression_length(line)
    return total


def part_b(input):
    total = 0
    for line in input_generator(input):
        total += decompression_length2(line)
    return total


if __name__ == "__main__":
    Run_2016_09().run_cmdline()
