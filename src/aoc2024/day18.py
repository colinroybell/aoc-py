from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2024_18(DayBase):
    YEAR = "2024"
    DAY = "18"


class State:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "{} {}".format(self.current)

    def __lt__(self, other):
        return 0


def part_a(input, size=70, count=1024):
    grid = Grid2d()
    n = 0
    for line in input_generator(input):
        coords = [int(n) for n in line.split(",")]
        grid.set(Vec2d(coords[0], coords[1]), "#")
        n += 1
        if n == count:
            break

    start = Vec2d(size, size)

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
        if pos.x == 0 and pos.y == 0:
            return t
        for a in pos.get_adjacent_orthogonal():
            if 0 <= a.x <= size and 0 <= a.y <= size and grid.get(a) != "#":
                new_state = State(a)
                state_queue.put((t + 1, new_state))
    return None


def part_b(input, size=70):
    total = 0
    lines = []
    for line in input_generator(input):
        total += 1
        lines.append(line)

    start = 0
    end = total

    while end - start > 1:
        mid = (start + end) // 2
        res = part_a(input, size, mid)
        print(start, end, mid, res)
        if part_a(input, size, mid):
            start = mid
        else:
            end = mid
    return lines[mid]


if __name__ == "__main__":
    Run_2024_18().run_cmdline()
