from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_05(DayBase):
    YEAR = "2025"
    DAY = "05"
    PREFIX = "ec"


def score(line):
    id, rest = line.split(":")
    spine = []
    left = []
    right = []
    score = ""
    for r in rest.split(","):
        val = int(r)
        for p in range(len(spine)):
            if left[p] == None and val < spine[p]:
                left[p] = val
                break
            if right[p] == None and val > spine[p]:
                right[p] = val
                break
        else:
            spine.append(val)
            left.append(None)
            right.append(None)
            score += r
    return int(score)


def sword(line):
    id, rest = line.split(":")
    spine = []
    left = []
    right = []
    score = ""
    for r in rest.split(","):
        val = int(r)
        for p in range(len(spine)):
            if left[p] == None and val < spine[p]:
                left[p] = val
                break
            if right[p] == None and val > spine[p]:
                right[p] = val
                break
        else:
            spine.append(val)
            left.append(None)
            right.append(None)
            score += r
    row_sc = ""
    rows = []
    for p in range(len(spine)):
        if left[p]:
            row_sc += str(left[p])
        row_sc += str(spine[p])
        if right[p]:
            row_sc += str(right[p])
        rows.append(int(row_sc))

    return (int(id), int(score), rows)


def part_1(input):
    line = next(input_generator(input))
    return score(line)


def part_2(input):
    scores = []
    for line in input_generator(input):
        scores.append(score(line))
    return max(scores) - min(scores)


def part_3(input):
    swords = []
    for line in input_generator(input):
        id, score, rows = sword(line)
        vals = [score] + rows + [id]
        swords.append((id, vals))
    swords.sort(key=lambda s: s[1], reverse=True)
    checksum = 0
    for i, s in enumerate(swords):
        print(i, s[0], s[1][0])
        checksum += (i + 1) * s[0]
    return checksum


if __name__ == "__main__":
    Run_2025_05().run_cmdline()
