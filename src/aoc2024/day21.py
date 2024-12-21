from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2024_21(DayBase):
    YEAR = "2024"
    DAY = "21"


def compute_transitions(source):
    output = {}
    grid = Grid2d()
    lines = source.split("/")
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != ".":
                grid.set(Vec2d(x, y), c)

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != ".":
                output[c] = []
                v = Vec2d(x, y)
                for d in "<>^v":
                    a = v.move_y_flipped(d)
                    a_c = grid.get(a)
                    if a_c:
                        output[c].append((d, a_c))
    return output


class State:
    def __init__(self, current, route, pressed):
        self.current = current
        self.pressed = pressed
        self.route = route

    def __repr__(self):
        return "{} {}".format(self.current, self.route, self.pressed)

    def __lt__(self, other):
        return 0


def compute_scores(transitions, buttons, scores):
    output = {}
    if scores == None:
        for b_from in buttons:
            output[b_from] = {}
            for b_to in buttons:
                output[b_from][b_to] = 1
    else:
        for b in buttons:
            output[b] = {}
            found = set()
            start_state = State(b, "", False)
            state_queue = PriorityQueue()
            state_queue.put((0, start_state))
            while not state_queue.empty():
                (t, state) = state_queue.get()
                loc = state.current
                route = state.route
                pressed = state.pressed
                if route == "":
                    last = "A"
                else:
                    last = route[-1]
                if (loc, pressed, last) in found:
                    continue
                found.add((loc, pressed, last))
                if pressed:
                    output[b][loc] = t
                    continue

                for (dir, dest) in transitions[loc]:
                    new_t = t + scores[last][dir]
                    new_state = State(dest, route + dir, False)
                    state_queue.put((new_t, new_state))
                new_t = t + scores[last]["A"]
                new_state = State(loc, route + "A", True)
                state_queue.put((new_t, new_state))
    return output


def part_a(input, keypads=4):
    grid0_source = "789/456/123/.0A"
    grid1_source = ".^A/<v>"
    t0 = compute_transitions(grid0_source)
    t1 = compute_transitions(grid1_source)

    scores = None
    for level in range(keypads - 1, 0, -1):
        buttons = "<>^vA"
        scores = compute_scores(t1, buttons, scores)
    buttons = "0123456789A"
    scores = compute_scores(t0, buttons, scores)

    total = 0
    for line in input_generator(input):
        val = int(line[0:3])
        line = "A" + line
        score = 0
        for i in range(len(line) - 1):
            c0 = line[i]
            c1 = line[i + 1]
            score += scores[c0][c1]
        total += val * score
    return total


def part_b(input):
    return part_a(input, keypads=27)


if __name__ == "__main__":
    Run_2024_21().run_cmdline()
