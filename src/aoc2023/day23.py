from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2023_23(DayBase):
    YEAR = "2023"
    DAY = "23"


def dir_to_index(dir):
    return ">v<^".index(dir)


def index_to_dir(index):
    return ">v<^"[index]


def rotateR(dir):
    return index_to_dir((dir_to_index(dir) + 1) % 4)


def rotateL(dir):
    return index_to_dir((dir_to_index(dir) - 1) % 4)


def flip(dir):
    return index_to_dir((dir_to_index(dir) + 2) % 4)


class Node:
    def __init__(self, id, pos):
        self.pos = pos
        self.id = id
        self.paths = []

    def __repr__(self):
        return "({}, {})".format(self.id, self.pos)


class Path:
    def __init__(self, node, dir):
        self.nodes = [node, None]
        self.dirs = [dir, None]
        self.length = 0
        self.usable = [True, True]

    def __repr__(self):
        return "({} {} {} {})".format(self.nodes, self.dirs, self.length, self.usable)

    def parse(self, grid, end_y):
        pos = self.nodes[0].pos
        dir = self.dirs[0]

        # print("Starting path at ",pos, self.nodes[0].id)

        pos = pos.move_y_flipped(dir)
        self.length = 1

        while True:
            if pos.y == end_y:
                # print("Reached end after ",self.length)
                self.dirs[1] = flip(dir)
                return (pos, "end")
            c = grid.get(pos)
            if c == dir:
                self.usable[1] = False
            elif flip(dir) == c:
                self.usable[0] = False
            dirs = []
            next_pos = None
            for d in "^>v<":
                if flip(d) != dir:
                    adj = pos.move_y_flipped(d)
                    if grid.get(adj) != "#":
                        dirs.append(d)
                        next_pos = adj
            assert len(dirs) > 0
            if len(dirs) > 1:
                # print("Reached junction with ",dirs," after ",self.length)
                self.dirs[1] = flip(dir)
                return (pos, dirs)
            dir = dirs[0]
            self.length += 1
            pos = next_pos
            # print("Moved {} {} {}".format(dir,pos,self.length))


# NB: better ways to handle cache


class State:
    def __init__(self, current, history):
        self.current = current
        self.history = history

    def __repr__(self):
        return "{} {}".format(self.current, sorted(self.history))

    def it(self):
        return (self.current, tuple(sorted(self.history)))

    def __lt__(self, other):
        return 0


def get_states(nodes, max_round, save_intermediates, start_node, end_node):
    round = 0
    # scores are negative so we do longest first
    state_queue = PriorityQueue()
    state_queue.put((0, (State(start_node, set()))))
    queue_count = 1
    maximum = 0
    end_count = 0

    states_return = []
    max_round += 1

    while round <= max_round:
        next_state_queue = PriorityQueue()
        round += 1
        print("Round", round, "states", queue_count, end_count)

        state_cache = set()
        queue_count = 0
        while not state_queue.empty():
            x = state_queue.get()
            (s, state) = x

            # print("Starting at ",state)
            if state.it() in state_cache:

                # print('in cache')
                continue
            else:
                state_cache.add(state.it())

            if round == max_round or save_intermediates:
                # print("returning",s,state)
                states_return.append((s, state))

            if round == max_round:
                continue

            this_node = nodes[state.current]
            if this_node == end_node:
                steps = -s
                end_count += 1
                # print('end at ',end_count, steps, round, state)
                maximum = max(maximum, steps)
            for p in this_node.paths:
                # print("Trying",p)
                (path, dir, path_end) = p
                other_node = path.nodes[1 - path_end]
                # No part_a condition here - note if we intend to fix up.
                if other_node.id in state.history:
                    continue
                new_history = state.history.copy()
                new_history.add(other_node.id)
                # print('move to ',other_node, 'dist',s-path.length)
                queue_count += 1
                next_state_queue.put(
                    (s - path.length, State(other_node.id, new_history))
                )
        state_queue = next_state_queue
    return states_return


def part_a(input, part_b=False):
    part_a = not part_b
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)

    nodes = {}
    paths = []
    start_node = Node("start", Vec2d(1, 0))
    nodes["start"] = start_node
    node_id = 0
    path_starts = [(start_node, "v")]
    while path_starts:
        (node, dir) = path_starts[0]
        path_starts = path_starts[1:]

        already_parsed = False
        for path in node.paths:
            if path[1] == dir:
                already_parsed = True
        if already_parsed:
            continue

        # need to check we haven't already done this

        path = Path(node, dir)
        paths.append(path)
        node.paths.append((path, dir, 0))
        (pos, parse_result) = path.parse(grid, height - 1)
        if parse_result == "end":
            end_node = Node("end", pos)
            nodes["end"] = end_node
            end_node.paths.append((path, path.dirs[1], 1))
            path.nodes[1] = end_node
        else:
            existing_node = False
            for node in nodes.values():
                if pos == node.pos:
                    # print("Reached existing node", node)
                    node.paths.append((path, path.dirs[1], 1))
                    path.nodes[1] = node
                    existing_node = True
            if not existing_node:
                str_id = "{:2d}".format(node_id)
                new_node = Node(str_id, pos)
                nodes[str_id] = new_node
                # print('Creating new node',new_node)
                path.nodes[1] = new_node
                new_node.paths.append((path, path.dirs[1], 1))
                node_id += 1
                for dir in parse_result:
                    path_starts.append((new_node, dir))

    # print(paths)
    if part_a:
        round = 0
        # scores are negative so we do longest first
        state_queue = PriorityQueue()
        state_queue.put((0, (State("start", set()))))
        queue_count = 1
        maximum = 0
        end_count = 0

        while not state_queue.empty():
            next_state_queue = PriorityQueue()
            round += 1
            print("Round", round, "states", queue_count, end_count)

            state_cache = set()
            queue_count = 0
            while not state_queue.empty():
                x = state_queue.get()
                (s, state) = x

                # print("Starting at ",state)
                if state.it() in state_cache:

                    # print('in cache')
                    continue
                else:
                    state_cache.add(state.it())
                this_node = nodes[state.current]
                if this_node == end_node:
                    steps = -s
                    end_count += 1
                    # print('end at ',end_count, steps, round, state)
                    maximum = max(maximum, steps)
                for p in this_node.paths:
                    # print("Trying",p)
                    (path, dir, path_end) = p
                    if part_a and not path.usable[path_end]:
                        continue
                    other_node = path.nodes[1 - path_end]
                    if other_node.id in state.history:
                        continue
                    new_history = state.history.copy()
                    new_history.add(other_node.id)
                    # print('move to ',other_node, 'dist',s-path.length)
                    queue_count += 1
                    next_state_queue.put(
                        (s - path.length, State(other_node.id, new_history))
                    )
            state_queue = next_state_queue
        return maximum
    if part_b:
        # Search from both ends and match up. Thing needs a ot of tidying up.
        num_steps = len(nodes) - 1
        second_steps = num_steps // 2
        first_steps = num_steps - second_steps
        print(num_steps, first_steps, second_steps)

        ret1 = get_states(nodes, first_steps, False, "start", nodes["end"])
        ret2 = get_states(nodes, second_steps, True, "end", nodes["start"])
        ret1.sort()
        ret2.sort()
        best = 0
        for i in ret1:
            (score1, state1) = i
            score1 = -score1
            node1 = state1.current
            history1 = state1.history
            for j in ret2:
                (score2, state2) = j
                score2 = -score2
                if score1 + score2 <= best:
                    break

                node2 = state2.current
                history2 = state2.history
                if node1 != node2:
                    continue
                for h1 in history1:
                    if h1 != node1 and h1 in history2:
                        break
                else:
                    total = score1 + score2
                    best = max(best, total)
                    print(i, j, score1, score2, score1 + score2)
        return best


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_23().run_cmdline()
