from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from utils.grid_2d import Grid2d
from collections import defaultdict
from math import sqrt, ceil
from queue import PriorityQueue


class Run_2025_17(DayBase):
    YEAR = "2025"
    DAY = "17"
    PREFIX = "ec"


def part_1(input):
    grid = Grid2d()
    dist = 10
    dist2 = dist * dist
    (width, height) = grid.read_from_file_strings(input)
    volcano = None
    for x in range(width):
        for y in range(height):
            p = Vec2d(x, y)
            print(p, grid.get(p))
            if grid.get(p) == "@":
                volcano = p
                print(x, y)
                break
        if volcano:
            break
    total = 0
    for x in range(width):
        for y in range(height):
            d2 = (x - volcano.x) * (x - volcano.x) + (y - volcano.y) * (y - volcano.y)
            if 0 < d2 <= dist2:
                total += int(grid.get(Vec2d(x, y)))
    return total


def part_2(input):
    grid = Grid2d()

    (width, height) = grid.read_from_file_strings(input)
    volcano = None
    for x in range(width):
        for y in range(height):
            p = Vec2d(x, y)
            if grid.get(p) == "@":
                volcano = p
                print(x, y)
                break
        if volcano:
            break
    totals = defaultdict(int)
    for x in range(width):
        for y in range(height):
            d = int(
                ceil(
                    sqrt(
                        (x - volcano.x) * (x - volcano.x)
                        + (y - volcano.y) * (y - volcano.y)
                    )
                )
            )
            if d > 0:
                totals[d] += int(grid.get(Vec2d(x, y)))
    print(totals)
    best = max(totals, key=totals.get)
    return best * totals[best]


class ScoreCache:
    def __init__(self):
        self.bests = {}

    def try_best(self, loc, time, dist, winding):
        if loc not in self.bests:
            self.bests[loc] = {}
        if winding not in self.bests[loc]:
            self.bests[loc][winding] = {}
        for d, t in self.bests[loc][winding].items():
            # print('Comparing',time, dist,' with',d,t)
            if d >= dist and t <= time:
                # print('... and quitting')
                return False
        self.bests[loc][winding][dist] = time
        return True

    def find_match(self, loc, time, dist, winding):
        """Require the given winding number, minimum distance"""
        if loc not in self.bests or winding not in self.bests[loc]:
            return None
        best = None
        for d, t in self.bests[loc][winding].items():
            required_dist = min(d, dist)
            joint_time = t + time
            if joint_time <= 30 * required_dist and (best == None or joint_time < best):
                best = joint_time
                # print("Pair ",loc,time,dist,winding,"with",d,t,'Joint time',joint_time, 'required dist',required_dist)
        return best


def distance(p, v):
    return int(ceil(sqrt((p.x - v.x) * (p.x - v.x) + (p.y - v.y) * (p.y - v.y))))


def part_3(input):
    grid = Grid2d()
    bests = defaultdict()

    (width, height) = grid.read_from_file_strings(input)
    volcano = None
    start = None
    for x in range(width):
        for y in range(height):
            p = Vec2d(x, y)
            if grid.get(p) == "@":
                volcano = p
            if grid.get(p) == "S":
                start = p

    sc = ScoreCache()
    queue = PriorityQueue()
    dist = distance(start, volcano)
    assert sc.try_best(start, 0, dist, 0)
    queue.put((0, (start, dist, 0)))
    best = None
    cases = 0
    while not queue.empty():
        (t, (p, dist, winding)) = queue.get()
        cases += 1
        # print('Trying',t,p,dist,winding, 'cases',cases)

        # Quit if we are going to exceed best on our own. Will be better optimisations than this
        g = grid.get(p)
        if best and g.isdigit():
            if t - int(g) > best:
                continue

        match = sc.find_match(p, t, dist, 1 - winding)
        if match:
            g = grid.get(p)
            match -= int(g)
            # print('Match totalling ',match)
            if best == None or match < best:
                best = match
            continue
        dirs = "URDL"
        for dir in dirs:
            adj = p.move(dir)
            g = grid.get(adj)
            if not g or not g.isdigit():
                continue
            v = int(g)
            adj_time = t + v
            adj_dist = min(dist, distance(adj, volcano))
            if dist * 30 < adj_time:
                continue
            adj_winding = winding
            if dir == "R" and adj.x == volcano.x and adj.y > volcano.y:
                adj_winding += 1
            if dir == "L" and p.x == volcano.x and p.y > volcano.y:
                adj_winding -= 1
            if (
                adj_winding < 0
            ):  # don't try this. If there's a 2 -1 to be found we will continue with the 2 and back down to 1 again.
                continue
            if sc.try_best(adj, adj_time, adj_dist, adj_winding):
                # print('Putting',adj_time,adj,adj_dist,adj_winding)
                queue.put((adj_time, (adj, adj_dist, adj_winding)))
    # print("cases",cases)
    return best * (best // 30)


if __name__ == "__main__":
    Run_2025_17().run_cmdline()
