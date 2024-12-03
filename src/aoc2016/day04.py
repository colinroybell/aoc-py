from utils.day_base import DayBase
from utils.data_input import input_generator
import re
from collections import defaultdict


class Run_2016_04(DayBase):
    YEAR = "2016"
    DAY = "04"


def part_a(input):
    parse_re = re.compile(r"(.+)-(\d+)\[(.{5})\]")

    total = 0
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        letters = m.group(1)
        id = int(m.group(2))
        top5 = m.group(3)

        counts = defaultdict(lambda: 0)
        for letter in letters:
            if letter != "-":
                counts[letter] += 1

        sorted_items = sorted(list(counts.items()), key=lambda x: (-x[1], x[0]))
        sorted_top5 = "".join([sorted_items[i][0] for i in range(5)])
        print(top5, sorted_top5)
        if top5 == sorted_top5:
            total += id
    return total


def part_b(input):
    parse_re = re.compile(r"(.+)-(\d+)\[(.{5})\]")

    total = 0
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        letters = m.group(1)
        id = int(m.group(2))
        top5 = m.group(3)
        output = ""
        for letter in letters:
            if letter != "-":
                output += chr(97 + (ord(letter) - 97 + id) % 26)
            else:
                output += "-"
        print(output)
        if output == "northpole-object-storage":
            return id
    return None


if __name__ == "__main__":
    Run_2016_04().run_cmdline()
