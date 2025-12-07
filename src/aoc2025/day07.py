from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2025_07(DayBase):
    YEAR = "2025"
    DAY = "07"


def part_a(input):
    grid = Grid2d()

    (width, height) = grid.read_from_file_strings_generator(input_generator(input))

    for x in range(width):
        start = Vec2d(x, 0)
        if grid.get(start) == "S":
            break

    splits = 0
    candidates = [start]
    while candidates:
        p = candidates.pop()
        if grid.get(p) == "|":
            continue
        grid.set(p, "|")
        p = p + Vec2d(0, 1)
        s = grid.get(p)
        if s == None or s == "|":
            continue
        if s == "^":
            candidates += [p + Vec2d(1, 0), p + Vec2d(-1, 0)]
            splits += 1
        else:
            candidates += [p]
    return splits


class TachyonCounts:
    def __init__(self, input):
        self.grid = Grid2d()
        (width, height) = self.grid.read_from_file_strings_generator(
            input_generator(input)
        )

        for x in range(width):
            self.start = Vec2d(x, 0)
            if self.grid.get(self.start) == "S":
                break
        self.counts = {}

    def process_recurse(self, p):
        if p in self.counts:
            return self.counts[p]
        s = self.grid.get(p)
        if s == None:
            return 1
        if s == "^":
            count = self.process_recurse(p + Vec2d(1, 0)) + self.process_recurse(
                p + Vec2d(-1, 0)
            )
        else:
            count = self.process_recurse(p + Vec2d(0, 1))
        self.counts[p] = count
        return count

    def process(self):
        return self.process_recurse(self.start)


def part_b(input):
    counts = TachyonCounts(input)

    return counts.process()


def notes():
    """
    Done a memoization with depth first recursion. Storing every point in the grid
    which is probably unnecessary - could do junction points.

    But better would be a breadth-first scan at each stage.
    """


if __name__ == "__main__":
    Run_2025_07().run_cmdline()
