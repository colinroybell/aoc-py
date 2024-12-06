from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_06(DayBase):
    YEAR = "2024"
    DAY = "06"


def part_a(input, part_b=False):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    dirs = "^>v<"
    guard = None
    found = set()

    for y in range(height):
        for x in range(width):
            pos = Vec2d(x, y)
            if grid.get(pos) == "^":
                guard = pos
    assert guard
    start = guard
    dir = 0
    while grid.get(guard):
        found.add(guard)
        new_guard = guard.move_y_flipped(dirs[dir])
        if grid.get(new_guard) == "#":
            dir = (dir + 1) % 4
        else:
            guard = new_guard
    if not part_b:
        return len(found)

    count = 0
    rounds = 0
    for pos in found:
        rounds += 1
        print(pos, rounds, count)
        if grid.get(pos) != ".":
            continue
        grid.set(pos, "#")
        guard = start
        found2 = set()
        dir = 0

        while grid.get(guard):
            item = (guard, dir)
            if item in found2:
                count += 1
                break
            found2.add(item)

            new_guard = guard.move_y_flipped(dirs[dir])
            if grid.get(new_guard) == "#":
                dir = (dir + 1) % 4
            else:
                guard = new_guard
        grid.set(pos, ".")
    return count


def part_b(input):
    return part_a(input, part_b=True)
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    dirs = "^>v<"
    guard = None
    found = set()

    for y in range(height):
        for x in range(width):
            pos = Vec2d(x, y)
            if grid.get(pos) == "^":
                guard = pos
    assert guard

    start = guard
    count = 0

    for y in range(height):
        for x in range(width):
            pos = Vec2d(x, y)
            if grid.get(pos) != ".":
                continue
            grid.set(pos, "#")
            guard = start
            found = set()
            dir = 0

            while grid.get(guard):
                item = (guard, dir)
                if item in found:
                    count += 1
                    break
                found.add(item)

                new_guard = guard.move_y_flipped(dirs[dir])
                if grid.get(new_guard) == "#":
                    dir = (dir + 1) % 4
                else:
                    guard = new_guard
            grid.set(pos, ".")
    return count


if __name__ == "__main__":
    Run_2024_06().run_cmdline()
