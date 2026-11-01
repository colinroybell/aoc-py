from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from utils.grid_2d import Grid2d


class Run_2026_05(DayBase):
    YEAR = "2026"
    DAY = "05"
    PREFIX = "ec"


# TODO:
# * remove prints
# * reduce reloading of grid contents
# * part 2 setup loop is slow - we need to do a lot of tests against the new_land loop. (Is this a case for the update step too?)


def update_step(grid, width, height, new_land, part=1):
    print("new_land", new_land)
    next_new_land = []
    contenders = set()
    for loc in new_land:
        if part == 1:
            grid.set(loc, "#")
        elif part == 2:
            grid.set(loc, "=")
        else:
            grid.set(loc, "+")
        adj = loc.get_adjacent_with_diagonals()
        for a in adj:
            if a not in new_land:
                if (
                    part == 1
                    and (grid.get(a) == "0" or grid.get(a) == "1")
                    or (part == 2 or part == 3)
                    and grid.get(a) == "#"
                ):
                    contenders.add(a)
    # print(grid.to_string_as_characters(width, height))
    print("contenders", contenders)
    for loc in contenders:
        nb_count = 0
        sand_count = 0
        adj = loc.get_adjacent_with_diagonals()
        for a in adj:
            if (
                part == 1
                and (grid.get(a) == "#" or grid.get(a) == "1")
                or part == 2
                and grid.get(a) == "="
                or part == 3
                and grid.get(a) == "+"
            ):
                nb_count += 1
            if part == 3 and grid.get(a) == "=":
                sand_count += 1
        if (part < 3 and nb_count >= 5) or (
            part == 3 and nb_count >= 4 and sand_count == 0
        ):
            next_new_land.append(loc)
        print(f"test: {loc} nb {nb_count}")
    return next_new_land


def part_1(input, part=1):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)

    new_land = [Vec2d((width - 1) // 2, (height - 1) // 2)]
    count = 0
    while new_land:
        count += len(new_land)
        new_land = update_step(grid, width, height, new_land, part=1)
        print("count", count)
    if part == 1:
        return count
    print("Part 2")
    new_land = []
    for x in range(-1, width + 1):
        for y in range(-1, height + 1):
            loc = Vec2d(x, y)
            if grid.get(loc) != "#":
                adj = loc.get_adjacent_with_diagonals()
                for a in adj:
                    if a not in new_land and grid.get(a) == "#":
                        new_land.append(a)
    count = 0
    print(f"new land {new_land}")
    while new_land:
        count += len(new_land)
        new_land = update_step(grid, width, height, new_land, part=2)
        print("count", count)
    if part == 2:
        return count
    count = 0
    new_land = []
    for x in range(width):
        for y in range(height):
            loc = Vec2d(x, y)
            ok = True
            for delta_x in range(-2, +3):
                for delta_y in range(-2, +3):
                    loc_delta = Vec2d(x + delta_x, y + delta_y)
                    grid_delta = grid.get(loc_delta)
                    if abs(delta_x) + abs(delta_y) < 4 and not (
                        grid_delta == "#" or grid_delta == "@"
                    ):
                        ok = False
            if ok:
                new_land.append(loc)
    print(f"new land {new_land}")
    for _ in range(3):
        # We do three rounds to insert the initial phase and two more. We compute a third additional round
        # which we could shortcut
        count += len(new_land)
        new_land = update_step(grid, width, height, new_land, part=3)
        print("count", count)
    return count


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2026_05().run_cmdline()
