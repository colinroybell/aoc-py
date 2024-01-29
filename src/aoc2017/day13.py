from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_13(DayBase):
    YEAR = "2017"
    DAY = "13"


def part_a(input):
    score = 0
    for line in input_generator(input):
        fields = line.split(":")
        depth = int(fields[0])
        range_ = int(fields[1])
        period = 2 * range_ - 2
        if depth % period == 0:
            score += depth * range_

    return score


# TODO: this runs fast enough, but more efficient would be to do a number theory version and spot modulos
def part_b(input):
    score = 0
    traps = {}
    for line in input_generator(input):
        fields = line.split(":")
        depth = int(fields[0])
        range_ = int(fields[1])
        period = 2 * range_ - 2
        if depth % period == 0:
            score += depth * range_
        traps[depth] = period

    delay = 0
    while 1:
        for depth, period in traps.items():
            if (depth + delay) % period == 0:
                break
        else:
            return delay
        delay += 1


if __name__ == "__main__":
    Run_2017_13().run_cmdline()
