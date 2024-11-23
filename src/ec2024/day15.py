from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2024_15(DayBase):
    YEAR = "2024"
    DAY = "15"
    PREFIX = "ec"


class State:
    def __init__(self, current, herbs=set()):
        self.current = current
        self.herbs = herbs

    def __repr__(self):
        return "{} {}".format(self.current, self.herbs)

    def it(self):
        return self.current

    def __lt__(self, other):
        return 0


# TODO: correct approach is at each stage to do a full search and pick up any new herbs not in our list


def part_1(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)

    all_herbs = set()

    for x in range(width):
        if grid.get(Vec2d(x, 0)) == ".":
            start = Vec2d(x, 0)

    for x in range(width):
        for y in range(height):
            c = grid.get(Vec2d(x, y))
            if c not in [".", "#", "~"]:
                all_herbs.add(c)

    found = {}
    start_state = State(start)
    state_queue = PriorityQueue()
    state_queue.put((0, start_state))
    while not state_queue.empty():
        x = state_queue.get()
        (t, state) = x
        pos = state.current
        herbs = state.herbs

        cache_state = (pos.tuple(), frozenset(herbs))
        if cache_state in found:
            continue
        found[cache_state] = t
        print("time {} state location {} herbs = {}".format(t, pos, herbs))
        if pos == start and herbs == all_herbs:
            return t
        pos_height = grid.get(pos)
        new_herbs = herbs.copy()
        if pos_height not in [".", "#", "~"]:
            new_herbs.add(pos_height)
        vecs = pos.get_adjacent_orthogonal()
        for v in vecs:
            v_height = grid.get(v)
            if v_height and v_height not in ["#", "~"]:
                new_t = t + 1
                new_state = State(v, new_herbs)
                state_queue.put((new_t, new_state))


def part_2(input):
    return part_1(input)


def part_3(input):
    return part_1(input)


if __name__ == "__main__":
    Run_2024_15().run_cmdline()
