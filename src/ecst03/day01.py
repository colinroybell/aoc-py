from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_st03_01(DayBase):
    YEAR = "st03"
    DAY = "01"
    PREFIX = "ec"


def toValue(string):
    value = 0
    for c in string:
        value *= 2
        if c.isupper():
            value += 1

    return value


def part_1(input):
    total = 0
    for line in input_generator(input):
        fields = line.split(":")
        score = int(fields[0])
        binaries = fields[1].split(" ")
        values = [toValue(b) for b in binaries]
        for p, v in enumerate(values):
            print(v, p, values[1])
            if v >= values[1] and p != 1:
                break
        else:
            total += score
        print(score, values)
    return total


def part_2(input):
    total = 0
    highest_shine = 0
    highest_sum = 0
    best_score = 0
    for line in input_generator(input):
        fields = line.split(":")
        score = int(fields[0])
        binaries = fields[1].split(" ")
        values = [toValue(b) for b in binaries]
        sum_ = sum(values[:3])
        if values[3] > highest_shine:
            highest_shine = values[3]
            highest_sum = sum_
            best_score = score
        elif values[3] == highest_shine:
            if sum_ < highest_sum:
                highest_sum = sum_
                best_score = score
    return best_score


def matte_shiny(value):
    if value >= 33:
        return 1
    elif value <= 30:
        return 0
    else:
        return None


def dominant_colour(values):
    m = max(values)
    d = None
    for p, v in enumerate(values):
        if v == m:
            if d == None:
                d = p
            else:
                return None
    return d


def part_3(input):
    best_total = 0
    totals = [[0 for i in range(3)] for j in range(2)]
    for line in input_generator(input):
        fields = line.split(":")
        score = int(fields[0])
        binaries = fields[1].split(" ")
        values = [toValue(b) for b in binaries]
        m_s = matte_shiny(values[3])
        dom = dominant_colour(values[:3])
        if m_s != None and dom != None:
            totals[m_s][dom] += score
    return max(map(max, totals))


if __name__ == "__main__":
    Run_st03_01().run_cmdline()
