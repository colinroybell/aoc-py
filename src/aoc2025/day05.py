from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_05(DayBase):
    YEAR = "2025"
    DAY = "05"


def part_a(input):
    ranges = []
    generator = input_generator(input)
    for line in generator:
        if line == "":
            break
        min, max = [int(n) for n in line.split("-")]
        ranges.append((min, max))
    total = 0
    for line in generator:
        n = int(line)
        for r in ranges:
            if r[0] <= n <= r[1]:
                total += 1
                break
    return total


def part_b(input):
    ranges = []
    generator = input_generator(input)
    for line in generator:
        if line == "":
            break
        _min, _max = [int(n) for n in line.split("-")]
        ranges.append([_min, _max])

    ranges.sort(key=lambda r: r[0])

    total = 0
    current = None
    for r in ranges:
        if current == None:
            current = r
        elif r[0] > current[1] + 1:
            total += current[1] - current[0] + 1
            current = r
        else:
            current[1] = max(current[1], r[1])
    total += current[1] - current[0] + 1
    return total


if __name__ == "__main__":
    Run_2025_05().run_cmdline()
