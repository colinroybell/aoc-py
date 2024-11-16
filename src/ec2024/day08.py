from utils.day_base import DayBase
from utils.data_input import input_generator
from math import sqrt


class Run_2024_08(DayBase):
    YEAR = "2024"
    DAY = "08"
    PREFIX = "ec"


def part_1(input):
    # Round up to nearest square number.
    bricks = int(next(input_generator(input)))
    size = int(sqrt(bricks) + 1)
    base = size * 2 - 1
    excess = size * size - bricks
    print(size, base, excess)
    return base * excess


def part_2(input):
    line = next(input_generator(input))
    (priests, acolytes, blocks) = [int(x) for x in line.split(",")]
    thickness = 1
    layer = 1
    used = 0
    while 1:
        round = (layer * 2 - 1) * thickness
        used += round
        print(layer, round)
        if used >= blocks:
            break
        layer += 1
        thickness = (thickness * priests) % acolytes
    return (used - blocks) * (layer * 2 - 1)


def part_3(input):
    line = next(input_generator(input))
    (priests, acolytes, blocks) = [int(x) for x in line.split(",")]
    print(priests, acolytes, blocks)
    thickness = 1
    layer = 1
    used = 0
    deltas = []
    while 1:
        deltas.append(thickness)
        total = 0
        used = 0
        for d in range(layer):
            total += deltas[layer - 1 - d]
            remove = (total * priests * (layer * 2 - 1)) % acolytes
            if d == layer - 1:
                used += total - remove
            elif d > 0:
                used += (total - remove) * 2
            else:
                used += total * 2
        if used >= blocks:
            break
        layer += 1
        thickness = ((thickness * priests) % acolytes) + acolytes
    return used - blocks


if __name__ == "__main__":
    Run_2024_08().run_cmdline()
