from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d


class Run_2021_02(DayBase):
    YEAR = "2021"
    DAY = "02"


class Position:
    def __init__(self):
        self.horiz = 0
        self.depth = 0
        self.aim = 0

    def down(self, dist):
        self.aim += dist

    def forward(self, dist):
        self.horiz += dist
        self.depth += self.aim * dist

    def score(self):
        return self.horiz * self.depth


def part_a(input):
    pos = Vec2d(0, 0)
    for line in input_generator(input):
        words = line.split(" ")
        dir = words[0]
        dist = int(words[1])
        if dir == "forward":
            vec = Vec2d(dist, 0)
        elif dir == "down":
            vec = Vec2d(0, dist)
        elif dir == "up":
            vec = Vec2d(0, -dist)
        else:
            assert 0, "bad direction {}".format(dir)
        pos = pos + vec
    return pos.x * pos.y


def part_b(input):
    pos = Position()
    for line in input_generator(input):
        words = line.split(" ")
        dir = words[0]
        dist = int(words[1])
        if dir == "forward":
            pos.forward(dist)
        elif dir == "down":
            pos.down(dist)
        elif dir == "up":
            pos.down(-dist)
        else:
            assert 0, "bad direction {}".format(dir)
    return pos.score()


if __name__ == "__main__":
    Run_2021_02().run_cmdline()
