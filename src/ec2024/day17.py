from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d


class Run_2024_17(DayBase):
    YEAR = "2024"
    DAY = "17"
    PREFIX = "ec"


def part_1(input):
    # Prim's algorithm
    stars = []

    for y, line in enumerate(input_generator(input)):
        for x, c in enumerate(line):
            if c == "*":
                stars.append(Vec2d(x, y))
    count = len(stars)
    min_dist = [None for _ in range(count)]
    total = 0
    for round in range(count):
        if round == 0:
            best = 0
            best_score = 0
        else:
            best = None
            best_score = None
            for s in range(count):
                if min_dist[s] > 0 and (best_score == None or min_dist[s] < best_score):
                    best_score = min_dist[s]
                    best = s
        total += best_score + 1
        for s in range(count):
            if min_dist[s] == None or min_dist[s] > 0:
                new_dist = stars[s].manhattan(stars[best])
                if min_dist[s] == None or new_dist < min_dist[s]:
                    min_dist[s] = new_dist
    return total


def part_2(input):
    return part_1(input)


def part_3(input):
    stars = []

    for y, line in enumerate(input_generator(input)):
        for x, c in enumerate(line):
            if c == "*":
                stars.append(Vec2d(x, y))
    count = len(stars)
    min_dist = [6 for _ in range(count)]
    const_scores = []
    total = None
    for round in range(count):
        best = None
        best_score = None
        for s in range(count):
            if min_dist[s] > 0 and (best_score == None or min_dist[s] < best_score):
                best_score = min_dist[s]
                best = s
        if best_score < 6:
            total += best_score + 1
        else:
            if total != None:
                const_scores.append(total)
            total = 1
        for s in range(count):
            if min_dist[s] == None or min_dist[s] > 0:
                new_dist = stars[s].manhattan(stars[best])
                if min_dist[s] == None or new_dist < min_dist[s]:
                    min_dist[s] = new_dist
    const_scores.append(total)
    const_scores.sort(reverse=1)
    return const_scores[0] * const_scores[1] * const_scores[2]


if __name__ == "__main__":
    Run_2024_17().run_cmdline()
