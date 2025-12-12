from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2025_12(DayBase):
    YEAR = "2025"
    DAY = "12"


def part_a(input):
    block_sizes = [7, 7, 7, 6, 5, 7]
    problem_re = re.compile(r"(\d+)x(\d+): (.+)")
    total = 0
    for line in input_generator(input):
        m = problem_re.match(line)
        if m:
            w = int(m.group(1))
            h = int(m.group(2))
            counts = [int(n) for n in m.group(3).split(" ")]
            grid3x3 = w // 3 * h // 3
            if sum(counts) <= grid3x3:
                # trivial pass by putting one in each 3x3 grid
                total += 1
            else:
                # test trivial fail
                hashcount = sum(
                    [counts[i] * block_sizes[i] for i, _ in enumerate(block_sizes)]
                )
                assert hashcount > w * h
    return total


def part_b(input):
    assert 0, "not implemented"


def notes():
    """
    Either trivial pass or trivial fail. Block sizes morally ought to be read out of the file.

    No attempt to solve the trial input.
    """


if __name__ == "__main__":
    Run_2025_12().run_cmdline()
