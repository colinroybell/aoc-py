from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2024_16(DayBase):
    YEAR = "2024"
    DAY = "16"


class State:
    def __init__(self, current, dir):
        self.current = current
        self.dir = dir

    def __repr__(self):
        return "{} {}".format(self.current, self.dir)

    def __lt__(self, other):
        return 0


def part_a(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    for x in range(width):
        for y in range(height):
            if grid.get(Vec2d(x, y)) == "S":
                start = Vec2d(x, y)

    found = {}
    start_state = State(start, ">")
    state_queue = PriorityQueue()
    state_queue.put((0, start_state))
    while not state_queue.empty():
        x = state_queue.get()
        (t, state) = x
        pos = state.current
        dir = state.dir
        if (pos, dir) in found:
            continue
        found[(pos, dir)] = t
        print("time {} state location {}".format(t, pos))
        c = grid.get(pos)
        if c == "E":
            return t
        a = pos.move(dir)
        if grid.get(a) != "#":
            new_state = State(a, dir)
            state_queue.put((t + 1, new_state))
        if dir in "<>":
            new_dirs = "^v"
        else:
            new_dirs = "<>"
        for d in new_dirs:
            new_state = State(pos, d)
            print("adding", new_state)
            state_queue.put((t + 1000, new_state))


def part_b(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    for x in range(width):
        for y in range(height):
            if grid.get(Vec2d(x, y)) == "S":
                start = Vec2d(x, y)

    found = {}
    start_state = State(start, ">")
    state_queue = PriorityQueue()
    state_queue.put((0, start_state))
    key = (start, ">")

    history = {}
    history_time = {}
    history[key] = set([start])
    history_time[key] = 0

    best_set = set()
    best_time = None
    while not state_queue.empty():
        x = state_queue.get()
        (t, state) = x
        pos = state.current
        dir = state.dir
        h = history[(state.current, state.dir)]
        if (pos, dir) in found:
            continue
        found[(pos, dir)] = t
        print("time {} state location {}".format(t, pos))
        c = grid.get(pos)
        if c == "E":
            print(h)
            return len(h)

        a = pos.move(dir)
        if grid.get(a) != "#":
            new_state = State(a, dir)
            state_queue.put((t + 1, new_state))
            key = (a, dir)
            if key not in history_time or t + 1 < history_time[key]:
                history_time[key] = t + 1
                history[key] = set()
            if t + 1 <= history_time[key]:
                history_time[key] = t + 1
                history[key].update(h)
                history[key].add(a)
        if dir in "<>":
            new_dirs = "^v"
        else:
            new_dirs = "<>"
        for d in new_dirs:
            new_state = State(pos, d)
            print("adding", new_state)
            state_queue.put((t + 1000, new_state))
            key = (pos, d)
            if key not in history_time or t + 1000 < history_time[key]:
                history_time[key] = t + 1000
                history[key] = set()
            if t + 1 <= history_time[key]:
                history_time[key] = t + 1000
                history[key].update(h)


if __name__ == "__main__":
    Run_2024_16().run_cmdline()
