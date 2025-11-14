from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_st01_03(DayBase):
    YEAR = "st01"
    DAY = "03"
    PREFIX = "ec"


def part_1(input):
    xy_re = re.compile(r"x=(\d+) y=(\d+)")
    score = 0
    for line in input_generator(input):
        m = xy_re.match(line)
        assert m
        x = int(m.group(1))
        y = int(m.group(2))
        disc = x + y - 1
        moves = 100 % disc
        x = ((x + moves - 1) % disc) + 1
        y = ((y - moves - 1) % disc) + 1
        score += x + 100 * y
    return score


# Extended GCD to compute Bezout identity values
def extended_gdb(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return (old_r, old_s, old_t)


def part_2(input):
    xy_re = re.compile(r"x=(\d+) y=(\d+)")

    s = None
    mod = None

    for line in input_generator(input):
        m = xy_re.match(line)
        assert m
        x = int(m.group(1))
        y = int(m.group(2))
        disc = x + y - 1
        steps = y - 1

        if s == None:
            s = steps
            mod = disc
        else:
            gcd, bez0, bez1 = extended_gdb(mod, disc)

            s = s * bez1 * disc + steps * bez0 * mod
            mod = mod * disc // gcd
            s = s % mod

    return s


def part_3(input):
    return part_2(input)


if __name__ == "__main__":
    Run_st01_03().run_cmdline()
