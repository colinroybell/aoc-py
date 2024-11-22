from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_11(DayBase):
    YEAR = "2024"
    DAY = "11"
    PREFIX = "ec"


def part_1(input, start="A", days=4):
    transitions = {}
    termites = []
    for line in input_generator(input):
        t, trans = line.split(":")
        transitions[t] = trans.split(",")
        termites.append(t)

    blank_counts = {t: 0 for t in termites}
    counts = blank_counts.copy()
    counts[start] = 1

    for _ in range(days):
        new_counts = blank_counts.copy()
        for t in termites:
            for tt in transitions[t]:
                new_counts[tt] += counts[t]
        print(new_counts)
        counts = new_counts

    return sum(counts[t] for t in termites)


def part_2(input):
    return part_1(input, start="Z", days=10)


def part_3(input, days=20):
    transitions = {}
    termites = []
    for line in input_generator(input):
        t, trans = line.split(":")
        transitions[t] = trans.split(",")
        termites.append(t)

    blank_counts = {t: 0 for t in termites}

    counts = {}
    for d in range(days, -1, -1):
        counts[d] = {}
        for t in termites:
            counts[d][t] = blank_counts.copy()
            if d == days:
                counts[d][t][t] = 1
            else:
                for tt in transitions[t]:
                    for ttt in termites:
                        counts[d][t][ttt] += counts[d + 1][tt][ttt]
            s = sum(counts[d][t][tt] for tt in termites)
            print(d, t, s)
    sums = [sum(counts[d][t][tt] for tt in termites) for t in termites]
    return max(sums) - min(sums)


if __name__ == "__main__":
    Run_2024_11().run_cmdline()
