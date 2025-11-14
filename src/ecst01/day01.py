from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_st01_01(DayBase):
    YEAR = "st01"
    DAY = "01"
    PREFIX = "ec"

    PART = 1


# May be optimisable further if we factorise the numbers and can work out patterns and paths


def eni3(n, exp, mod):
    cache = [0]
    cum_cache = [0]
    cum = 0
    x = 1
    done = False
    e = 0
    print("eni3", n, exp, mod)
    while 1:
        x = (x * n) % mod
        cache.append(x)
        cum += x
        cum_cache.append(cum)
        e += 1
        if e == exp:
            return cum
        for p in range(e - 1, 0, -1):
            if cache[p] == x:
                exp -= e
                rounds = exp // (e - p)
                rem = exp - rounds * (e - p)
                return (
                    cum
                    + rounds * (cum - cum_cache[p])
                    + cum_cache[p + rem]
                    - cum_cache[p]
                )


def eni(n, exp, mod):
    x = 1
    res = ""

    if Run_st01_01.PART == 3:
        return eni3(n, exp, mod)

    if Run_st01_01.PART == 2 and exp > 5:
        # Work out the value to exponent - 5 by binary decomposition and squaring the
        # multiplier each time
        rem = exp - 5
        exp = 5
        n_pow = n
        while rem:
            if rem % 2 == 1:
                x = (x * n_pow) % mod
            rem //= 2
            n_pow = (n_pow * n_pow) % mod

    for e in range(exp):
        x = (x * n) % mod
        if Run_st01_01.PART == 1 or (Run_st01_01.PART == 2 and exp - e <= 5):
            res = str(x) + res
    return int(res)


def part_1_formula(a, b, c, x, y, z, m):
    return eni(a, x, m) + eni(b, y, m) + eni(c, z, m)


def part_1_value(string):
    res = []
    fields = string.split(" ")
    for field in fields:
        _, v = field.split("=")
        res.append(int(v))
    return part_1_formula(res[0], res[1], res[2], res[3], res[4], res[5], res[6])


def part_1(input, part=1):
    Run_st01_01.PART = part
    maximum = 0
    for line in input_generator(input):
        v = part_1_value(line)
        maximum = max(maximum, v)
    return maximum


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_st01_01().run_cmdline()
