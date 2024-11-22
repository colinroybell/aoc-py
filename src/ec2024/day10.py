from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_10(DayBase):
    YEAR = "2024"
    DAY = "10"
    PREFIX = "ec"


# TODO: Not working. Think likely issue is that we're doing a first round solve on second round which is then filling in a ? so we need to check for this case.

# Fixed first round so we only check correct spaces.
# Need to account for rule that everything is unique, which may address 42 18
# problem.


# horiz goes y,x; vert goes x,y so we group correctly.
def copy_temp(grid, x_offset, y_offset):
    centre = [[None for _ in range(4)] for _ in range(4)]
    horiz = [[None for _ in range(4)] for _ in range(4)]
    vert = [[None for _ in range(4)] for _ in range(4)]
    for j, y in enumerate(range(2, 6)):
        for i, x in enumerate(range(2, 6)):
            centre[i][j] = grid.get(Vec2d(x + x_offset, y + y_offset))
    for j, y in enumerate(range(2, 6)):
        for i, x in enumerate([0, 1, 6, 7]):
            horiz[j][i] = grid.get(Vec2d(x + x_offset, y + y_offset))
    for j, y in enumerate([0, 1, 6, 7]):
        for i, x in enumerate(range(2, 6)):
            vert[i][j] = grid.get(Vec2d(x + x_offset, y + y_offset))
    return (centre, horiz, vert)


def copy_back(grid, x_offset, y_offset, centre, horiz, vert):
    for j, y in enumerate(range(2, 6)):
        for i, x in enumerate(range(2, 6)):
            grid.set(Vec2d(x + x_offset, y + y_offset), centre[i][j])
    for j, y in enumerate(range(2, 6)):
        for i, x in enumerate([0, 1, 6, 7]):
            grid.set(Vec2d(x + x_offset, y + y_offset), horiz[j][i])
    for j, y in enumerate([0, 1, 6, 7]):
        for i, x in enumerate(range(2, 6)):
            grid.set(Vec2d(x + x_offset, y + y_offset), vert[i][j])


def check_duplicates(array):
    found = set()
    for i in range(0, 4):
        for j in range(0, 4):
            c = array[i][j]
            if c != "?":
                if c in found:
                    return False
                else:
                    found.add(array[i][j])
    return True


def find_unique_question_mark(array):
    pos = None
    for i in range(0, 4):
        if array[i] == "?":
            if pos:
                # duplicate
                return None
            else:
                pos = i
    return pos


def find_missing(array1, array2):
    # returns if array1 contains 4 symbols, array2 3 and a dot
    count = 0
    for c in array2:
        if c == ".":
            count += 1
    if count > 1:
        return "."

    for c in array1:
        if c not in array2:
            return c


def grid_solve(grid, x_offset, y_offset, part):
    (centre, horiz, vert) = copy_temp(grid, x_offset, y_offset)

    all_done = True
    for y in range(0, 4):
        for x in range(0, 4):
            if centre[x][y] == ".":
                for h in horiz[y]:
                    if h in vert[x] and h != "?":
                        centre[x][y] = h
                        # print("first",x,y,h)
                        break
                else:
                    all_done = False

    if all_done:
        copy_back(grid, x_offset, y_offset, centre, horiz, vert)
        return "DONE"

    if not check_duplicates(horiz) or not check_duplicates(vert):
        return "INSOLUBLE"

    all_done = True
    for y in range(0, 4):
        for x in range(0, 4):
            if centre[x][y] == ".":
                hq = find_unique_question_mark(horiz[y])
                vq = find_unique_question_mark(vert[x])
                if hq != None and vq == None:
                    vert_centre = [centre[x][j] for j in range(4)]
                    c = find_missing(vert[x], vert_centre)
                    if c != ".":
                        centre[x][y] = c
                        horiz[y][hq] = c
                    # print("hq",x,y,centre[x][y])
                elif vq != None and hq == None:
                    horiz_centre = [centre[i][y] for i in range(4)]
                    c = find_missing(horiz[y], horiz_centre)
                    if c != ".":
                        centre[x][y] = c
                        vert[x][vq] = c
                    # print("vq",x,y,centre[x][y])

                if centre[x][y] == ".":
                    all_done = False

    copy_back(grid, x_offset, y_offset, centre, horiz, vert)
    if all_done:

        return "DONE"
    else:
        # print(centre, horiz, vert)
        return "REPEAT"


def grid_score(grid, x_offset, y_offset):
    count = 0
    score = 0
    for y in range(2, 6):
        for x in range(2, 6):
            s = grid.get(Vec2d(x + x_offset, y + y_offset))
            print(x + x_offset, y + y_offset, s)
            value = ord(s) - 64
            if value < 1 or value > 26:
                # Not solved
                return 0
            count += 1
            score += count * value
    print("score", score)
    return score


def grid_word(grid, x_offset, y_offset):
    word = ""
    for y in range(2, 6):
        for x in range(2, 6):
            s = grid.get(Vec2d(x + x_offset, y + y_offset))
            word += s
    return word


def part_1(input, part=1):
    grid = Grid2d()
    size = 8
    (x_max, y_max) = grid.read_from_file_strings(input, stop_at_blank=False)
    print(x_max, y_max)
    word = ""
    score = 0
    for y_offset in range(0, y_max + 1, 9):
        for x_offset in range(0, x_max + 1, 9):
            grid_solve(grid, x_offset, y_offset, part)
            score += grid_score(grid, x_offset, y_offset)
            word += grid_word(grid, x_offset, y_offset)

    if part == 1:
        return word
    else:
        return score


def part_2(input):
    return part_1(input, 2)


def part_3(input):
    grid = Grid2d()
    size = 8
    (x_max, y_max) = grid.read_from_file_strings(input, stop_at_blank=False)
    new_round = True
    status = {}
    for y_offset in range(0, y_max - 6, 6):
        status[y_offset] = {}
        for x_offset in range(0, x_max - 6, 6):
            status[y_offset][x_offset] = "REPEAT"
    while new_round:
        new_round = False
        for y_offset in range(0, y_max - 6, 6):
            for x_offset in range(0, x_max - 6, 6):
                if status[y_offset][x_offset] == "REPEAT":
                    print("solve", x_offset, y_offset)
                    update = grid_solve(grid, x_offset, y_offset, 3)
                    print("update", update)
                    status[y_offset][x_offset] = update
                    if update == "REPEAT":
                        new_round = True

    score = 0
    for y_offset in range(0, y_max - 6, 6):
        for x_offset in range(0, x_max - 6, 6):
            if status[y_offset][x_offset] == "DONE":
                print("score", x_offset, y_offset)
                score += grid_score(grid, x_offset, y_offset)
    return score


if __name__ == "__main__":
    Run_2024_10().run_cmdline()
