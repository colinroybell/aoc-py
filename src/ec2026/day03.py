from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2026_03(DayBase):
    YEAR = "2026"
    DAY = "03"
    PREFIX = "ec"


def part_1(input):
    generator = input_generator(input)
    total = 0
    for line in generator:
        fields = line.split(" ")
        powers_input = fields[0][4:]
        values = fields[1]
        powers = powers_input
        while len(powers) < len(values):
            powers += powers_input
        powers = powers[-len(values) :]
        score = 0
        for i in range(0, len(values)):
            score += pow(int(powers[-(i % len(powers)) - 1]), i) * int(values[-i - 1])
            print(i, score)
        total += score
    return total


def part_2(input):
    return part_1(input)


def part_3_recurse(powers, value, cache):
    key = (value, tuple(powers))
    if key in cache:
        return cache[key]
    if len(powers) == 1:
        if value <= 9:
            return value
        else:
            return None
    weight = pow(int(powers[0]), len(powers) - 1)
    for v in range(0, 10):
        remainder = value - v * weight
        if remainder >= 0:
            sub_solution = part_3_recurse(powers[1:], remainder, cache)
            if sub_solution:
                solution = v * pow(10, len(powers) - 1) + sub_solution
                cache[key] = solution
                return solution
    cache[key] = None
    return None


def part_3(input):
    generator = input_generator(input)
    total = 0
    cache = {}
    for line in generator:
        fields = line.split(" ")
        powers_input = fields[0][5:]
        values = fields[1]
        powers = powers_input
        while len(powers) < len(values):
            powers += powers_input
        powers = powers[-len(values) :]
        score = 0
        for i in range(0, len(values)):
            score += pow(int(powers[-i - 1]), i) * int(values[-i - 1])
        best_rep = part_3_recurse(powers, score, cache)
        if str(best_rep) == values:
            total += score
    return total


if __name__ == "__main__":
    Run_2026_03().run_cmdline()
