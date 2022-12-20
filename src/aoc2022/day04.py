from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2022_04(DayBase):
    YEAR = "2022"
    DAY = "04"


def part_a(input):
    count = 0
    parse_re = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        val = [int(m.group(i)) for i in range(1, 5)]
        if val[0] <= val[2] <= val[3] <= val[1] or val[2] <= val[0] <= val[1] <= val[3]:
            count += 1
    return count


def part_b(input):
    count = 0
    parse_re = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        val = [int(m.group(i)) for i in range(1, 5)]
        if (
            val[0] <= val[2] <= val[1]
            or val[0] <= val[3] <= val[1]
            or val[2] <= val[0] <= val[3]
            or val[2] <= val[1] <= val[3]
        ):
            count += 1
    return count


if __name__ == "__main__":
    Run_2022_04().run_cmdline()
