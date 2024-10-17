from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_05(DayBase):
    YEAR = "2020"
    DAY = "05"


def seat_id(code):
    row = 0
    for i in range(0, 7):
        row *= 2
        if code[i] == 'B':
            row += 1
    col = 0
    for i in range(7, 10):
        col *= 2
        if code[i] == 'R':
            col += 1
    return row * 8 + col


def part_a(input):
    max_id = 0
    for line in input_generator(input):
        id = seat_id(line)
        max_id = max(max_id, id)
    return max_id


def part_b(input):
    ids = set()
    for line in input_generator(input):
        id = seat_id(line)
        ids.add(id)

    for seat in ids:
        if (seat + 2) in ids and not (seat + 1) in ids:
            return seat + 1
    return 0

if __name__ == "__main__":
    Run_2020_05().run_cmdline()

