from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_11(DayBase):
    YEAR = "2025"
    DAY = "11"


def score(node, links, scores):
    if node in scores:
        return scores[node]
    total = sum([score(n, links, scores) for n in links[node]])
    scores[node] = total
    return total


def part_a(input):
    links = {}
    for line in input_generator(input):
        fields = line.split(" ")
        source = fields[0][:-1]
        dests = fields[1:]
        links[source] = dests

    scores = {}
    scores["out"] = 1
    return score("you", links, scores)


def score_b(node, links, scores):
    if node in scores:
        return scores[node]

    total = [[0, 0], [0, 0]]
    for n in links[node]:
        s = score_b(n, links, scores)
        for x in range(2):
            for y in range(2):
                total[x][y] += s[x][y]

    if node == "dac":
        for x in range(2):
            total[x][1] += total[x][0]
            total[x][0] = 0

    if node == "fft":
        for y in range(2):
            total[1][y] += total[0][y]
            total[0][y] = 0

    scores[node] = total
    return total


def part_b(input):
    links = {}
    for line in input_generator(input):
        fields = line.split(" ")
        source = fields[0][:-1]
        dests = fields[1:]
        links[source] = dests

    scores = {}
    scores["out"] = [[1, 0], [0, 0]]
    return score_b("svr", links, scores)[1][1]


if __name__ == "__main__":
    Run_2025_11().run_cmdline()
