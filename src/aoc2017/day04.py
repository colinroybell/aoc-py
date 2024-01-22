from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_04(DayBase):
    YEAR = "2017"
    DAY = "04"


def isValidPassPhrase(line, part_b=False):
    words = line.split()
    if not words:
        return 0
    hash = {}
    print(line)
    for word in words:
        if part_b:
            word = "".join(sorted(word))
        if word in hash:
            print("Failed on {}".format(word))
            return 0
        hash[word] = 1
    return 1


def part_a(input):
    return sum(isValidPassPhrase(line) for line in input_generator(input))


def part_b(input):
    return sum(isValidPassPhrase(line, True) for line in input_generator(input))


if __name__ == "__main__":
    Run_2017_04().run_cmdline()
