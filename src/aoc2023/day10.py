from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2023_10(DayBase):
    YEAR = "2023"
    DAY = "10"


def part_a(input, part_b=False):
    part_a = not part_b
    grid = Grid2d()
    grid2 = Grid2d()

    (width, height) = grid.read_from_file_strings(input)

    found = False
    for x in range(width):
        for y in range(height):
            if grid.get(Vec2d(x, y)) == "S":
                found = True
                start_x = x
                start_y = y
                break
        if found:
            break

    # find first direction.
    # Note: we have y positive up assumed in moves in vec2d, but y positive down assumed in grid2d.
    # so flip U/D here.

    if grid.get(Vec2d(start_x + 1, start_y)) in "-J7":
        move = "R"
    elif grid.get(Vec2d(start_x, start_y + 1)) in "|LJ":
        move = "U"
    else:
        assert grid.get(Vec2d(start_x - 1, start_y)) in "-LF"
        move = "L"

    first_move = move

    pos = Vec2d(start_x, start_y)
    next_pos = pos.move(move)
    count = 0
    prev_char = "S"

    while grid.get(next_pos) != "S":

        next_char = grid.get(next_pos)
        grid2.set(next_pos, next_char)
        # print(count,pos,move,next_pos,next_char)
        if move == "R":
            if next_char == "-":
                move = "R"
            elif next_char == "J":
                move = "D"
            else:
                assert next_char == "7"
                move = "U"
        elif move == "U":
            if next_char == "|":
                move = "U"
            elif next_char == "L":
                move = "R"
            else:
                assert next_char == "J"
                move = "L"
        elif move == "L":
            if next_char == "-":
                move = "L"
            elif next_char == "F":
                move = "U"
            else:
                assert next_char == "L"
                move = "D"
        elif move == "D":
            if next_char == "|":
                move = "D"
            elif next_char == "7":
                move = "L"
            else:
                assert next_char == "F"
                move = "R"

        pos = next_pos
        next_pos = pos.move(move)
        count += 1
    if part_a:
        return (count + 1) // 2
    else:
        # work out what's under the S
        print(first_move, move)
        if first_move == "R":
            if move == "R":
                char = "-"
            elif move == "U":
                char = "L"
            else:
                assert move == "D"
                char = "F"
        elif first_move == "U":
            if move == "D":
                char = "|"
            elif move == "L":
                char = "F"
            else:
                assert move == "R"
                char = "7"
        else:
            assert first_move == "L"
            if move == "L":
                char = "-"
            elif move == "D":
                char = "7"
            else:
                assert move == "U"
                char = "J"
        print("Setting", next_pos, "to", char)
        grid2.set(next_pos, char)

        total = 0
        print("run")
        # Convention is that we are looking below the pipe
        for y in range(height):
            inside = False
            for x in range(width):
                char2 = grid2.get(Vec2d(x, y))
                if char2 and char2 in "F7|":
                    inside = not inside
                if not char2 and inside:
                    print("in", x, y)
                    total += 1

        return total


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_10().run_cmdline()
