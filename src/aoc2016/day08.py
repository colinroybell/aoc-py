from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2016_08(DayBase):
    YEAR = "2016"
    DAY = "08"


def part_a(input, width=50, height=6, part_b=False):
    part_a = not part_b
    number_re = re.compile(r"(\d+).+?(\d+)")
    grid = [[0 for _ in range(height)] for _ in range(width)]
    colcopy = [0 for _ in range(height)]
    rowcopy = [0 for _ in range(width)]
    for line in input_generator(input):
        m = number_re.search(line)
        n1 = int(m.group(1))
        n2 = int(m.group(2))

        if line.startswith("rect"):
            for x in range(n1):
                for y in range(n2):
                    grid[x][y] = 1
        elif line.startswith("rotate c"):
            x = n1
            for y in range(height):
                colcopy[(y + n2) % height] = grid[x][y]
            for y in range(height):
                grid[x][y] = colcopy[y]
        elif line.startswith("rotate r"):
            y = n1
            for x in range(width):
                rowcopy[(x + n2) % width] = grid[x][y]
            for x in range(width):
                grid[x][y] = rowcopy[x]
    if part_a:
        total = sum(grid[x][y] for x in range(width) for y in range(height))
        return total
    else:
        string = ""
        for y in range(height):
            for x in range(width):
                if grid[x][y]:
                    string += "#"
                else:
                    string += "."
            string += "\n"
        return string


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2016_08().run_cmdline()
