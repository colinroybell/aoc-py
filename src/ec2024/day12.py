from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d


class Run_2024_12(DayBase):
    YEAR = "2024"
    DAY = "12"
    PREFIX = "ec"


def part_1(input, part=1):
    total = 0
    mults = {"T": 1, "H": 2}
    lines = [line for line in input_generator(input)]
    print(lines)
    for count, line in enumerate(lines):
        y = len(lines) - 2 - count  # treat A as ground
        for pos, c in enumerate(line):
            if c == "T" or c == "H":
                x = pos - 1
                dist = x + y
                power = dist // 3
                catapult_score = (dist % 3) + 1
                score = power * catapult_score
                print(score * mults[c])

                total += score * mults[c]
    return total


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    total = 0
    for line in input_generator(input):
        (orig_x, orig_y) = [int(f) for f in line.split()]
        x = orig_x // 2
        y = orig_y - (orig_x - x)
        best_score = None
        print("meteor", orig_x, orig_y, " hit at ", x, y)
        for h in range(0, 3):
            hit = False
            catapult_mult = h + 1
            yy = y - h
            if yy > x:
                # Too high. Can't hit
                pass
            elif yy == x and yy > 0:
                power = yy * catapult_mult
                hit = True
                print("Hit height", h, "phase 1, power", power)
            elif yy > 0 and x > yy and x <= 2 * yy:
                power = yy * catapult_mult
                hit = True
                print("Hit height", h, "phase 2, power", power)
            else:
                # find positive intercept
                xx = yy + x
                if xx % 3 == 0:
                    power = (xx // 3) * catapult_mult
                    assert power > 0
                    hit = True
                    print("Hit height", h, "phase 3, power", power)

            if hit:
                if best_score == None or power < best_score:
                    best_score = power
        print(
            "({},{})  scores  {}  at time {}".format(
                orig_x, orig_y, best_score, orig_x - x
            )
        )
        assert best_score
        total += best_score

    return total


class Meteor:
    def __init__(self, x, y):
        self.base = Vec2d(x, y)

    def pos_at_time(self, t):
        return self.base + Vec2d(-1, -1) * t


class Projectile:
    def __init__(self, height, power):
        self.height = height
        self.power = power

    def score(self):
        return self.power * (self.height + 1)

    def pos_at_time(self, t):
        if t <= self.power:
            return Vec2d(t, t + self.height)
        elif t <= 2 * self.power:
            return Vec2d(t, self.power + self.height)
        else:
            return Vec2d(t, self.height + self.power - (t - 2 * self.power))


def part_3_new(input):
    total = 0
    meteors = []
    for line in input_generator(input):
        (orig_x, orig_y) = [int(f) for f in line.split()]
        meteors.append(Meteor(orig_x, orig_y))

    score_array = {}
    projectiles = []
    for height in range(0, 3):
        projectiles.append(Projectile(height, 1))

    t = 1
    while len(meteors) and t < 4000:
        for height in range(0, 3):
            projectiles.append(Projectile(height, t))
        new_projectiles = []
        for p in projectiles:
            pos = p.pos_at_time(t)
            if pos.y >= 0:
                score = p.score()
                pos = pos
                if pos in score_array:
                    score_array[pos] = min(score_array[pos], score)
                else:
                    score_array[pos] = score
                new_projectiles.append(p)
        new_meteors = []
        for m in meteors:
            pos = m.pos_at_time(t)
            pos = pos
            if pos in score_array:
                score = score_array[pos]
                print(m.base, " scores ", score, " at time", t)
                total += score
            else:
                new_meteors.append(m)
        projectiles = new_projectiles
        meteors = new_meteors
        t += 1
    return total


if __name__ == "__main__":
    Run_2024_12().run_cmdline()
