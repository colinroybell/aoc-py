from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2023_17(DayBase):
    YEAR = "2023"
    DAY = "17"


class State:
    seen = set()

    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir

    def init_class():
        State.seen = set()

    def __lt__(self, other):
        return self.pos < other.pos or (self.pos == other.pos and self.dir < other.dir)

    def __repr__(self):
        return "{} {}".format(self.pos, self.dir)

    def iterable(self):
        return (self.pos.tuple(), self.dir)

    def mark_processed(self):
        State.seen.add(self.iterable())

    def already_processed(self):
        # print('trying',self.iterable())
        return self.iterable() in State.seen


def part_a(input, part_b=False):
    grid = Grid2d()
    (width, height) = grid.read_from_file(input)
    grid_seen = Grid2d()
    to_process = PriorityQueue()
    if part_b:
        search_min = 4
        search_max = 10
    else:
        search_min = 1
        search_max = 3

    # NOTE: usual up/down issue
    state0 = State(Vec2d(width - 1, height - 1), "<")
    state1 = State(Vec2d(width - 1, height - 1), "v")
    to_process.put((0, state0))
    to_process.put((0, state1))
    State.init_class()

    while not to_process.empty():
        (cost, state) = to_process.get()
        # print("trying")
        if state.already_processed():
            continue
        print("Starting at {}, {}".format(cost, state))
        state.mark_processed()
        if state.pos == Vec2d(0, 0):
            break
        pos = state.pos
        v = grid.get(pos)
        if state.dir in "<>":
            new_dirs = "v^"
        else:
            new_dirs = "<>"
        for moves in range(1, search_max + 1):
            cost += v
            pos = pos.move(state.dir)
            v = grid.get(pos)
            # print(pos, v, cost,new_dirs)
            if v == None:
                break
            if moves >= search_min:
                for new_dir in new_dirs:
                    new_state = State(pos, new_dir)
                    # print(new_state)
                    if not new_state.already_processed():
                        # print('adding')
                        to_process.put((cost, new_state))

    return cost


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_17().run_cmdline()
