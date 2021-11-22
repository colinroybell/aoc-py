from aoc2015.day02 import score
from utils.day_base import DayBase
from utils.data_input import input_generator
import re
import itertools


class Run_2015_13(DayBase):
    YEAR = "2015"
    DAY = "13"


def part_a(input, part_b=False):
    people = []
    scores = {}
    parse_re = re.compile(
        r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\."
    )
    if part_b:
        people.append("You")
        scores["You"] = {}
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        person = m.group(1)
        score = int(m.group(3))
        if m.group(2) == "lose":
            score = -score
        other = m.group(4)
        if person not in people:
            people.append(person)
            scores[person] = {}
            if part_b:
                scores[person]["You"] = 0
                scores["You"][person] = 0
        scores[person][other] = score
    best = None
    # Circular table, so we can assume one person is fixed
    for p in itertools.permutations(people[1:]):
        pp = [people[0]] + list(p) + [people[0]]
        score = 0
        for i in range(0, len(pp) - 1):
            score += scores[pp[i]][pp[i + 1]] + scores[pp[i + 1]][pp[i]]
        if not best or score > best:
            best = score
    return best


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2015_13().run_cmdline()
