from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2023_11(DayBase):
    YEAR = "2023"
    DAY = "11"


def part_a(input, part_b=False, expansion_factor=None):
    y = 0
    galaxies = []
    rows_hit = []
    cols_hit = []
    for line in input_generator(input):
        if y == 0:
            cols_hit = [0] * len(line)
        row_hit = 0
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append((x, y))
                cols_hit[x] = 1
                row_hit = 1
        rows_hit.append(row_hit)
        y += 1

    expansion = 1
    if part_b:
        expansion = expansion_factor - 1

    t = 0
    rows_bonus = []
    for i in rows_hit:
        if i == 0:
            t += expansion
        rows_bonus.append(t)

    t = 0
    cols_bonus = []
    for i in cols_hit:
        if i == 0:
            t += expansion
        cols_bonus.append(t)

    total = 0
    for i, g1 in enumerate(galaxies):
        for _, g2 in enumerate(galaxies[i + 1 :]):
            g1x = g1[0] + cols_bonus[g1[0]]
            g1y = g1[1] + rows_bonus[g1[1]]
            g2x = g2[0] + cols_bonus[g2[0]]
            g2y = g2[1] + rows_bonus[g2[1]]
            d = abs(g1x - g2x) + abs(g1y - g2y)
            total += d

    return total


def part_b(input, expansion_factor=1000000):
    return part_a(input, True, expansion_factor)


if __name__ == "__main__":
    Run_2023_11().run_cmdline()
