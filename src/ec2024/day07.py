from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_07(DayBase):
    YEAR = "2024"
    DAY = "07"
    PREFIX = "ec"


class Squire:
    def __init__(self, name, plan):
        self.name = name
        self.power = 10
        self.plan = plan
        self.score = 0

    def update_power(self, time, force=None):
        pos = (time - 1) % len(self.plan)
        c = self.plan[pos]
        if force == "+" or force == "-":
            c = force
        if c == "+":
            self.power += 1
        elif c == "-" and self.power > 0:
            self.power -= 1
        self.score += self.power


def part_1(input):
    squires = {}
    for line in input_generator(input):
        name = line[0]
        plan = line[2:].split(",")
        squires[name] = Squire(name, plan)

    for time in range(1, 11):
        for s in squires.values():
            s.update_power(time)

    return "".join(sorted(squires, key=lambda key: squires[key].score, reverse=True))


def part_2(input):
    track = ""
    end_track = ""
    track_done = False
    first = True
    squires = {}
    for line in input_generator(input):
        if first:
            track = line[1:]
            end_track = line[0]
            first = False
        elif not track_done:
            if " " in line:
                track += line[-1]
                end_track = line[0] + end_track
            else:
                track += line[::-1] + end_track
                track_done = True
        else:
            if line == "":
                next
            else:
                name = line[0]
                plan = line[2:].split(",")
                squires[name] = Squire(name, plan)
    time = 0
    for loop in range(10):
        for t in track:
            time += 1
            for s in squires.values():
                s.update_power(time, force=t)
    return "".join(sorted(squires, key=lambda key: squires[key].score, reverse=True))


def squire_score(track, plan, rounds):
    # 2024 is a multiple of 11. We have 5+, 3-, and a lot of + forcing early on, so no need to deal with case of hitting 0 (we assert)
    # s.power after 11 rounds should be constant (depends on counts of +-= on track) so score after 11 rounds is sufficient, but we've done it properly for now.
    s = Squire("", plan)
    assert rounds % 11 == 0
    time = 0
    for loop in range(11):
        for t in track:
            time += 1
            s.update_power(time, force=t)
            assert s.power >= 1
    N = rounds // 11
    return s.score * N + (s.power - 10) * 11 * len(track) * N * (N - 1) // 2


def generate_pattern(string, plus, minus, equals):
    if plus == 0 and minus == 0 and equals == 0:
        yield string
    else:
        if plus > 0:
            yield from generate_pattern(string + "+", plus - 1, minus, equals)
        if minus > 0:
            yield from generate_pattern(string + "-", plus, minus - 1, equals)
        if equals > 0:
            yield from generate_pattern(string + "=", plus, minus, equals - 1)


def part_3(input):
    grid = Grid2d()
    # TODO: fix reading so we pass a input_generator
    grid.read_from_file_strings(input)
    opp_line = "A:-,-,+,=,+,+,=,+,-,+,="
    opp_plan = opp_line[2:].split(",")
    last_pos = Vec2d(0, 0)
    pos = Vec2d(1, 0)
    c = grid.get(pos)
    track = ""
    while c != "S":
        track += c
        for v in pos.get_adjacent_orthogonal():
            c = grid.get(v)
            if v != last_pos and c != " " and c != None:
                last_pos = pos
                pos = v
                break
    track += "S"
    target = squire_score(track, opp_plan, 2024)

    total = 0
    for string in generate_pattern("", 5, 3, 3):
        score = squire_score(track, string, 2024)
        if score > target:
            total += 1
    return total


if __name__ == "__main__":
    Run_2024_07().run_cmdline()
