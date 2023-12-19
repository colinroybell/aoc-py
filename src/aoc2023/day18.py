from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2023_18(DayBase):
    YEAR = "2023"
    DAY = "18"


def old_part_a(input):
    grid = Grid2d()
    pos = Vec2d(0, 0)
    initial_dir = None
    previous_dir = None
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for line in input_generator(input):
        (dir, count_string, _) = line.split()
        count = int(count_string)
        for c in range(count):
            if c == 0:
                if previous_dir:
                    grid.set(pos, previous_dir + dir)
                else:
                    initial_dir = dir
            else:
                grid.set(pos, dir)
            pos = pos.move(dir)
            min_x = min(min_x, pos.x)
            max_x = max(max_x, pos.x)
            min_y = min(min_y, pos.y)
            max_y = max(max_y, pos.y)
        previous_dir = dir
    assert pos == Vec2d(0, 0)
    grid.set(pos, dir + initial_dir)
    count = 0
    for y in range(min_y, max_y + 1):
        inside = False
        for x in range(min_x, max_x + 1):
            c = grid.get(Vec2d(x, y))
            # inside is down
            if c == "U" or c == "D" or c == "UR" or c == "UL" or c == "LD" or c == "RD":
                inside = not inside
            if c or inside:
                count += 1
            print(x, y, c, inside, count)
    return count


class Transition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

    def __lt__(self, other):
        print("cmp", self, other)
        return self.y < other.y or (self.y == other.y and self.x < other.x)


def new_transition(transitions, x, y, dir, previous_dir):
    if dir == "R":
        if previous_dir == "U":
            transitions.append(Transition(x, y))
        else:
            transitions.append(Transition(x, y))
    elif dir == "L":
        if previous_dir == "U":
            transitions.append(Transition(x, y))
        else:
            transitions.append(Transition(x, y))
    elif dir == "U":
        transitions.append(Transition(x, y))
    elif dir == "D":
        transitions.append(Transition(x, y))


def part_a(input, part_b=False):
    x = 0
    y = 0
    transitions = []
    previous_dir = None
    initial_dir = None
    interior_horiz = 0

    area_total = 0
    boundary_total = 0

    for line in input_generator(input):
        (dir, count_string, colour) = line.split()
        count = int(count_string)
        if part_b:
            print(colour[2:7])
            count = int(colour[2:7], 16)
            if colour[7] == "0":
                dir = "R"
            if colour[7] == "1":
                dir = "D"
            if colour[7] == "2":
                dir = "L"
            if colour[7] == "3":
                dir = "U"

        if previous_dir:
            new_transition(transitions, x, y, dir, previous_dir)
        else:
            initial_dir = dir
        if dir == "R":
            x += count
            area_total -= count * y
        if dir == "L":
            x -= count
            area_total += count * y
        if dir == "U":
            y -= count
            area_total -= count * x
        if dir == "D":
            y += count
            area_total += count * x
        boundary_total += count
        previous_dir = dir
        # print(transitions)
        print(x, y, area_total, boundary_total)
    print(area_total, boundary_total)
    # Work out area in triangles, then need to add 1 for 360 degree rotation, plus half a square per boundary
    return abs(area_total // 2) + boundary_total // 2 + 1

    print(x, y)
    assert x == 0 and y == 0
    new_transition(transitions, 0, 0, initial_dir, dir)

    transitions.sort()
    print(interior_horiz)
    count = 0  # interior_horiz

    def row_count_single(list):
        assert len(list) % 2 == 0

        count = 0
        list_pos = 0
        current_x = 0
        inside = False
        while list_pos < len(list):
            x = list[list_pos]
            if inside:
                count += x - current_x + 1
            inside = not inside
            current_x = x
            list_pos += 1
        print("rc", list, count)
        return count

    def row_count_double(list1, list2):
        assert len(list1) % 2 == 0
        assert len(list2) % 2 == 0
        count = 0
        list_pos1 = 0
        list_pos2 = 0
        current_x = 0
        inside1 = False
        inside2 = False
        while list_pos1 < len(list1) or list_pos2 < len(list2):
            if list_pos1 < len(list1):
                x1 = list1[list_pos1]
            else:
                x1 = None
            if list_pos2 < len(list2):
                x2 = list2[list_pos2]
            else:
                x2 = None
            if x2 == None or (x1 != None and x1 < x2):
                use1 = True
                x = x1
            else:
                use1 = False
                x = x2
            if inside1 or inside2:
                count += x - current_x
            print(x, current_x, count)
            current_x = x
            if use1:
                inside1 = not inside1
                list_pos1 += 1
            else:
                inside2 = not inside2
                list_pos2 += 1
            if not inside1 and not inside2:
                count += 1

        print("rcd", list1, list2, count)
        return count

    last_y = None
    list = []
    print(transitions)
    previous_list = []
    for t in transitions:
        x = t.x
        y = t.y
        print(x, y, last_y, list)
        if last_y != None and y != last_y:
            list.sort()
            count += row_count_double(list, previous_list)
            print(y, count)
            count += row_count_single(list) * (y - last_y - 1)
            print(y, count)
            previous_list = list.copy()
        last_y = y
        if x not in list:
            list.append(x)
        else:
            list.remove(x)
    count += row_count_single(previous_list)
    return count


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_18().run_cmdline()
