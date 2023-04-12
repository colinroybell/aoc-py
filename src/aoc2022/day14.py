from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from utils.grid_2d import Grid2d


class Run_2022_14(DayBase):
    YEAR = "2022"
    DAY = "14"


def part_a(input, part_b=False):
    part_a = not part_b
    grid = Grid2d()
    min_x = 500
    max_x = 500
    min_y = 0
    max_y = 0

    for line in input_generator(input):
        words = line.split("->")
        last_coord = None
        for word in words:
            fields = word.split(",")
            coord = Vec2d(int(fields[0]), int(fields[1]))
            if last_coord:
                if last_coord.x == coord.x:
                    x = last_coord.x
                    ys = [last_coord.y, coord.y]
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, min(ys))
                    max_y = max(max_y, max(ys))
                    for y in range(min(ys), max(ys) + 1):
                        grid.set(Vec2d(x, y), "#")
                elif last_coord.y == coord.y:
                    y = last_coord.y
                    xs = [last_coord.x, coord.x]
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)
                    min_x = min(min_x, min(xs))
                    max_x = max(max_x, max(xs))
                    for x in range(min(xs), max(xs) + 1):
                        grid.set(Vec2d(x, y), "#")
                else:
                    assert 0

            last_coord = coord

    if part_b:
        for x in range(500 - (max_y + 5), 500 + (max_y + 5)):
            grid.set(Vec2d(x, max_y + 2), "#")

        min_x = min(min_x, 500 - (max_y + 5))
        max_x = max(max_x, 500 + (max_y + 5))
        max_y += 2

    # print(grid.to_string_as_characters(max_x+1,max_y+1,min_x,min_y))
    count = 0
    done = False
    while not done:
        pos = Vec2d(500, 0)
        placed = False
        while pos.y < max_y:
            candidates = [pos + Vec2d(0, 1), pos + Vec2d(-1, 1), pos + Vec2d(1, 1)]
            moved = False
            for candidate in candidates:
                if not grid.get(candidate):
                    # print("dropped to {}".format(candidate))
                    pos = candidate
                    moved = True
                    break
            if not moved:
                grid.set(pos, "o")
                count += 1
                placed = True
                # print(count)
                # print(grid.to_string_as_characters(max_x+1,max_y+1,min_x,min_y))
                break
        if part_a and not placed or part_b and pos == Vec2d(500, 0):
            done = True
    return count


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2022_14().run_cmdline()
