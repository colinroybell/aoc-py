from utils.day_base import DayBase
from utils.data_input import input_generator
from statistics import median


class Run_2021_10(DayBase):
    YEAR = "2021"
    DAY = "10"


match = {"}": "{", "]": "[", ")": "(", ">": "<"}
closing = "}])>"
points = {"}": 1197, "]": 57, ")": 3, ">": 25137}
comp_score = {"(": 1, "[": 2, "{": 3, "<": 4}


def part_a_score(line):
    score = 0
    cache = ""
    for c in line:
        if c in closing:
            if match[c] == cache[-1]:
                cache = cache[:-1]
            else:
                score = points[c]
                break
        else:
            cache += c
    if score:
        return (score, None)
    else:
        score = 0
        while cache:
            c = cache[-1]
            cache = cache[:-1]
            score = score * 5 + comp_score[c]
        return (0, score)


def part_a(input, part_b=False):

    score = 0
    part_b_scores = []
    for line in input_generator(input):
        line_score, part_b_score = part_a_score(line)
        if not part_b:
            score += line_score
        else:
            if part_b_score is not None:
                part_b_scores.append(part_b_score)
    if not part_b:
        return score
    else:
        return median(part_b_scores)

    return score


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_10().run_cmdline()
