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


def breadth_first_search(states, transitions, first_state):
    times = {}
    start_state = State(first_state)
    state_queue = PriorityQueue()
    state_queue.put((0, start_state))
    while not state_queue.empty():
        (t, s) = state_queue.get()
        state = s.current
        if state in times:
            continue
        for tr in transitions[state]:
            other_state = tr.state
            other_time = t + tr.time
            if other_state not in times:
                new_state = State(other_state)
                state_queue.put((other_time, new_state))
    return times


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
        times = breadth_first_search(states, transitions, "STT")

        top3 = sorted(times.items(), key=lambda x: x[1], reverse=True)[:3]
        return top3[0][1] * top3[1][1] * top3[2][1]
    else:
        best = 0
        for s in states:
            times = breadth_first_search(states, transitions, s)
            if s in times:
                print(s, times[s])
            if s in times and times[s] > best:
                best = times[s]
        return best


def part_2(input):
    return part_1(input)


def part_3(input):
    return part_1(input)


if __name__ == "__main__":
    Run_2025_13().run_cmdline()
