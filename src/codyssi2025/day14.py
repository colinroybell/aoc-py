from utils.day_base import DayBase
from utils.data_input import input_generator
import re
import sys


class Run_2025_14(DayBase):
    YEAR = "2025"
    DAY = "14"
    PREFIX = "codyssi"


class Item:
    def __init__(self, id, quality, cost, materials):
        self.id = id
        self.quality = quality
        self.cost = cost
        self.materials = materials
        self.ratio = self.quality / self.cost

    def __repr__(self):
        return "{}".format(self.id)

    def __lt__(self, other):
        if self.quality < other.quality:
            return 1
        if self.quality > other.quality:
            return 0
        if self.cost < other.cost:
            return 1
        return 0


def parse_file(input):
    items = []
    parse_re = re.compile(
        r"(\d+)\s(\S+) \| Quality : (\d+), Cost : (\d+), Unique Materials : (\d+)"
    )
    for line in input_generator(input):
        fields = line.split()
        m = parse_re.match(line)
        assert m
        item = Item(m.group(2), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        items.append(item)
    return items


def part_1(input):
    items = parse_file(input)
    items.sort(reverse=True)
    total = 0
    for i in range(5):
        total += items[i].materials
    return total


class Score:
    def __init__(self, cost, quality, materials):
        self.cost = cost
        self.quality = quality
        self.materials = materials

    def __add__(self, other):
        return Score(
            self.cost + other.cost,
            self.quality + other.quality,
            self.materials + other.materials,
        )

    def __lt__(self, other):
        if self.quality < other.quality:
            return 1
        if self.quality > other.quality:
            return 0
        if self.materials > other.materials:
            return 1
        return 0

    def __repr__(self):
        return "cost {} quality {} materials {}".format(
            self.cost, self.quality, self.materials
        )


states = 0


def recurse_search(items, selected, score, first, budget, best_so_far, cache):
    global states
    states += 1
    best = max(best_so_far, score)
    remaining = budget - score.cost
    state = (first, remaining)
    # Keep a cache of best score we've got to with this budget remaining and this index to look at.
    if state in cache and score < cache[state]:
        return best
    cache[state] = score
    for i in range(first, len(items)):
        # Give up if we couldn't get to the existing best based on cost ratio
        if best.quality + remaining * items[i].ratio <= best_so_far.quality:
            break
        if items[i].cost <= remaining:
            updated_score = score + Score(
                items[i].cost, items[i].quality, items[i].materials
            )
            updated_selected = selected + [items[i].id]
            best_score = recurse_search(
                items, updated_selected, updated_score, i + 1, budget, best, cache
            )
            best = max(best, best_score)
    return best


def part_2(input, budget=30):
    items = parse_file(input)
    # Greedy search
    items.sort(reverse=True, key=lambda x: x.ratio)
    cache = {}
    best = recurse_search(items, [], Score(0, 0, 0), 0, budget, Score(0, 0, 0), cache)
    return best.quality * best.materials


def part_3(input, budget=300):
    return part_2(input, budget)


if __name__ == "__main__":
    Run_2025_14().run_cmdline()
