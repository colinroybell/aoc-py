from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_07(DayBase):
    YEAR = "2025"
    DAY = "07"
    PREFIX = "ec"


def part_1(input, part=1):
    generator = input_generator(input)
    names = next(generator).split(",")
    blank = next(generator)
    assert blank == ""
    rules = {}
    for line in generator:
        a, b = line.split(" > ")
        outputs = b.split(",")
        rules[a] = outputs

    passes = ""
    score = 0
    count = 0
    for name in names:
        count += 1
        prev = None
        # print(name)
        for n in name:
            if prev and n not in rules[prev]:
                break
            prev = n
        else:
            passes += name
            score += count
    if part == 1:
        return passes
    else:
        return score


def part_2(input):
    return part_1(input, part=2)


# Note: could be made a lot more efficient by cacheing the number of suffixes which can be made to
# eg a name of length 8 ending in r. Runtime is about a second so haven't needed this.


def recurse(name, rules):
    count = 0
    if len(name) >= 7:
        count = 1
    if len(name) == 11:
        return count
    last_c = name[-1]
    if last_c in rules:
        for c in rules[last_c]:
            count += recurse(name + c, rules)
    return count


def part_3(input):
    generator = input_generator(input)
    names = next(generator).split(",")
    blank = next(generator)
    assert blank == ""
    rules = {}
    for line in generator:
        a, b = line.split(" > ")
        outputs = b.split(",")
        rules[a] = outputs

    count = 0
    for name in names:
        # Don't process if another name is our prefix (it would generate our names already)
        prefix = False
        for other in names:
            if other != name and name.startswith(other):
                prefix = True
                break
        if prefix:
            continue

        prev = None
        for n in name:
            if prev and n not in rules[prev]:
                break
            prev = n
        else:
            count += recurse(name, rules)
            print(name, count)
    return count


if __name__ == "__main__":
    Run_2025_07().run_cmdline()
