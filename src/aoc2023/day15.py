from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2023_15(DayBase):
    YEAR = "2023"
    DAY = "15"


def hash(string):
    value = 0
    for c in string:
        value += ord(c)
        value = (value * 17) % 256
    return value


def part_a(input):
    line = next(input_generator(input))
    strings = line.split(",")
    total = 0
    for s in strings:
        total += hash(s)
    return total


def part_b(input):
    lenses = [[] for _ in range(256)]
    line = next(input_generator(input))
    strings = line.split(",")
    parse_equals = re.compile(r"(\w+)\=(\d+)")
    parse_dash = re.compile(r"(\w+)\-")
    for s in strings:
        m = parse_dash.match(s)
        if m:
            label = m.group(1)
            box = hash(label)
            pos = None
            for i, lens in enumerate(lenses[box]):
                if lens[0] == label:
                    pos = i
            if pos != None:
                del lenses[box][pos]
        else:
            m = parse_equals.match(s)
            assert m
            label = m.group(1)
            box = hash(label)
            value = int(m.group(2))
            pos = None
            for i, lens in enumerate(lenses[box]):
                if lens[0] == label:
                    pos = i
            if pos != None:
                lenses[box][pos][1] = value
            else:
                lenses[box].append([label, value])
    total = 0
    for b, box in enumerate(lenses):
        for i, lens in enumerate(box):
            score = (1 + b) * (1 + i) * lens[1]
            total += score
    return total


if __name__ == "__main__":
    Run_2023_15().run_cmdline()
