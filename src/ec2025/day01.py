from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_01(DayBase):
    YEAR = "2025"
    DAY = "01"
    PREFIX = "ec"


def part_1(input, part=1):
    generator = input_generator(input)
    line = next(generator)
    names = line.split(",")
    empty = next(generator)
    assert empty == ""
    instructions = next(generator)
    pos = 0
    num_names = len(names)
    for inst in instructions.split(","):
        dir = inst[0]
        num = int(inst[1:])
        if dir == "L":
            diff = -num
        else:
            diff = num
        if part == 1:
            pos = min(max(pos + diff, 0), num_names - 1)
        elif part == 2:
            pos = (pos + diff) % num_names
        else:
            diff = diff % num_names
            names[0], names[diff] = names[diff], names[0]

    if part < 3:
        return names[pos]
    else:
        return names[0]


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2025_01().run_cmdline()
