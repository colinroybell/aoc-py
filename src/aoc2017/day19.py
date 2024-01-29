from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_19(DayBase):
    YEAR = "2017"
    DAY = "19"


def part_a(input, part_b=False):
    part_a = not part_b
    grid = []
    for line in input_generator(input):
        grid.append(line)

    def getItem(pos):
        nonlocal grid
        (x, y) = pos
        print("trying: {}".format(pos))
        if y < 0 or y >= len(grid):
            return " "
        gridLine = grid[y]
        if x < 0 or x >= len(gridLine):
            return " "
        return gridLine[x]

    def advance(pos, dir_):
        return (pos[0] + dir_[0], pos[1] + dir_[1])

    def left(dir_):
        return (dir_[1], -dir_[0])

    def right(dir_):
        return (-dir_[1], dir_[0])

    for i in range(len(grid[0])):
        if getItem((i, 0)) != " ":
            pos = (i, 0)

    dir_ = (0, 1)
    output = ""
    steps = 1
    while True:
        print("At {}".format(pos, dir_))
        posS = advance(pos, dir_)
        itemS = getItem(posS)
        posL = advance(pos, left(dir_))
        itemL = getItem(posL)
        posR = advance(pos, right(dir_))
        itemR = getItem(posR)
        if itemS != " ":
            item = itemS
            pos = posS
        elif itemL != " ":
            item = itemL
            dir_ = left(dir_)
            pos = posL
        elif itemR != " ":
            item = itemR
            dir_ = right(dir_)
            pos = posR
        else:
            break

        steps += 1
        if ord(item) > 64 and ord(item) <= 90:
            output += item
            print("Found {}".format(item))
    if part_a:
        return output
    else:
        return steps


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_19().run_cmdline()
