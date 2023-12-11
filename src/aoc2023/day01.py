from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2023_01(DayBase):
    YEAR = "2023"
    DAY = "01"


def part_a(input):
    total = 0
    for line in input_generator(input):
        i = 0
        while not line[i].isdigit():
            i += 1
        j = -1
        while not line[j].isdigit():
            j -= 1
        value = int(line[i] + line[j])
        total += value
    return total


def part_b(input):
    strings = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    total = 0
    for line in input_generator(input):
        # Add string to end as str[-4:0] doesn't do what you expect.
        line += " "
        i = 0
        found = False
        while not found:
            for count, s in enumerate(strings):
                length = len(s)
                if line[i : i + length] == s:
                    found = True
                    if count < 10:
                        v0 = count
                    else:
                        v0 = count - 9
            i += 1
        j = -1
        found = False
        while not found:
            for count, s in enumerate(strings):
                length = len(s)
                if s == "nine":
                    print(line[j - length : j], s)
                if line[j - length : j] == s:
                    found = True
                    if count < 10:
                        v1 = count
                    else:
                        v1 = count - 9
            j -= 1
        value = v0 * 10 + v1
        print(v0, v1)
        total += value
    return total


if __name__ == "__main__":
    Run_2023_01().run_cmdline()
