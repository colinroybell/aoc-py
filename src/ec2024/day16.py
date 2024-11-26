from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.maths import lcm


class Run_2024_16(DayBase):
    YEAR = "2024"
    DAY = "16"
    PREFIX = "ec"


def part_1(input):
    generator = input_generator(input)
    line = next(generator)
    nums = [int(n) for n in line.split(",")]
    advances = nums
    wheels = len(advances)
    sequences = [[] for _ in range(wheels)]
    for line in generator:
        line += " " * (wheels * 4)
        for w in range(wheels):
            string = line[4 * w : 4 * w + 3]
            if string != "   ":
                sequences[w].append(string)
    output = ""
    for w in range(wheels):
        length = len(sequences[w])
        output += sequences[w][(100 * advances[w]) % length] + " "
    output = output[:-1]
    return output


def part_2(input, pulls=202420242024):
    generator = input_generator(input)
    line = next(generator)
    nums = [int(n) for n in line.split(",")]
    advances = nums
    wheels = len(advances)
    sequences = [[] for _ in range(wheels)]
    for line in generator:
        line += " " * (wheels * 4)
        for w in range(wheels):
            string = line[4 * w : 4 * w + 3]
            if string != "   ":
                sequences[w].append(string)

    # More efficient is to generate actual lcm, but for our data
    # all entries coprime
    length = 1
    for w in range(wheels):
        length = lcm(length, len(sequences[w]))

    rounds = pulls // length
    excess = pulls - rounds * length
    total = 0
    for p in range(length):
        if p % 10000 == 0:
            print(p, lcm)
        mult = rounds
        if p > 0 and p <= excess:
            mult += 1
        counts = {}
        for w in range(wheels):
            c = sequences[w][(p * advances[w]) % len(sequences[w])]
            if c[0] not in counts:
                counts[c[0]] = 1
            else:
                counts[c[0]] += 1
            if c[2] not in counts:
                counts[c[2]] = 1
            else:
                counts[c[2]] += 1
        for v in counts.values():
            if v >= 3:
                total += mult * (v - 2)

    return total


class Score:
    def __init__(self, base):
        self.base = base
        self.transitions = {}


class ScoreCache:
    def __init__(self, advances, sequences):
        self.cache = {}
        self.advances = advances
        self.sequences = sequences
        self.count = len(self.advances)

    def hash(self, pulls, base):
        return (pulls, tuple(base))

    def points(self, positions):
        counts = {}
        total = 0
        for w in range(self.count):
            c = self.sequences[w][positions[w]]
            if c[0] not in counts:
                counts[c[0]] = 1
            else:
                counts[c[0]] += 1
            if c[2] not in counts:
                counts[c[2]] = 1
            else:
                counts[c[2]] += 1
        for v in counts.values():
            if v >= 3:
                total += v - 2
        return total

    def get_from_cache(self, pulls, base):
        full_hash = self.hash(pulls, base)
        if full_hash not in self.cache:
            score = Score(base)
            transitions = []
            if pulls == 1:
                for left in range(-1, 2):
                    position = []
                    for w in range(self.count):
                        position.append(
                            (base[w] + left + self.advances[w]) % len(self.sequences[w])
                        )
                    points = self.points(position)
                    score.transitions[tuple(position)] = [points, points]
            else:
                p1 = pulls // 2
                p2 = pulls - p1
                score = Score(base)
                score1 = self.get_from_cache(p1, base)
                for t1 in score1.transitions.keys():
                    score2 = self.get_from_cache(p2, t1)
                    for t2 in score2.transitions.keys():
                        new_max = score1.transitions[t1][0] + score2.transitions[t2][0]
                        new_min = score1.transitions[t1][1] + score2.transitions[t2][1]
                        if t2 not in score.transitions:
                            score.transitions[t2] = [new_max, new_min]
                        else:
                            score.transitions[t2] = [
                                max(score.transitions[t2][0], new_max),
                                min(score.transitions[t2][1], new_min),
                            ]
            self.cache[full_hash] = score
        return self.cache[full_hash]

    def get_max_min(self, pulls, base):
        score = self.get_from_cache(pulls, base)
        maximum = max(t[0] for t in score.transitions.values())
        minimum = min(t[1] for t in score.transitions.values())
        return (maximum, minimum)


def part_3(input, pulls=256):
    generator = input_generator(input)
    line = next(generator)
    nums = [int(n) for n in line.split(",")]
    advances = nums
    wheels = len(advances)
    sequences = [[] for _ in range(wheels)]
    for line in generator:
        line += " " * (wheels * 4)
        for w in range(wheels):
            string = line[4 * w : 4 * w + 3]
            if string != "   ":
                sequences[w].append(string)

    cache = ScoreCache(advances, sequences)
    maximum, minimum = cache.get_max_min(pulls, [0] * len(advances))
    return "{} {}".format(maximum, minimum)


if __name__ == "__main__":
    Run_2024_16().run_cmdline()
