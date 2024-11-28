from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2024_18(DayBase):
    YEAR = "2024"
    DAY = "18"
    PREFIX = "ec"


class State:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "{}".format(self.current)

    def __lt__(self, other):
        return 0


# More or less a copy from day 13.
def part_1(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    starts = []
    for y in range(height):
        if grid.get(Vec2d(0, y)) == ".":
            starts.append(Vec2d(0, y))
        if grid.get(Vec2d(width - 1, y)) == ".":
            starts.append(Vec2d(width - 1, y))

    found = {}
    start_states = [State(start) for start in starts]
    state_queue = PriorityQueue()
    for state in start_states:
        state_queue.put((0, state))
    max_t = 0
    while not state_queue.empty():
        x = state_queue.get()
        (t, state) = x
        pos = state.current
        if pos in found:
            continue
        found[pos] = t
        # print("time {} state location {}".format(t, pos))
        pos_height = grid.get(pos)
        if pos_height == "P":
            max_t = t
        vecs = pos.get_adjacent_orthogonal()
        for v in vecs:
            v_height = grid.get(v)
            if v not in found and v_height and v_height != "#":
                new_t = t + 1
                new_state = State(v)
                state_queue.put((new_t, new_state))
    return max_t


def part_2(input):
    return part_1(input)


def part_3(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    starts = []
    for x in range(width):
        for y in range(height):
            v = Vec2d(x, y)
            if grid.get(v) == "#":
                continue
            count = 0
            for a in v.get_adjacent_orthogonal():
                if grid.get(a) != "#":
                    count += 1
            if count >= 3:
                starts.append(v)

    min_total = None
    for start in starts:
        print("Start at ", start)
        found = {}
        start_state = State(start)
        state_queue = PriorityQueue()
        state_queue.put((0, start_state))
        total = 0
        while not state_queue.empty():
            x = state_queue.get()
            (t, state) = x
            pos = state.current
            if pos in found:
                continue
            found[pos] = t
            # print("time {} state location {}".format(t, pos))
            pos_height = grid.get(pos)
            if pos_height == "P":
                # print("found {} at {}".format(pos,t))
                total += t
            vecs = pos.get_adjacent_orthogonal()
            for v in vecs:
                v_height = grid.get(v)
                if v not in found and v_height and v_height != "#":
                    new_t = t + 1
                    new_state = State(v)
                    state_queue.put((new_t, new_state))
        print("total", total)
        if min_total == None or total < min_total:
            min_total = total
    return min_total


if __name__ == "__main__":
    Run_2024_18().run_cmdline()
