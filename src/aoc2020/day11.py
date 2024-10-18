from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_11(DayBase):
    YEAR = "2020"
    DAY = "11"


def count_neighbours(grid, x, y, part):
    width = len(grid[0])
    height = len(grid)
    count = 0
    for xs in range(-1, 2):
        for ys in range(-1, 2):
            if xs != 0 or ys != 0:
                xt = x + xs
                yt = y + ys
                done = False
                while not done:
                    if xt < 0 or xt == width or yt < 0 or yt == height:
                        done = True
                    elif grid[yt][xt] == "#":
                        count += 1
                        done = True
                    elif grid[yt][xt] == "L":
                        done = True
                    else:
                        if part == "a":
                            done = True
                        else:
                            xt += xs
                            yt += ys
    return count


def update_grid(grid, part):
    width = len(grid[0])
    height = len(grid)

    empty_threshold = 4
    if part == "b":
        empty_threshold = 5

    new_grid = []
    change = False
    for y in range(0, height):
        row = ""
        for x in range(0, width):
            state = grid[y][x]
            new_state = state
            if state != ".":
                count = count_neighbours(grid, x, y, part)
                if state == "L" and count == 0:
                    new_state = "#"
                    change = True
                elif state == "#" and count >= empty_threshold:
                    new_state = "L"
                    change = True
            row += new_state
        new_grid.append(row)
    print(new_grid)
    return (new_grid, change)


def part_a(input):
    grid = []
    for line in input_generator(input):
        grid.append(line)

    change = True
    rounds = 0
    print(grid)
    while change:
        (grid, change) = update_grid(grid, "a")
        rounds += 1
    count = 0
    for line in grid:
        for c in line:
            if c == "#":
                count += 1
    return count


def part_b(input):
    grid = []
    for line in input_generator(input):
        grid.append(line)

    change = True
    rounds = 0
    while change:
        (grid, change) = update_grid(grid, "b")
        rounds += 1
    count = 0
    for line in grid:
        for c in line:
            if c == "#":
                count += 1
    return count


if __name__ == "__main__":
    Run_2020_11().run_cmdline()
