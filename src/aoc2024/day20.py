from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2024_20(DayBase):
    YEAR = "2024"
    DAY = "20"


class State:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "{} {}".format(self.current)

    def __lt__(self, other):
        return 0


def part_a(input, part_b=False):
    part_a = not part_b
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    for x in range(width):
        for y in range(height):
            if grid.get(Vec2d(x, y)) == "S":
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
        print("time {} state location {}".format(t, pos))
        c = grid.get(pos)
        if c == "E":
            break
        for a in pos.get_adjacent_orthogonal():
            if grid.get(a) != "#":
                new_state = State(a)
                state_queue.put((t + 1, new_state))
    if part_a:

        cheat_counts = [0 for _ in range(100)]
        total = 0
        for x in range(width):
            for y in range(height):
                pos = Vec2d(x, y)
                if grid.get(Vec2d(x, y)) == "#":
                    adj_scores = []
                    for a in pos.get_adjacent_orthogonal():
                        if a in found:
                            adj_scores.append(found[a])
                    if len(adj_scores) > 1:
                        diff = max(adj_scores) - min(adj_scores) - 2
                        if diff > 0 and diff < 100:
                            cheat_counts[diff] += 1
                        if diff >= 100:
                            total += 1
        for saved in range(1, 100):
            count = cheat_counts[saved]
            if count > 0:
                print("{} counts saving {} ps".format(count, saved))
        return total
    else:
        cheat_counts = [0 for _ in range(100)]
        total = 0
        for x in range(width):
            for y in range(height):
                pos = Vec2d(x, y)
                if pos in found:
                    this_score = found[pos]
                    for xx in range(-20, 21):
                        for yy in range(-20 + abs(xx), 21 - abs(xx)):
                            other = Vec2d(x + xx, y + yy)
                            diff = abs(xx) + abs(yy)
                            if other in found:
                                skip = found[other] - this_score - diff

                                if skip > 0 and skip < 100:
                                    cheat_counts[skip] += 1
                                if skip >= 100:
                                    total += 1
        for saved in range(50, 100):
            count = cheat_counts[saved]
            if count > 0:
                print("{} counts saving {} ps".format(count, saved))
        return total


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2024_20().run_cmdline()
