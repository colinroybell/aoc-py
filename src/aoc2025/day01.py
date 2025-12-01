from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_01(DayBase):
    YEAR = "2025"
    DAY = "01"


def part_a(input, part="a"):
    pos = 50
    mul = {"R": 1, "L": -1}
    total = 0
    rounds = 0
    for line in input_generator(input):
        dir = line[0]
        steps = int(line[1:])
        start = pos
        pos += mul[dir] * steps
        pos %= 100
        if pos == 0:
            total += 1
        print(dir, steps, pos, rounds, total)
    return total


def part_b(input):
    pos = 50
    mul = {"R": 1, "L": -1}
    total = 0
    rounds = 0
    for line in input_generator(input):
        dir = line[0]
        steps = int(line[1:])
        start = pos
        pos += mul[dir] * steps
        rounds = pos // 100
        if rounds > 0:
            total += rounds
        elif rounds < 0:
            total += abs(rounds)
            if start == 0:
                total -= 1
        pos = pos % 100
        if pos == 0 and rounds <= 0:
            total += 1
        print(dir, steps, pos, rounds, total)
    return total


def notes(input):
    """
    Quite awkward to get part b correct. Rightward fell out correctly,
    but leftward we need a couple of offsets to deal with the case where
    we are starting or ending on a zero.

    Needed to write own test case 2 to sort it out - goes from 50 to 800
    and back picking up all the coverage cases.
    """


if __name__ == "__main__":
    Run_2025_01().run_cmdline()
