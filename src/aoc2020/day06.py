from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_06(DayBase):
    YEAR = "2020"
    DAY = "06"


def group_score_a(lines):
    responses = set()
    for line in lines:
        for char in line:
            responses.add(char)
    return len(responses)


def group_score_b(lines):
    responses = set()
    for char in lines[0]:
        responses.add(char)

    for line in lines:
        r_copy = [r for r in responses]
        for r in r_copy:
            if r not in line:
                responses.remove(r)
    return len(responses)


def group_score(part, lines):
    if part == "a":
        return group_score_a(lines)
    else:
        return group_score_b(lines)


def both_parts(part, input):
    group = []
    total = 0
    for line in input_generator(input):
        if line == "":
            total += group_score(part, group)
            group = []
        else:
            group.append(line)
    total += group_score(part, group)
    return total


def part_a(input):
    return both_parts("a", input)


def part_b(input):
    return both_parts("b", input)


if __name__ == "__main__":
    Run_2020_06().run_cmdline()
