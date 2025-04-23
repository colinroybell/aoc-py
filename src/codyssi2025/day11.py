from utils.day_base import DayBase
from utils.data_input import input_generator
from math import log, exp, ceil


class Run_2025_11(DayBase):
    YEAR = "2025"
    DAY = "11"
    PREFIX = "codyssi"


def character_value(c):
    v = ord(c)
    if 0 <= v - 48 <= 9:
        return v - 48
    if 0 <= v - 65 <= 25:
        return v - 65 + 10
    if 0 <= v - 97 <= 25:
        return v - 97 + 36
    assert 0, "can't parse {} ord={}".format(c, v)


def inverse_value(v):
    if v < 10:
        return chr(v + 48)
    if v < 36:
        return chr(v - 10 + 65)
    if v < 61:
        return chr(v - 36 + 97)
    else:
        return "!@#$%^"[v - 62]


def part_1(input, part=1):
    vals = []
    for line in input_generator(input):
        fields = line.split()
        base = int(fields[1])
        val = 0
        for c in fields[0]:
            val = val * base + character_value(c)
        vals.append(val)
    if part == 1:
        return max(vals)
    elif part == 2:
        s = sum(vals)
        out = ""
        while s > 0:
            out = inverse_value(s % 68) + out
            s = s // 68
        return out
    else:
        s = sum(vals)
        return ceil(exp(log(s) / 4))


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2025_11().run_cmdline()
