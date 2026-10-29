from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2026_02(DayBase):
    YEAR = "2026"
    DAY = "02"
    PREFIX = "ec"


def part_1(input):
    generator = input_generator(input)
    total = 0
    for line in generator:
        # count the number we are bigger than, which gives positional place
        counts = [0 for _ in range(6)]
        items = line.split(" ")
        for item in items:
            if item[1] == "<":
                bigger = item[2]
            else:
                bigger = item[0]
            counts[int(bigger)] += 1
        score = 0
        for c in range(1, 6):
            score += c * pow(10, counts[c])
        total += score
    return total


def part_2(input):
    generator = input_generator(input)
    total = 0
    for line in generator:
        # We don't know size ahead of time - this is sufficient for our data.
        biggers = [[] for _ in range(10)]
        items = line.split(" ")
        max_number = 0
        for item in items:
            right = int(item[2])
            left = int(item[0])
            if item[1] == "<":
                biggers[right].append(left)
            else:
                biggers[left].append(right)
            max_number = max(max_number, left)
            max_number = max(max_number, right)
        for a in range(1, max_number + 1):
            for b in range(a + 1, max_number + 1):
                if b not in biggers[a] and a not in biggers[b]:
                    # Look up from first element in list
                    if len(biggers[a]) and b in biggers[biggers[a][0]]:
                        biggers[a].append(b)
                    elif len(biggers[b]) and a in biggers[biggers[b][0]]:
                        biggers[b].append(a)
                    else:
                        assert 0, "can't resolve missing"
        score = 0
        for c in range(1, max_number + 1):
            score += c * pow(10, len(biggers[c]))
            print(c, score)
        total += score
    return total


def part_3(input):
    generator = input_generator(input)
    total = 0
    for line in generator:
        max_number = 0
        biggers = [[] for _ in range(10)]
        items = line.split(" ")
        numbers_remaining = set()
        for item in items:
            right = int(item[2])
            left = int(item[0])
            if item[1] == "<":
                biggers[right].append(left)
            else:
                biggers[left].append(right)
            max_number = max(max_number, left)
            max_number = max(max_number, right)
            numbers_remaining.add(left)
            numbers_remaining.add(right)
        mult = 1
        score = 0
        # By construction, there will be one number each time which is not bigger than anything:
        # it is therefore the smallest. Remove it and iterate
        while len(numbers_remaining):
            smallest = None
            for n in numbers_remaining:
                if len(biggers[n]) == 0:
                    assert smallest == None
                    smallest = n
            score += mult * smallest
            mult *= 10
            numbers_remaining.remove(smallest)
            for n in numbers_remaining:
                if smallest in biggers[n]:
                    biggers[n].remove(smallest)
        total += score
    return total


if __name__ == "__main__":
    Run_2026_02().run_cmdline()
