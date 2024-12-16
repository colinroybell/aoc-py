from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_15(DayBase):
    YEAR = "2024"
    DAY = "15"


def can_advance(grid, pos, dir):
    a = pos.move_y_flipped(dir)
    c = grid.get(a)
    move = False
    if c == ".":
        move = True
    elif c == "#":
        move = False
    else:
        _, move = can_advance(grid, a, dir)
    if move:
        print("move", grid.get(pos), dir, "to", a)
        grid.set(a, grid.get(pos))
        grid.set(pos, ".")
        return a, True
    else:
        return pos, False


def can_advance_iterative(grid, pos, dir):
    done = set()
    to_blank = []
    to_set = []
    to_consider = [pos]
    while to_consider:
        p = to_consider.pop(0)
        if p in done:
            continue
        done.add(p)
        a = p.move_y_flipped(dir)
        c = grid.get(a)
        if c == "#":
            return pos, False
        if c != ".":
            to_consider.append(a)
        if c == "[":
            to_consider.append(a.move(">"))
        if c == "]":
            to_consider.append(a.move("<"))
        to_blank.append(p)
        to_set.append((a, grid.get(p)))
    print(to_blank)
    print(to_set)
    for p in to_blank:
        grid.set(p, ".")
    for (p, v) in to_set:
        grid.set(p, v)
    return pos.move_y_flipped(dir), True


def part_a(input):
    grid = Grid2d()
    generator = input_generator(input)
    width, height = grid.read_from_file_strings_generator(generator, stop_at_blank=True)
    for y in range(height):
        for x in range(width):
            v = Vec2d(x, y)
            if grid.get(v) == "@":
                guard = v

    for line in generator:
        for dir in line:
            print("dir", dir)
            guard, _ = can_advance_iterative(grid, guard, dir)

    total = 0
    for y in range(height):
        for x in range(width):
            if grid.get(Vec2d(x, y)) == "O":  #
                total += y * 100 + x
    return total


def part_b(input):
    grid = Grid2d()
    grid_assemble = True

    y = 0
    for line in input_generator(input):
        if grid_assemble:
            if line == "":
                grid_assemble = False
                width = x
                height = y
            else:
                x = 0
                for c in line:
                    p0 = Vec2d(x, y)
                    p1 = Vec2d(x + 1, y)
                    if c == "#":
                        grid.set(p0, "#")
                        grid.set(p1, "#")
                    elif c == "O":
                        grid.set(p0, "[")
                        grid.set(p1, "]")
                    elif c == ".":
                        grid.set(p0, ".")
                        grid.set(p1, ".")
                    else:
                        grid.set(p0, "@")
                        grid.set(p1, ".")
                        guard = p0
                    x += 2
                y += 1

        else:
            for dir in line:
                print("dir", dir)
                guard, _ = can_advance_iterative(grid, guard, dir)

    total = 0
    for y in range(height):
        for x in range(width):
            if grid.get(Vec2d(x, y)) == "[":
                total += y * 100 + x
    return total


if __name__ == "__main__":
    Run_2024_15().run_cmdline()
