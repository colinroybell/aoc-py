from utils.day_base import DayBase
from utils.data_input import input_generator
import re

# TODO: optimise by combining tunnels


class Run_2022_16(DayBase):
    YEAR = "2022"
    DAY = "16"


class State:
    def __init__(self, time, pos, last_pos, opened, delta, score):
        self.time = time
        self.pos = pos
        self.opened = opened
        self.delta = delta
        self.score = score
        self.last_pos = last_pos

    def copy(self):
        return State(
            self.time,
            self.pos,
            self.last_pos,
            self.opened.copy(),
            self.delta,
            self.score,
        )

    def iterable(self):
        return (self.time, self.pos, tuple(self.opened), self.score)

    def __repr__(self):
        return "time {} pos {} last {} opened {} delta {} score {}".format(
            self.time, self.pos, self.last_pos, self.opened, self.delta, self.score
        )

    def best_possible(self, node, end_time, max_flow):
        time_left = end_time - self.time
        best_possible = self.score + time_left * self.delta
        if self.pos in self.opened or node.flow_rate == 0:
            time_left -= 1
        if time_left % 2 == 0:
            best_possible += (time_left // 2) * (time_left // 2) * max_flow
        else:
            best_possible += (time_left // 2) * (time_left // 2 + 1) * max_flow
        print(best_possible, time_left, max_flow)
        return best_possible

    def advance(self, nodes, end_time, best_found, max_flow):
        node = nodes[self.pos]
        best_possible = self.best_possible(node, end_time, max_flow)
        if best_possible <= best_found:
            print("Cull: {} vs {}".format(best_possible, best_found))
            return []
        advances = []
        self.time += 1
        self.score += self.delta

        for t in node.tunnels:
            if True or t != self.last_pos:
                new = self.copy()
                new.last_pos = new.pos
                new.pos = t
                advances.append(new)
        # Prioritise opening one
        if self.pos not in self.opened and node.flow_rate > 0:
            new = self.copy()
            new.opened.add(self.pos)
            new.delta += node.flow_rate
            new.last_pos = None
            advances.append(new)

        return advances


class Node:
    def init_class():
        Node.match_re = re.compile(r"Valve (\w+).+?(\d+).+?valves? (.+)")

    def __init__(self, string):
        m = Node.match_re.match(string)
        assert m
        self.name = m.group(1)
        self.flow_rate = int(m.group(2))
        self.tunnels = m.group(3).split(", ")


def part_a(input):
    nodes = {}
    Node.init_class()
    max_flow = 0
    for line in input_generator(input):
        node = Node(line)
        nodes[node.name] = node
        max_flow = max(max_flow, node.flow_rate)

    state_queue = []
    state_queue.append(State(0, "AA", None, set(), 0, 0))
    best_found = 0
    end_time = 30
    count = 0
    states_considered = set()

    while state_queue:
        state = state_queue.pop()
        print("Considering ", state)
        it = state.iterable()
        if it in states_considered:
            continue
        else:
            states_considered.add(it)
        if state.time == end_time:
            count += 1
            if state.score > best_found:
                print(count, "best so far ", state.score)
                best_found = state.score
        else:
            advances = state.advance(nodes, end_time, best_found, max_flow)
            state_queue.extend(advances)

    return best_found


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2022_16().run_cmdline()
