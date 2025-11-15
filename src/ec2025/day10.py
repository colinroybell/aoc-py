from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from utils.grid_2d import Grid2d


class Run_2025_10(DayBase):
    YEAR = "2025"
    DAY = "10"
    PREFIX = "ec"


def part_1(input, steps=4):
    grid = Grid2d()
    width, height = grid.read_from_file_strings(input)

    moves = [
        Vec2d(2, 1),
        Vec2d(2, -1),
        Vec2d(1, 2),
        Vec2d(1, -2),
        Vec2d(-1, 2),
        Vec2d(-1, -2),
        Vec2d(-2, 1),
        Vec2d(-2, -1),
    ]

    found = False
    for x in range(width):
        for y in range(height):
            pos = Vec2d(x, y)
            if grid.get(pos) == "D":
                found = True
                break
        if found:
            break
    assert found

    queue = []
    queue.append((pos, 0))
    done = set()
    count = 0
    while queue:
        (p, s) = queue[0]
        queue = queue[1:]
        if p in done:
            continue
        done.add(p)
        c = grid.get(p)
        if not c:
            # off grid
            continue
        if c == "S":
            count += 1
        if s < steps:
            for m in moves:
                queue.append((p + m, s + 1))
    return count


def part_2(input, steps=20):
    grid = Grid2d()
    width, height = grid.read_from_file_strings(input)

    moves = [
        Vec2d(2, 1),
        Vec2d(2, -1),
        Vec2d(1, 2),
        Vec2d(1, -2),
        Vec2d(-1, 2),
        Vec2d(-1, -2),
        Vec2d(-2, 1),
        Vec2d(-2, -1),
    ]

    found = False
    for x in range(width):
        for y in range(height):
            pos = Vec2d(x, y)
            if grid.get(pos) == "D":
                found = True
                break
        if found:
            break
    assert found

    queue = []
    queue.append((pos, 0))
    done = set()
    sheep_done = set()
    count = 0
    while queue:
        (p, s) = queue[0]
        queue = queue[1:]
        if (p, s) in done:
            continue
        c = grid.get(p)
        if not c:
            # off grid
            continue
        done.add((p, s))
        if c != "#":
            for d in range(s - 1, s + 1):
                start_pos = p + Vec2d(0, -d)
                if grid.get(start_pos) == "S" and start_pos not in sheep_done:
                    count += 1
                    sheep_done.add(start_pos)
        if s < steps:
            for m in moves:
                queue.append((p + m, s + 1))
    return count


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2025_10().run_cmdline()
