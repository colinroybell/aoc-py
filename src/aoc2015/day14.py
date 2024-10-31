from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2015_14(DayBase):
    YEAR = "2015"
    DAY = "14"


def distance(time, speed, fly_time, rest_time):
    loop_time = fly_time + rest_time
    loops = time // loop_time
    excess_time = time % loop_time
    loops_distance = loops * speed * fly_time
    excess_distance = min(fly_time, excess_time) * speed
    return loops_distance + excess_distance


def part_a(input, time=2503):
    number_re = re.compile(r".+?(\d+).+?(\d+).+?(\d+).+?")
    win_dist = 0
    for line in input_generator(input):
        m = number_re.match(line)
        win_dist = max(
            win_dist, distance(time, int(m.group(1)), int(m.group(2)), int(m.group(3)))
        )
    return win_dist


def part_b(input, time=2503):
    number_re = re.compile(r".+?(\d+).+?(\d+).+?(\d+).+?")
    reindeer = []
    count = 0
    scores = []
    for line in input_generator(input):
        m = number_re.match(line)
        reindeer.append([count, int(m.group(1)), int(m.group(2)), int(m.group(3))])
        scores.append(0)
        count += 1

    for t in range(1, time + 1):
        win_dist = 0
        winners = []
        for r in range(count):
            dist = distance(t, reindeer[r][1], reindeer[r][2], reindeer[r][3])
            if dist > win_dist:
                win_dist = dist
                winners = [r]
            elif dist == win_dist:
                winners.append(r)
        for r in winners:
            scores[r] += 1

    return max(scores)


if __name__ == "__main__":
    Run_2015_14().run_cmdline()
