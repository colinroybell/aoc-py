from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_19(DayBase):
    YEAR = "2025"
    DAY = "19"
    PREFIX = "ec"


def part_1(input):
    x = 0
    min_y = 0
    max_y = 0
    for line in input_generator(input):
        (slit_x, slit_base, slit_size) = [int(n) for n in line.split(",")]
        w = slit_x - x
        x = slit_x
        slit_min = slit_base
        slit_max = slit_base + slit_size - 1
        new_max_y = min(max_y + w, slit_max)
        new_min_y = max(min_y - w, slit_min)
        # Allow for the fact we can only go diagonally
        if (new_max_y - x) % 2:
            new_max_y -= 1
        if (new_min_y - x) % 2:
            new_min_y += 1

        assert new_max_y >= min_y - w
        assert new_min_y <= max_y + w

        min_y = new_min_y
        max_y = new_max_y
    return (x + min_y) // 2


def part_2(input):
    assert 0, "not implemented"


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2025_19().run_cmdline()
