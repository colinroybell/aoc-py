from utils.day_base import DayBase
from utils.data_input import input_generator
from queue import PriorityQueue
from collections import namedtuple


class Run_2025_13(DayBase):
    YEAR = "2025"
    DAY = "13"
    PREFIX = "codyssi"


PART = None


class State:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "{}".format(self.current)

    def __lt__(self, other):
        return 0


Transition = namedtuple("Transition", ["state", "time"])


def breadth_first_search(transitions, first_state):
    times = {}
    start_state = State(first_state)
    state_queue = PriorityQueue()
    state_queue.put((0, start_state))
    while not state_queue.empty():
        (t, s) = state_queue.get()
        state = s.current
        if state in times:
            continue
        times[state] = t
        for tr in transitions[state]:
            other_state = tr.state
            other_time = t + tr.time
            if other_state not in times:
                new_state = State(other_state)
                state_queue.put((other_time, new_state))
    return times


def depth_first_search(transitions, time, target, visited, exclude):
    best = 0
    if not visited:
        current = target
    else:
        current = visited[-1]
        if current == target:
            return time

    for tr in transitions[current]:
        new_state = tr.state
        if new_state in visited or new_state in exclude:
            continue
        score = depth_first_search(
            transitions, time + tr.time, target, visited + [new_state], exclude
        )
        best = max(best, score)
    return best


def part_1(input):
    states = set()
    transitions = {}
    for line in input_generator(input):
        fields = line.split()
        s0 = fields[0]
        s1 = fields[2]
        if PART == 1:
            t = 1
        else:
            t = int(fields[4])
        states.add(s0)
        states.add(s1)
        if s0 not in transitions:
            transitions[s0] = []
        if s1 not in transitions:
            transitions[s1] = []
        transitions[s0].append(Transition(state=s1, time=t))

    if PART < 3:
        times = breadth_first_search(transitions, "STT")

        top3 = sorted(times.items(), key=lambda x: x[1], reverse=True)[:3]
        return top3[0][1] * top3[1][1] * top3[2][1]
    else:
        # Depth first search from all points trying to find a cycle. But exclude starting
        # point from subsequent searches as any cycle going through them would already have
        # been found.
        best = 0
        exclude = []
        for s in states:
            score = depth_first_search(transitions, 0, s, [], exclude)
            best = max(best, score)
            exclude += [s]
        return best


def part_2(input):
    return part_1(input)


def part_3(input):
    return part_1(input)


if __name__ == "__main__":
    Run_2025_13().run_cmdline()
