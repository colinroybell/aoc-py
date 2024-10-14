from utils.day_base import DayBase
from utils.data_input import input_generator
from .knothash import knothash


class Run_2017_10(DayBase):
    YEAR = "2017"
    DAY = "10"


def part_a(input, part_b=False, length=256):
    part_a = not part_b
    line = next(input_generator(input))
    if part_a:
        lengths = [int(n) for n in line.split(",")]
    else:
        lengths = [ord(char) for char in line] + [17, 31, 73, 47, 23]

    n = []
    for i in range(length):
        n.append(i)

    pos = 0
    skipSize = 0

    if part_a:
        iterations = 1
    else:
        iterations = 64

    for _ in range(iterations):
        for k in lengths:
            for l in range(k // 2):
                p1 = (pos + l) % length
                p2 = (pos + k - 1 - l) % length
                t = n[p1]
                n[p1] = n[p2]
                n[p2] = t
            pos = (pos + k + skipSize) % length
            skipSize += 1
            print(n)
    if part_a:
        return n[0] * n[1]

    out = ""
    for c in range(16):
        x = 0
        for i in range(16):
            x ^= n[c * 16 + i]
        out += "{:02x}".format(x)

    return out

def part_b(input):
    return knothash(next(input_generator(input)))
    #return part_a(input, True)


if __name__ == "__main__":
    Run_2017_10().run_cmdline()
