from utils.day_base import DayBase
from utils.data_input import input_generator
import re
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_st02_03(DayBase):
    YEAR = "st02"
    DAY = "03"
    PREFIX = "ec"


class Die:
    def __init__(self, id, faces, seed):
        self.id = id
        self.seed = seed
        self.pulse = seed
        self.faces = faces
        self.roll_number = 0
        self.current = 0

    def roll(self):
        self.roll_number += 1
        spin = self.roll_number * self.pulse
        self.current = (self.current + spin) % len(self.faces)
        self.pulse += spin
        self.pulse %= self.seed
        self.pulse += 1 + self.roll_number + self.seed
        return self.faces[self.current]


def die_from_string(line):
    parse_re = re.compile(r"(\d+):\sfaces=\[(.*)\]\sseed=(\d+)")
    m = parse_re.match(line)
    assert m
    id = int(m.group(1))
    faces = [int(d) for d in m.group(2).split(",")]
    seed = int(m.group(3))

    die = Die(id, faces, seed)
    return die


def roll_test_function(input, **kwargs):

    die = die_from_string(next(input_generator(input)))

    assert "trace" in kwargs
    rolls = 0
    for line in input_generator(kwargs["trace"]):
        if not line:
            continue
        if line[0] != " ":
            continue
        fields = line.split()
        if fields[0] == "-":
            continue
        roll = int(fields[0])
        # Could expose spin but unnecessary
        exp_result = int(fields[2])
        exp_pulse = int(fields[3])
        result = None
        while rolls < roll:
            result = die.roll()
            rolls += 1
        print(result, exp_result)
        assert result == exp_result
        assert die.pulse == exp_pulse

    return True


def part_1(input, roll_test=False, **kwargs):
    if roll_test:
        return roll_test_function(input, **kwargs)
    dice = []
    for line in input_generator(input):
        dice.append(die_from_string(line))

    total = 0
    roll = 0
    while total < 10000:
        roll += 1
        score = 0
        for die in dice:
            score += die.roll()
        total += score
    return roll


def part_2(input):
    dice = []
    generator = input_generator(input)
    for line in generator:
        if not line:
            break
        else:
            dice.append(die_from_string(line))
    track = next(generator)
    track = [int(t) for t in track]
    len_track = len(track)
    players = len(dice)
    pos = [0 for _ in range(players)]
    done = [False for _ in range(players)]
    num_done = 0
    finishing_order = ""

    roll = 0
    while num_done < players:
        roll += 1
        for i, die in enumerate(dice):
            if done[i]:
                continue
            result = die.roll()
            if result == track[pos[i]]:
                pos[i] += 1
                if pos[i] == len(track):
                    done[i] = True
                    num_done += 1
                    finishing_order += ",{}".format(die.id)
    return finishing_order[1:]


def part_3(input):
    dice = []
    generator = input_generator(input)
    for line in generator:
        if not line:
            break
        else:
            dice.append(die_from_string(line))
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings_generator(
        generator, convert_to_int=True
    )
    marked_grid = Grid2d()

    for die in dice:
        result = die.roll()
        candidates = set()
        for x in range(width):
            for y in range(height):
                v = Vec2d(x, y)
                if grid.get(v) == result:
                    candidates.add(v)
                    marked_grid.set(v, 1)
        while candidates:
            result = die.roll()
            new_candidates = set()
            for c in candidates:
                adj = [c] + c.get_adjacent_orthogonal()
                for a in adj:
                    if grid.get(a) == result:
                        new_candidates.add(a)
                        marked_grid.set(a, 1)
            candidates = new_candidates

    return marked_grid.count_non_zero()


if __name__ == "__main__":
    Run_st02_03().run_cmdline()
