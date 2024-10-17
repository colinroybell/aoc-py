from utils.day_base import DayBase
from utils.data_input import input_generator
import re

class Run_2020_02(DayBase):
    YEAR = "2020"
    DAY = "02"

def part_a(input):
    pw_re = re.compile(r'(\d+)-(\d+) (.):\ (.+)')
    valid = 0
    for line in input_generator(input):
        m = pw_re.match(line)
        assert(m)
        min_ = int(m.group(1))
        max_ = int(m.group(2))
        char = m.group(3)
        pw = m.group(4)
        count = pw.count(char)
        if count >= min_ and count <= max_:
            valid += 1
    return valid


def part_b(input):
    pw_re = re.compile(r'(\d+)-(\d+) (.):\ (.+)')
    valid = 0
    for line in input_generator(input):
        m = pw_re.match(line)
        assert(m)
        pos1 = int(m.group(1)) - 1
        pos2 = int(m.group(2)) - 1
        char = m.group(3)
        pw = m.group(4)
        if (pw[pos1] == char) ^ (pw[pos2] == char):
            valid += 1
    return valid

if __name__ == "__main__":
    Run_2020_02().run_cmdline()

