from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_12(DayBase):
    YEAR = "2020"
    DAY = "12"


def pos_add(pos, d):
    return (pos[0] + d[0], pos[1] + d[1])


def delta_mult(delta, m):
    return (delta[0] * m, delta[1] * m)


def rotate_right(delta):
    return (-delta[1], delta[0])


def rotate_left(delta):
    return (delta[1], -delta[0])


def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])


def part_a(input):
    # E and S are positive, x is first coord
    pos = (0, 0)
    dir_ = (1, 0)
    for line in input_generator(input):
        cmd = line[0]
        val = int(line[1:])
        delta = (0, 0)
        if cmd == "F":
            delta = delta_mult(dir_, val)
        elif cmd == "N":
            delta = (0, -val)
        elif cmd == "S":
            delta = (0, val)
        elif cmd == "E":
            delta = (val, 0)
        elif cmd == "W":
            delta = (-val, 0)
        elif cmd == "R":
            assert val % 90 == 0
            for i in range(val // 90):
                dir_ = rotate_right(dir_)
        elif cmd == "L":
            assert val % 90 == 0
            for i in range(val // 90):
                dir_ = rotate_left(dir_)
        pos = pos_add(pos, delta)
        print(pos, dir_)
    return manhattan(pos)


def part_b(input):
    # E and S are positive, x is first coord
    pos = (0, 0)
    waypt = (10, -1)
    for line in input_generator(input):
        cmd = line[0]
        val = int(line[1:])
        delta = (0, 0)
        waypt_delta = (0, 0)
        if cmd == "F":
            delta = delta_mult(waypt, val)
        elif cmd == "N":
            waypt_delta = (0, -val)
        elif cmd == "S":
            waypt_delta = (0, val)
        elif cmd == "E":
            waypt_delta = (val, 0)
        elif cmd == "W":
            waypt_delta = (-val, 0)
        elif cmd == "R":
            assert val % 90 == 0
            for i in range(val // 90):
                waypt = rotate_right(waypt)
        elif cmd == "L":
            assert val % 90 == 0
            for i in range(val // 90):
                waypt = rotate_left(waypt)
        waypt = pos_add(waypt, waypt_delta)
        pos = pos_add(pos, delta)
        print(pos, waypt)
    return manhattan(pos)


if __name__ == "__main__":
    Run_2020_12().run_cmdline()
