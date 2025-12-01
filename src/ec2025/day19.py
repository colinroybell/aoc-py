from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_19(DayBase):
    YEAR = "2025"
    DAY = "19"
    PREFIX = "ec"


class Slit:
    def __init__(self, x, min_y, max_y):
        self.x = x
        self.min_y = min_y
        self.max_y = max_y

    def project(self, other):
        w = other.x - self.x
        max_y = self.max_y + w
        min_y = self.min_y - w

        new_max_y = min(max_y, other.max_y)
        if (new_max_y - other.x) % 2:
            new_max_y -= 1
        new_min_y = max(min_y, other.min_y)
        if (new_min_y - other.x) % 2:
            new_min_y += 1
        if new_min_y <= new_max_y:
            return Slit(other.x, new_min_y, new_max_y)
        else:
            return None


def part_1(input):
    x = 0
    min_y = 0
    max_y = 0
    current = Slit(0, 0, 0)
    for line in input_generator(input):
        (slit_x, slit_base, slit_size) = [int(n) for n in line.split(",")]
        slit_min = slit_base
        slit_max = slit_base + slit_size - 1
        other = Slit(slit_x, slit_min, slit_max)
        project = current.project(other)
        current = project
    return (current.x + current.min_y) // 2


def part_2(input):
    assert 0, "not implemented"


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2025_19().run_cmdline()
