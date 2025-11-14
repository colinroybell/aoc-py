from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_08(DayBase):
    YEAR = "2025"
    DAY = "08"
    PREFIX = "ec"


def part_1(input, nails=32):
    line = next(input_generator(input))
    positions = [int(n) for n in line.split(",")]
    count = 0
    for i in range(len(positions) - 1):
        p0 = positions[i]
        p1 = positions[i + 1]
        if (p0 - p1) % nails == nails / 2:
            count += 1
    return count


def knot_needed(nails, a, b, c, d):
    bb = (b - a) % nails
    cc = (c - a) % nails
    dd = (d - a) % nails
    x = min(cc, dd)
    y = max(cc, dd)
    return 0 < x < bb < y


def cut(nails, a, b, c, d):
    bb = (b - a) % nails
    cc = (c - a) % nails
    dd = (d - a) % nails
    x = min(cc, dd)
    y = max(cc, dd)
    return 0 < x < bb < y or (x == 0 and y == bb)


def part_2(input, nails=256):
    line = next(input_generator(input))
    positions = [int(n) for n in line.split(",")]
    count = 0
    for i in range(len(positions) - 1):
        i0 = positions[i]
        i1 = positions[i + 1]
        for j in range(0, i):
            j0 = positions[j]
            j1 = positions[j + 1]
            if knot_needed(nails, i0, i1, j0, j1):
                count += 1
    return count


# Long run-time. Is there a more efficient way? We have 4100 threads, so counting pairs not likely to gain much.


def part_3(input, nails=256):
    line = next(input_generator(input))
    positions = [int(n) for n in line.split(",")]
    count = 0
    max_count = 0
    for i0 in range(0, nails):
        for i1 in range(i0 + 1, nails):
            count = 0
            for j in range(len(positions) - 1):
                j0 = positions[j]
                j1 = positions[j + 1]
                if cut(nails, i0, i1, j0, j1):
                    count += 1
            max_count = max(count, max_count)
        print(i0, max_count)
    return max_count


if __name__ == "__main__":
    Run_2025_08().run_cmdline()
