from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_08(DayBase):
    YEAR = "2015"
    DAY = "08"


def part_a_score(line):
    # count 2 for opening/closing quotes, one per \, but three for \x (four chars to 1)
    score = 2
    print(line)
    i = 0
    while i < len(line):
        print(i, line[i])
        # TODO: better with raw strings?
        if line[i] == "\\":
            i += 1
            score += 1
            if line[i] == "x":
                score += 2
                i += 2
        i += 1
    return score


def part_b_score(line):
    # count 2 for new opening/closing quotes, then one for each \ or "
    score = 2
    for i in range(len(line)):
        if line[i] == "\\" or line[i] == '"':
            score += 1
    return score


def part_a(input):
    score = 0
    for line in input_generator(input):
        score += part_a_score(line)
    return score


def part_b(input):
    score = 0
    for line in input_generator(input):
        score += part_b_score(line)
    return score


if __name__ == "__main__":
    Run_2015_08().run_cmdline()
