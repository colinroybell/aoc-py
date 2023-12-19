from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2023_19(DayBase):
    YEAR = "2023"
    DAY = "19"


class Cond:
    def init_class():
        Cond.match_re = re.compile(r"(.)(.)(\d+)")

    def __init__(self, string):
        if string:
            m = Cond.match_re.match(string)
            self.attr = m.group(1)
            self.cond = m.group(2)
            self.value = int(m.group(3))
            assert self.cond in "<>"
        else:
            self.cond = True

    def check(self, part):
        if self.cond == True:
            return True
        value = part.get_attr(self.attr)
        if self.cond == "<":
            return value < self.value
        else:
            return value > self.value

    def check_block(self, block):
        if self.cond == True:
            return (block, None)
        range = block.get_attr(self.attr)
        if self.cond == "<":
            if range[1] - 1 < self.value:
                return (block, None)
            elif range[0] >= self.value:
                return (None, block)
            else:
                split = self.value
        if self.cond == ">":
            if range[0] > self.value:
                return (block, None)
            elif range[1] - 1 <= self.value:
                return (None, block)
            else:
                split = self.value + 1

        block0 = block.split(self.attr, (range[0], split))
        block1 = block.split(self.attr, (split, range[1]))
        if self.cond == "<":
            return (block0, block1)
        else:
            return (block1, block0)


class Rule:
    def init_class():
        Rule.match_re = re.compile(r"(.+?)\{(.+?)\}")

    def __init__(self, string):
        m = Rule.match_re.match(string)
        self.name = m.group(1)
        rule_strings = m.group(2).split(",")
        self.rules = []
        for r in rule_strings:
            try:
                colon = r.index(":")
            except ValueError:
                colon = None
            if colon:
                self.rules.append((Cond(r[:colon]), r[colon + 1 :]))
            else:
                self.rules.append((Cond(None), r))

    def next(self, part):
        for rule in self.rules:
            if rule[0].check(part):
                return rule[1]
        assert 0

    def next_block(self, block):
        output = []
        for rule in self.rules:
            (block_in, block_out) = rule[0].check_block(block)
            if block_in:
                output.append((block_in, rule[1]))
            if block_out:
                block = block_out
            else:
                break
        return output


class Part:
    def __init__(self, string):
        string = string[1:-1]
        attrs = string.split(",")
        self.attrs = {}
        for a in attrs:
            attr = a[0]
            value = int(a[2:])
            self.attrs[attr] = value

    def get_attr(self, attr):
        return self.attrs[attr]

    def get_score(self):
        return sum(self.attrs.values())


class PartBlock:
    def __init__(self, ranges):
        self.ranges = ranges

    def get_attr(self, attr):
        return self.ranges[attr]

    def split(self, attr, range):
        new_block = PartBlock(self.ranges.copy())
        new_block.ranges[attr] = range
        return new_block

    def get_score(self):
        prod = 1
        for r in self.ranges.values():
            prod *= r[1] - r[0]
        return prod

    def __repr__(self):
        return self.ranges.__repr__()


def part_a(input, part_b=False):
    part_a = not part_b
    Cond.init_class()
    Rule.init_class()
    parse_rules = True
    rules = {}
    parts = []
    for line in input_generator(input):
        if parse_rules:
            if line == "":
                parse_rules = False
                continue
            rule = Rule(line)
            rules[rule.name] = rule
        else:
            parts.append(Part(line))
    score = 0
    if part_a:

        for part in parts:
            rule = "in"
            while 1:
                if rule == "A":
                    score += part.get_score()
                    break
                if rule == "R":
                    break
                rule = rules[rule].next(part)
    else:
        ranges = {}
        for attr in "xmas":
            ranges[attr] = (1, 4001)
        block = PartBlock(ranges)
        block_queue = [(block, "in")]
        while block_queue:
            (block, rule) = block_queue.pop()
            if rule == "A":
                score += block.get_score()
            elif rule == "R":
                pass
            else:
                output = rules[rule].next_block(block)
                block_queue.extend(output)
    return score


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_19().run_cmdline()
