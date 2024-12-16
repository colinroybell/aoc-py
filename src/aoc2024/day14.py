from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2024_14(DayBase):
    YEAR = "2024"
    DAY = "14"


def split_to_xy(split_re, string):
    m = split_re.search(string)
    print(string)
    assert m
    return (int(m.group(1)), int(m.group(2)))


def part_a(input, width=101, height=103):
    split_re = re.compile(r"\=(.+),(.+)")
    counts = [0, 0, 0, 0]
    for line in input_generator(input):
        pv = line.split()
        (px, py) = split_to_xy(split_re, pv[0])
        (vx, vy) = split_to_xy(split_re, pv[1])

        x = (px + vx * 100) % width
        y = (py + vy * 100) % height
        if x < width // 2:
            x_bucket = 0
        elif x > width // 2:
            x_bucket = 1
        else:
            x_bucket = None
        if y < height // 2:
            y_bucket = 0
        elif y > height // 2:
            y_bucket = 1
        else:
            y_bucket = None
        if x_bucket != None and y_bucket != None:
            counts[x_bucket + 2 * y_bucket] += 1
        print(x, y, x_bucket, y_bucket, counts)
    prod = 1
    for c in counts:
        prod *= c
    return prod


def part_b(input, width=101, height=103):
    split_re = re.compile(r"\=(.+),(.+)")
    counts = [0, 0, 0, 0]
    robots = []
    for line in input_generator(input):
        pv = line.split()
        (px, py) = split_to_xy(split_re, pv[0])
        (vx, vy) = split_to_xy(split_re, pv[1])
        robots.append([px, py, vx, vy])

    min_sigma = None
    min_time = None
    for t in range(10000):
        sigma = 0
        for px, py, vx, vy in robots:
            x = (px + vx * t) % width
            y = (py + vy * t) % height
            sigma += (x - width // 2) ** 2 + (y - height // 2) ** 2

        if min_sigma == None or sigma < min_sigma:
            min_sigma = sigma
            min_time = t

    return min_time


if __name__ == "__main__":
    Run_2024_14().run_cmdline()
