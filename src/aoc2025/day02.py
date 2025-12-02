from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_02(DayBase):
    YEAR = "2025"
    DAY = "02"


def is_invalid(string, part):
    length = len(string)
    if part == "a":
        if length % 2:
            return False
        else:
            return string[: length // 2] == string[length // 2 :]
    else:
        for n in range(2, length + 1):
            if length % n == 0:
                s = length // n
                comp = string[:s]
                for i in range(1, n):
                    if string[i * s : (i + 1) * s] != comp:
                        break
                else:
                    return True
        return False


def part_a(input, part="a"):
    ranges = next(input_generator(input)).split(",")
    count = 0
    for r in ranges:
        low, high = [int(n) for n in r.split("-")]
        for id in range(low, high + 1):
            if is_invalid(str(id), part):
                print(id)
                count += int(id)
    return count


def part_b(input):
    return part_a(input, part="b")


def notes():
    """
    First part does a full search, whereas it ought to be possible to do it via construction. Second part ditto. Current time for part 2 is 1.5s so nice to get it down"""


if __name__ == "__main__":
    Run_2025_02().run_cmdline()
