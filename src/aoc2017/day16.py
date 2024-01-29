from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2017_16(DayBase):
    YEAR = "2017"
    DAY = "16"


def part_a(input, part_b=False, length=16):
    part_a = not part_b
    ps = re.compile(r"s(\d+)")
    px = re.compile(r"x(\d+)/(\d+)")
    pp = re.compile(r"p(.)/(.)")
    perm = []
    outputs = []
    lookup = {}
    for i in range(length):
        perm.append(chr(97 + i))

    def spin(n):
        nonlocal perm
        perm = perm[-n:] + perm[:-n]

    def exchange(m, n):
        nonlocal perm
        t = perm[m]
        perm[m] = perm[n]
        perm[n] = t

    def loc(c):
        nonlocal perm
        for i in range(length):
            if perm[i] == c:
                return i

    def partner(c1, c2):
        nonlocal perm
        exchange(loc(c1), loc(c2))

    line = next(input_generator(input))
    array = line.split(",")

    rounds = 1000000000
    for round in range(rounds):
        output = ""
        for i in range(length):
            output += perm[i]
        if part_a and round == 1:
            print(lookup, perm, round)
            return output
        if output in lookup:
            old = lookup[output]
            pos = old + (rounds - old) % (round - old)
            return outputs[pos]
        else:
            outputs.append(output)
            lookup[output] = round
        for instruction in array:
            ms = ps.match(instruction)
            mx = px.match(instruction)
            mp = pp.match(instruction)
            if ms:
                spin(int(ms.group(1)))
            elif mx:
                exchange(int(mx.group(1)), int(mx.group(2)))
            elif mp:
                partner(mp.group(1), mp.group(2))
            else:
                print("No match on {}".format(instruction))
                assert 0

    assert 0

    return output


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_16().run_cmdline()
