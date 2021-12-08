from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2021_08(DayBase):
    YEAR = "2021"
    DAY = "08"


def part_a(input):
    data = ""
    count = 0
    for line in input_generator(input):
        data += line
        if data[-1] == "|":
            data += " "
            continue
        words = data.split()
        for word in words[10:]:
            if 2 <= len(word) <= 4 or len(word) == 7:
                count += 1
        data = ""
    return count


def find_missing(word):
    for c in "abcdefg":
        if c not in word:
            return c


def identify(string, chars):
    digits = [
        "ABCEFG",
        "CF",
        "ACDEG",
        "ACDFG",
        "BCDF",
        "ABDFG",
        "ABDEFG",
        "ACF",
        "ABCDEFG",
        "ABCDFG",
    ]

    for val, d in enumerate(digits):
        if len(d) != len(string):
            continue
        ok = True
        for c in d:
            if chars[c] not in string:
                ok = False
                continue
        if ok:
            return val
    assert 0, "not found"


def part_b(input):
    data = ""
    sum_ = 0
    for line in input_generator(input):
        data += line
        if data[-1] == "|":
            data += " "
            continue
        words = data.split()
        nums = words[0:10]
        missing6 = ""
        found = ""
        for word in nums:
            if len(word) == 2:
                w2 = word
            if len(word) == 3:
                w3 = word
            if len(word) == 4:
                w4 = word
            if len(word) == 6:
                missing6 += find_missing(word)
        chars = {}
        for c in w2:
            if c in missing6:
                chars["C"] = c
            else:
                chars["F"] = c
            found += c

        for c in w3:
            if c != chars["C"] and c != chars["F"]:
                chars["A"] = c
                found += c

        for c in w4:
            if c != chars["C"] and c != chars["F"]:
                if c in missing6:
                    chars["D"] = c
                else:
                    chars["B"] = c
                found += c

        for c in missing6:
            if c != chars["C"] and c != chars["D"]:
                chars["E"] = c
                found += c

        chars["G"] = find_missing(found)
        score = 0
        for word in words[11:]:

            score = 10 * score + identify(word, chars)
        sum_ += score
        data = ""

    return sum_


if __name__ == "__main__":
    Run_2021_08().run_cmdline()
