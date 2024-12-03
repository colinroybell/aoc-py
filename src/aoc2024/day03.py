from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2024_03(DayBase):
    YEAR = "2024"
    DAY = "03"


def part_a(input):
    mulre = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    for line in input_generator(input):
        finds = mulre.findall(line)
        for f in finds:
            print(f)
            total += int(f[0]) * int(f[1])
    return total


def part_b(input):
    mulre = re.compile(r"^mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    enabled = True
    for line in input_generator(input):

        for i in range(len(line)):
            subline = line[i:]
            if subline.startswith("do()"):
                enabled = True
            elif subline.startswith("don't()"):
                enabled = False
            elif enabled and subline.startswith("mul"):
                m = mulre.match(subline)
                if m:
                    total += int(m.group(1)) * int(m.group(2))
    return total


if __name__ == "__main__":
    Run_2024_03().run_cmdline()
