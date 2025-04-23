from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_10(DayBase):
    YEAR = "2025"
    DAY = "10"
    PREFIX = "codyssi"


def part_1(input):
    data = []
    rows = 0
    for line in input_generator(input):
        fields = line.split()
        row = [int(n) for n in fields]
        data.append(row)
        rows += 1
        cols = len(row)

    row_min = min([sum(data[i][j] for j in range(cols)) for i in range(rows)])
    col_min = min([sum(data[i][j] for i in range(rows)) for j in range(cols)])

    return min(row_min, col_min)


def part_2(input, part=2):
    data = []
    rows = 0
    for line in input_generator(input):
        fields = line.split()
        row = [int(n) for n in fields]
        data.append(row)
        rows += 1
        cols = len(row)

    danger = []

    if part == 2:
        last_row = 15
        last_col = 15
    else:
        last_row = rows
        last_col = cols

    for row in range(last_row):
        danger.append([])
        for col in range(last_col):

            if row == 0 and col == 0:
                d = 0
            elif row == 0:
                d = danger[0][col - 1]
            elif col == 0:
                d = danger[row - 1][0]
            else:
                d = min(danger[row - 1][col], danger[row][col - 1])
            d += data[row][col]
            danger[row].append(d)
    return danger[-1][-1]


def part_3(input):
    return part_2(input, part=3)


if __name__ == "__main__":
    Run_2025_10().run_cmdline()
