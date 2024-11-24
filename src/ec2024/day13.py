from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2024_13(DayBase):
    YEAR = "2024"
    DAY = "13"
    PREFIX = "ec"


class State:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "{}".format(self.current)

    def __lt__(self, other):
        return 0


def height_diff(a, b):
    if a == "E":
        a = 0
    else:
        a = int(a)
    if b == "S":
        b = 0
    else:
        b = int(b)
    return min((a - b) % 10, (b - a) % 10)


# Do everything backwards then we have one start point


def part_1(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    for x in range(width):
        for y in range(height):
            if grid.get(Vec2d(x, y)) == "E":
                start = Vec2d(x, y)

    found = {}
    start_state = State(start)
    state_queue = PriorityQueue()
    state_queue.put((0, start_state))
    while not state_queue.empty():
        x = state_queue.get()
        (t, state) = x
        pos = state.current
        if pos in found:
            continue
        found[pos] = t
        # print("time {} state location {}".format(t, pos))
        pos_height = grid.get(pos)
        if pos_height == "S":
            return t
        vecs = pos.get_adjacent_orthogonal()
        for v in vecs:
            v_height = grid.get(v)
            if v not in found and v_height and v_height != "#":
                new_t = t + height_diff(grid.get(pos), grid.get(v)) + 1
                new_state = State(v)
                state_queue.put((new_t, new_state))


def part_2(input):
    return part_1(input)


def part_3(input):
    return part_1(input)


if __name__ == "__main__":
    Run_2024_13().run_cmdline()
