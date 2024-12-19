from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_19(DayBase):
    YEAR = "2024"
    DAY = "19"


def pattern_possible(design, patterns, no_exact=False):
    for pattern in patterns:
        if design == pattern and not no_exact:
            return True
        if design.startswith(pattern):
            if pattern_possible(design[len(pattern) :], patterns):
                return True
    return False


def part_a(input):
    generator = input_generator(input)
    full_patterns = next(generator).split(", ")
    patterns = []
    for pattern in full_patterns:
        if pattern_possible(pattern, full_patterns, no_exact=True):
            pass
        else:
            patterns.append(pattern)
    _ = next(generator)
    count = 0
    for line in generator:
        if pattern_possible(line, patterns):
            count += 1
    return count


def pattern_count(design, patterns, cache):
    if design in cache:
        return cache[design]
    total = 0
    for pattern in patterns:
        if design == pattern:
            total += 1
        elif design.startswith(pattern):
            total += pattern_count(design[len(pattern) :], patterns, cache)
    cache[design] = total
    return total


def part_b(input):
    generator = input_generator(input)
    patterns = next(generator).split(", ")
    total = 0
    cache = {}
    for line in generator:
        total += pattern_count(line, patterns, cache)
    return total


if __name__ == "__main__":
    Run_2024_19().run_cmdline()
