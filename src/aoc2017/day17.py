from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_17(DayBase):
    YEAR = "2017"
    DAY = "17"


def spinlock(buffer, value, pos, advance):
    # length is same as value
    pos = (pos + advance) % value
    buffer = buffer[: (pos + 1)] + [value] + buffer[(pos + 1) :]
    return buffer, pos + 1


def part_a(input):
    buffer = [0]
    advance = int(next(input_generator(input)))
    pos = 0
    for i in range(1, 2018):
        buffer, pos = spinlock(buffer, i, pos, advance)
    nextPos = (pos + 1) % (i + 1)
    print(len(buffer), pos, i, nextPos)
    return buffer[nextPos]


def part_b(input):
    advance = int(next(input_generator(input)))
    # Don't need to actually add the numbers
    last_post_0 = None
    pos = 0
    for i in range(1, 50000001):
        pos = (pos + advance) % i
        if pos == 0:
            last_post_0 = i
        pos += 1
    return last_post_0


if __name__ == "__main__":
    Run_2017_17().run_cmdline()
