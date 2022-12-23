from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from utils.grid_2d import Grid2d
import re


class Run_2022_09(DayBase):
    YEAR = "2022"
    DAY = "09"


def sign(a):
    return (a > 0) - (a < 0)


def part_a(input):
    grid = Grid2d()
    head = Vec2d(0, 0)
    tail = Vec2d(0, 0)
    parse_re = re.compile(r"(.)\s(\d+)")
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        dir = m.group(1)
        count = int(m.group(2))
        for _ in range(count):
            head = head.move(dir)
            if head.x == tail.x and abs(head.y - tail.y) == 2:
                tail = tail + Vec2d(0, sign(head.y - tail.y))
            elif head.y == tail.y and abs(head.x - tail.x) == 2:
                tail = tail + Vec2d(sign(head.x - tail.x), 0)
            elif (
                head.x != tail.x
                and head.y != tail.y
                and (abs(head.x - tail.x) == 2 or abs(head.y - tail.y) == 2)
            ):
                tail = tail + Vec2d(sign(head.x - tail.x), sign(head.y - tail.y))
            print(head, tail)
            grid.set(tail, 1)
    return grid.count_non_zero()


def part_b(input):
    grid = Grid2d()
    knot = [Vec2d(0, 0) for _ in range(10)]
    parse_re = re.compile(r"(.)\s(\d+)")
    for line in input_generator(input):
        m = parse_re.match(line)
        assert m
        dir = m.group(1)
        count = int(m.group(2))
        for _ in range(count):
            knot[0] = knot[0].move(dir)
            for i in range(0, 9):
                if knot[i].x == knot[i + 1].x and abs(knot[i].y - knot[i + 1].y) == 2:
                    knot[i + 1] = knot[i + 1] + Vec2d(
                        0, sign(knot[i].y - knot[i + 1].y)
                    )
                elif knot[i].y == knot[i + 1].y and abs(knot[i].x - knot[i + 1].x) == 2:
                    knot[i + 1] = knot[i + 1] + Vec2d(
                        sign(knot[i].x - knot[i + 1].x), 0
                    )
                elif (
                    knot[i].x != knot[i + 1].x
                    and knot[i].y != knot[i + 1].y
                    and (
                        abs(knot[i].x - knot[i + 1].x) == 2
                        or abs(knot[i].y - knot[i + 1].y) == 2
                    )
                ):
                    knot[i + 1] = knot[i + 1] + Vec2d(
                        sign(knot[i].x - knot[i + 1].x), sign(knot[i].y - knot[i + 1].y)
                    )
            grid.set(knot[9], 1)
    return grid.count_non_zero()


if __name__ == "__main__":
    Run_2022_09().run_cmdline()
