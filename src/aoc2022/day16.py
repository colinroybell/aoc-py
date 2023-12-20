from utils.day_base import DayBase
from utils.data_input import input_generator
import re

# TODO: correct approach is to do path-analysis and then just pick off a next one to go to, prioritising something like additional delta/time


class Run_2022_16(DayBase):
    YEAR = "2022"
    DAY = "16"


class State:
    def __init__(self, count, time, pos, opened, score, residual, path=[]):
        self.count = count
        self.first_time = time
        self.time = time
        self.pos = pos
        self.opened = opened
        self.residual = residual
        self.score = score
        self.path = path

    def copy(self):
        return State(
            self.count,
            self.time.copy(),
            self.pos.copy(),
            self.opened.copy(),
            self.score,
            self.residual,
            self.path.copy(),
        )

    def iterable(self):
        if self.count == 1:
            return ((self.time[0], self.pos[0], tuple(self.opened)), self.score)
        else:
            positions = tuple(
                set([(self.time[0], self.pos[0]), (self.time[1], self.pos[1])])
            )
            return ((positions, tuple(self.opened)), self.score)

    def __repr__(self):
        return "time {} pos {} opened {} score {} path {}".format(
            self.time, self.pos, self.opened, self.score, self.path
        )

    def advance(self, end_time, best):

        advances = []

        first_time = min(self.time)

        for i in range(self.count):
            if self.time[i] == first_time:
                adv = i

        time_offset = 1
        # TODO: incorporate this in distance calculations
        if self.pos[adv].name == "AA":
            time_offset = 0

        best_possible = self.score
        for (t, dist) in self.pos[adv].tunnels:
            if t.name not in self.opened:
                best_possible += (end_time - first_time - 1) * t.flow_rate

        if best_possible <= best:
            # print("Cull {} vs {}".format(best_possible,best))
            return []
        advanced = False

        for (t, dist) in self.pos[adv].tunnels:
            if t.name in self.opened:
                continue
            if t.name == "AA":
                continue
            dist += time_offset
            if self.time[adv] + dist >= end_time:
                continue
            new = self.copy()
            # print(new)
            new.time[adv] += dist
            new.pos[adv] = t
            new.opened.add(t.name)
            new.score += (end_time - new.time[adv] - 1) * t.flow_rate
            new.residual -= t.flow_rate
            new.path.append((new.pos[adv].name, new.time[adv]))
            # print('to',new)
            # print("Advance to ",new)
            advances.append(new)
            advanced = True

        if not advanced:
            # Just sit there
            new = self.copy()
            new.time[adv] = end_time
            advances.append(new)

        def sort_func(e):
            return e.score

        advances.sort(key=sort_func)

        return advances


class InputNode:
    def init_class():
        Node.match_re = re.compile(r"Valve (\w+).+?(\d+).+?valves? (.+)")

    def __init__(self, string):
        m = Node.match_re.match(string)
        assert m
        self.name = m.group(1)
        self.flow_rate = int(m.group(2))
        self.tunnels = m.group(3).split(", ")


class Node:
    def __init__(self, name, flow_rate):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = []

    def set_distances(self, input_nodes, nodes):
        seen = set()
        node_queue = [(self.name, 0)]
        print("From", self.name)
        while node_queue:
            (name, dist) = node_queue[0]
            node_queue = node_queue[1:]
            if name in seen:
                continue
            seen.add(name)
            if name in nodes and dist > 0:
                print("To {} at {}".format(name, dist))
                self.tunnels.append((nodes[name], dist))
            for t in input_nodes[name].tunnels:
                if t not in seen:
                    node_queue.append((t, dist + 1))

        def sort_func(e):
            return e[0].flow_rate

        self.tunnels.sort(key=sort_func)

    def __repr__(self):
        return self.name


def part_a(input, part_b=False):
    part_a = not part_b
    input_nodes = {}
    nodes = {}
    InputNode.init_class()
    max_flow = 0
    for line in input_generator(input):
        input_node = InputNode(line)
        input_nodes[input_node.name] = input_node

        if input_node.flow_rate or input_node.name == "AA":
            node = Node(input_node.name, input_node.flow_rate)
            nodes[node.name] = node

    for node in nodes.values():
        node.set_distances(input_nodes, nodes)

    total_flow = sum(node.flow_rate for node in nodes.values())

    if part_a:
        initial_state = State(1, [0], [nodes["AA"]], set(), 0, total_flow)
        end_time = 30
    else:
        initial_state = State(
            2, [0, 0], [nodes["AA"], nodes["AA"]], set(), 0, total_flow
        )
        end_time = 26

    state_queue = [initial_state]
    states_considered = {}
    count = 0
    best_found = 0

    while state_queue:
        state = state_queue.pop()
        # print("Considering {} with {} left on queue".format(state,len(state_queue)))

        count += 1
        if len(state.path) == 3:
            print(count, state.path, best_found)
        (it, score) = state.iterable()
        if it in states_considered and states_considered[it] >= score:
            continue
        else:
            states_considered[it] = score
        if min(state.time) == end_time:
            if state.score > best_found:
                print(count, "best so far", state.score)
                best_found = state.score
        else:
            advances = state.advance(end_time, best_found)
            state_queue.extend(advances)
    return best_found

    return 0


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2022_16().run_cmdline()
