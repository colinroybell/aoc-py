from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
import re


class Run_2022_22(DayBase):
    YEAR = "2022"
    DAY = "22"


def dir_to_index(dir):
    return ">v<^".index(dir)


def index_to_dir(index):
    return ">v<^"[index]


def rotateR(dir):
    return index_to_dir((dir_to_index(dir) + 1) % 4)


def rotateL(dir):
    return index_to_dir((dir_to_index(dir) - 1) % 4)


def flip(dir):
    return index_to_dir((dir_to_index(dir) + 2) % 4)


def part_a(input, part_b=False):
    part_a = not part_b
    grid = Grid2d()
    in_grid = True
    grid_lines = []
    for line in input_generator(input):
        if line:
            if in_grid:
                grid_lines.append(line)
            else:
                commands = line
        else:
            in_grid = False

    (width, height) = grid.read_from_file_strings(grid_lines)
    adj = {}
    if part_a:
        start_y = 0
        for y in range(height):
            first_square = None
            last_square = None
            for x in range(width):
                # print('-',grid.get(Vec2d(x,y)),'-')
                # Fix up parsing
                if grid.get(Vec2d(x, y)) == None:
                    grid.set(Vec2d(x, y), " ")
                if grid.get(Vec2d(x, y)) != " ":
                    if first_square == None:
                        first_square = x
                        if y == 0:
                            start_x = x
                    last_square = x
            adj[(last_square, y, ">")] = (first_square, y, ">")
            adj[(first_square, y, "<")] = (last_square, y, "<")
            print(y, first_square, last_square)
        for x in range(width):
            first_square = None
            last_square = None
            for y in range(height):
                if grid.get(Vec2d(x, y)) != " ":
                    if first_square == None:
                        first_square = y
                    last_square = y
            adj[(x, last_square, "v")] = (x, first_square, "v")
            adj[(x, first_square, "^")] = (x, last_square, "^")
            print(x, first_square, last_square)

    else:

        def add_edge(adj, length, pos0, dir0, dir_off0, pos1, dir1, dir_off1):
            dir_on0 = flip(dir_off0)
            dir_on1 = flip(dir_off1)
            for i in range(length):
                adj[(pos0.x, pos0.y, dir_off0)] = (pos1.x, pos1.y, dir_on1)
                adj[(pos1.x, pos1.y, dir_off1)] = (pos0.x, pos0.y, dir_on0)
                pos0 = pos0.move_y_flipped(dir0)
                pos1 = pos1.move_y_flipped(dir1)

        # Do this by hand!
        if width == 16:
            # 13
            add_edge(adj, 4, Vec2d(8, 3), "^", "<", Vec2d(7, 4), "<", "^")
            # 12
            add_edge(adj, 4, Vec2d(8, 0), ">", "^", Vec2d(0, 4), ">", "^")
            # 16
            add_edge(adj, 4, Vec2d(11, 0), "v", ">", Vec2d(15, 11), "^", ">")
            # 46
            add_edge(adj, 4, Vec2d(11, 4), "v", ">", Vec2d(15, 8), "<", "^")
            # 62
            add_edge(adj, 4, Vec2d(15, 11), "<", "v", Vec2d(0, 4), "v", "<")
            # 52
            add_edge(adj, 4, Vec2d(11, 11), "<", "v", Vec2d(0, 7), ">", "v")
            # 53
            add_edge(adj, 4, Vec2d(11, 8), "^", "<", Vec2d(4, 7), ">", "v")
            start_x = 8
            start_y = 0
            print(adj)
        elif width == 150:
            # 26
            add_edge(adj, 50, Vec2d(100, 0), ">", "^", Vec2d(0, 199), ">", "v")
            # 25
            add_edge(adj, 50, Vec2d(149, 0), "v", ">", Vec2d(99, 149), "^", ">")
            # 23
            add_edge(adj, 50, Vec2d(149, 49), "<", "v", Vec2d(99, 99), "^", ">")
            # 56
            add_edge(adj, 50, Vec2d(99, 149), "<", "v", Vec2d(49, 199), "^", ">")
            # 61
            add_edge(adj, 50, Vec2d(0, 199), "^", "<", Vec2d(99, 0), "<", "^")
            # 41
            add_edge(adj, 50, Vec2d(0, 149), "^", "<", Vec2d(50, 0), "v", "<")
            # 43
            add_edge(adj, 50, Vec2d(0, 100), ">", "^", Vec2d(50, 50), "v", "<")
            start_x = 50
            start_y = 0

    pos = Vec2d(start_x, start_y)
    dir = ">"
    number_next = True
    number_re = re.compile(r"(\d+)(.*)")

    while commands:
        print(pos, dir, commands, number_next)
        if number_next:
            m = number_re.match(commands)
            n = int(m.group(1))
            commands = m.group(2)
            for _ in range(n):
                try:
                    result = adj[(pos.x, pos.y, dir)]
                    adv = Vec2d.from_tuple(result[0:2])
                    new_dir = result[2]
                    print("wrap to ", adv, grid.get(adv))
                except:
                    adv = pos.move_y_flipped(dir)
                    new_dir = dir
                    print("adv to ", adv, grid.get(adv))
                assert grid.get(adv) != " "
                if grid.get(adv) == "#":
                    break
                else:
                    pos = adv
                    dir = new_dir
        else:
            rotate = commands[0]
            commands = commands[1:]
            if rotate == "R":
                dir = rotateR(dir)
            else:
                dir = rotateL(dir)

        number_next = not number_next

    print(pos, dir)
    return 4 * (pos.x + 1) + 1000 * (pos.y + 1) + dir_to_index(dir)


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2022_22().run_cmdline()
