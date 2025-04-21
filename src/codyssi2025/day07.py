from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_07(DayBase):
    YEAR = "2025"
    DAY = "07"
    PREFIX = "codyssi"


def part_1(input):
    freqs = [None]
    generator = input_generator(input)
    for line in generator:
        if not line:
            break
        freqs.append(int(line))

    for line in generator:
        if not line:
            break
        fields = line.split("-")
        p0 = int(fields[0])
        p1 = int(fields[1])
        freqs[p0], freqs[p1] = freqs[p1], freqs[p0]

    line = next(generator)
    pos = int(line)
    return freqs[pos]


def part_2(input):
    freqs = [None]
    generator = input_generator(input)
    for line in generator:
        if not line:
            break
        freqs.append(int(line))

    swaps = []

    for line in generator:
        if not line:
            break
        fields = line.split("-")
        p0 = int(fields[0])
        p1 = int(fields[1])
        swaps.append((p0, p1))

    length = len(swaps)

    for s in range(length):
        p0 = swaps[s][0]
        p1 = swaps[s][1]
        p2 = swaps[(s + 1) % length][0]

        freqs[p0], freqs[p1], freqs[p2] = freqs[p2], freqs[p0], freqs[p1]

    line = next(generator)
    pos = int(line)
    return freqs[pos]


def part_3(input):
    freqs = [None]
    generator = input_generator(input)
    for line in generator:
        if not line:
            break
        freqs.append(int(line))

    length = len(freqs) - 1

    for line in generator:
        if not line:
            break
        fields = line.split("-")
        p0 = int(fields[0])
        p1 = int(fields[1])
        if p0 > p1:
            p0, p1 = p1, p0
        base1 = p1

        while p0 < base1 and p1 <= length:
            freqs[p0], freqs[p1] = freqs[p1], freqs[p0]
            p0 += 1
            p1 += 1

    line = next(generator)
    pos = int(line)
    return freqs[pos]


if __name__ == "__main__":
    Run_2025_07().run_cmdline()
