from utils.day_base import DayBase
from utils.data_input import input_generator
import hashlib


class Run_2015_04(DayBase):
    YEAR = "2015"
    DAY = "04"


def part_a(input, start="00000"):
    key = next(input_generator(input))
    found = False
    count = 1
    while not found:
        string = key + str(count)
        string = string.encode("utf-8")
        hash = hashlib.md5(string).hexdigest()
        if hash[0 : len(start)] == start:
            found = True
        else:
            count += 1
        if count % 10000 == 0:
            print(count)

    return count


def part_b(input):
    return part_a(input, start="000000")


if __name__ == "__main__":
    Run_2015_04().run_cmdline()
