from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d


class Run_2022_24(DayBase):
    YEAR = "2022"
    DAY = "24"


def safe(p, time, horiz_b, vert_b, width, height):
    def safe_dir(pos, time, blizzard, modulo):
        for b in blizzard:
            p = (b[0] + time * b[1]) % modulo
            if p == pos:
                return False
        return True

    x = p.x
    y = p.y
    if not safe_dir(x, time, horiz_b[y], width):
        return False
    if not safe_dir(y, time, vert_b[x], height):
        return False
    return True


def trip(start, target, time, horiz_b, vert_b, width, height):
    positions = set()
    positions.add(start.tuple())
    while target.tuple() not in positions:
        new_positions = set()
        new_positions.add(start.tuple())
        print(time, positions)
        for p_tuple in positions:
            p = Vec2d.from_tuple(p_tuple)
            for dir in "<>^v.":
                new_p = p.move(dir)
                if new_p.x < 0 or new_p.x >= width or new_p.y < 0 or new_p.y >= height:
                    continue
                elif new_p.tuple() in new_positions:
                    continue
                elif safe(new_p, time + 1, horiz_b, vert_b, width, height):
                    new_positions.add(new_p.tuple())
        time += 1
        positions = new_positions
    return time + 1


def part_a(input, part_b=False):
    first_line = True
    horiz_b = []
    height = 0
    for line in input_generator(input):
        if first_line:
            width = len(line) - 2
            vert_b = [[] for x in range(width)]
            first_line = False
        elif line[0:2] == "##":
            pass
        else:
            row_b = []
            line = line[1:-1]
            for pos in range(len(line)):
                i = line[pos]
                if i == ">":
                    row_b.append((pos, 1))
                elif i == "<":
                    row_b.append((pos, -1))
                elif i == "v":
                    vert_b[pos].append((height, 1))
                elif i == "^":
                    vert_b[pos].append((height, -1))
            horiz_b.append(row_b)
            height += 1

    time = 0
    start_forward = Vec2d(0, -1)
    target_forward = Vec2d(width - 1, height - 1)
    start_reverse = Vec2d(width - 1, height)
    target_reverse = Vec2d(0, 0)
    time = trip(start_forward, target_forward, time, horiz_b, vert_b, width, height)
    if part_b:
        time = trip(start_reverse, target_reverse, time, horiz_b, vert_b, width, height)
        time = trip(start_forward, target_forward, time, horiz_b, vert_b, width, height)
    return time


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2022_24().run_cmdline()
