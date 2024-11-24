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
    return part_3(input)


class FoundHerbCache:
    def __init__(self):
        self.found = []

    def add(self, item):
        new_found = []
        old_count = len(self.found)
        for c in self.found:
            if not c.issubset(item):
                new_found.append(c)
        self.found = new_found
        self.found.append(item)
        new_count = len(self.found)
        print("count", old_count, new_count, self.found)

    def already_found(self, item):
        for c in self.found:
            if item.issubset(c):
                return True
        return False


def grid_cull(grid, x, y):
    # if we get a pattern #.H.# with same H above and below, we don't need this
    h = grid.get(Vec2d(x, y))
    if (
        grid.get(Vec2d(x, y + 1)) == h
        and grid.get(Vec2d(x, y - 1)) == h
        and grid.get(Vec2d(x + 1, y)) == "."
        and grid.get(Vec2d(x + 2, y)) == "#"
        and grid.get(Vec2d(x - 1, y)) == "."
        and grid.get(Vec2d(x - 2, y)) == "#"
    ):
        return True
    else:
        return False


# Get rid of obviously redundant ones around lakes


def lake_cull(grid, xx, yy):
    print("Lake at ", xx, yy)
    xx -= 10
    yy -= 2
    h = grid.get(Vec2d(xx + 6, yy))
    print("herb", h)
    keep = [(0, 4), (0, 7), (0, 8), (10, 12), (18, 12), (28, 5), (28, 6), (28, 8)]
    for x in range(0, 29):
        for y in range(0, 13):
            if grid.get(Vec2d(xx + x, yy + y)) == h:
                if (x, y) not in keep:
                    print("lake cull ", x, y)
                    grid.set(Vec2d(xx + x, yy + y), ".")


def part_3(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)

    all_herbs = set()
    locations = []

    for x in range(width):
        pos = Vec2d(x, 0)
        if grid.get(pos) == ".":
            start = pos
            grid.set(pos, "$")

    loc_counts = {}

    # Cull around lakes

    lake_found = False
    for y in range(height):
        last = None
        for x in range(width):
            pos = Vec2d(x, y)
            c = grid.get(pos)
            if c == "~" and last == ".":
                lake_cull(grid, x, y)
                lake_found = True
            last = c
        if lake_found:
            break

    for y in range(height):
        for x in range(width):
            pos = Vec2d(x, y)
            c = grid.get(pos)
            if c not in [".", "#", "~"]:
                if c != "$":
                    all_herbs.add(c)
                if grid_cull(grid, x, y):
                    pass
                    # print("cull ",x,y)
                else:
                    locations.append(pos)
                    if c not in loc_counts:
                        loc_counts[c] = 0
                    loc_counts[c] += 1
    print(loc_counts)

    # TODO: more efficient to do a single floodfill starting from each point.
    transitions = {}
    for location in locations:
        # print("Search from ",location)
        found = {}
        transitions[location.tuple()] = []
        start_state = State(location)
        state_queue = PriorityQueue()
        state_queue.put((0, start_state))
        while not state_queue.empty():
            x = state_queue.get()
            (t, state) = x
            pos = state.current

            cache_state = pos.tuple()
            if cache_state in found:
                continue
            found[cache_state] = t
            pos_height = grid.get(pos)

            if t > 0 and pos in locations:
                transitions[location.tuple()].append((t, pos, pos_height))
                # print("Found ",pos,pos_height," at ",t)

            vecs = pos.get_adjacent_orthogonal()
            for v in vecs:
                v_height = grid.get(v)
                if v_height and v_height not in ["#", "~"]:
                    new_t = t + 1
                    new_state = State(v)
                    state_queue.put((new_t, new_state))
    # Main search
    found = {}
    for location in locations:
        found[location.tuple()] = FoundHerbCache()

    start_state = State(start)
    state_queue = PriorityQueue()
    state_queue.put((0, start_state))
    while not state_queue.empty():
        x = state_queue.get()
        (t, state) = x
        pos = state.current
        herbs = state.herbs
        # print(t,"start at",pos,herbs, 'queue length',state_queue.qsize())

        if pos == start and t > 0:
            # print("done")
            return t
        cache = found[pos.tuple()]
        if cache.already_found(herbs):
            # print("Already found")
            continue
        cache.add(herbs)

        for transition in transitions[pos.tuple()]:
            # print("Considering",transition)
            d, new_pos, h = transition
            if h in herbs:
                # print("... already have this herb")
                continue
            if h == "$" and herbs != all_herbs:
                # print("... can't go to finish without all herbs")
                continue
            cache = found[new_pos.tuple()]
            new_herbs = herbs.copy()
            new_herbs.add(h)
            if cache.already_found(new_herbs):
                # print("... already found those herbs at location")
                continue
            # print("... add to queue")
            new_state = State(new_pos, new_herbs)
            state_queue.put((t + d, new_state))


if __name__ == "__main__":
    Run_2024_15().run_cmdline()
