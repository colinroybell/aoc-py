from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_09(DayBase):
    YEAR = "2025"
    DAY = "09"
    PREFIX = "ec"


def similarity(child, p1, p2):
    s1 = 0
    s2 = 0
    for g in range(len(child)):
        m1 = child[g] == p1[g]
        m2 = child[g] == p2[g]
        if not m1 and not m2:
            return 0
        if m1:
            s1 += 1
        if m2:
            s2 += 1
    return s1 * s2


def part_1(input):
    genomes = {}
    ids = []
    for line in input_generator(input):
        id, genome = line.split(":")
        genomes[id] = genome
        ids.append(id)
        length = len(genome)

    score = 0
    for child in range(len(ids)):
        for p0 in range(len(ids)):
            if p0 == child:
                continue
            for p1 in range(p0 + 1, len(ids)):
                if p1 == child:
                    continue
                score += similarity(
                    genomes[ids[child]], genomes[ids[p0]], genomes[ids[p1]]
                )
    return score


def part_2(input):
    return part_1(input)


def part_3(input):
    genomes = {}
    ids = []
    links = {}
    for line in input_generator(input):
        id, genome = line.split(":")
        id = int(id)
        genomes[id] = genome
        ids.append(id)
        length = len(genome)
        links[id] = []

    for child in range(len(ids)):
        for p0 in range(len(ids)):
            if p0 == child:
                continue
            for p1 in range(p0 + 1, len(ids)):
                if p1 == child:
                    continue
                c_id = ids[child]
                p0_id = ids[p0]
                p1_id = ids[p1]
                if similarity(genomes[c_id], genomes[p0_id], genomes[p1_id]):
                    links[c_id].append(p0_id)
                    links[c_id].append(p1_id)
                    links[p0_id].append(c_id)
                    links[p1_id].append(c_id)

    done = {}
    max_count = 0
    max_total = 0
    for id in ids:
        if id in done:
            continue
        count = 0
        total = 0
        stack = []
        stack.append(id)
        while stack:
            node = stack.pop()
            if node in done:
                continue
            count += 1
            total += node
            done[node] = True
            for link in links[node]:
                if link not in done:
                    stack.append(link)
        if count > max_count:
            max_count = count
            max_total = total
    return max_total


if __name__ == "__main__":
    Run_2025_09().run_cmdline()
