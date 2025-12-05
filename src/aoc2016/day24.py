from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from utils.maze import MazeStructure, MazeAdjacency, grid_to_maze
from queue import PriorityQueue


class Run_2016_24(DayBase):
    YEAR = "2016"
    DAY = "24"


def part_a(input, part="a"):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings_generator(input_generator(input))
    for x in range(width):
        for y in range(height):
            if grid.get(Vec2d(x, y)) == "0":
                start = Vec2d(x, y)

    maze = grid_to_maze(grid, start, "0")
    print(maze.pois)
    for id in maze.nodes.keys():
        node = maze.nodes[id]
        print("Node {} poi {}", id, node.poi)
        for adj in node.adjs:
            print("{} {}".format(adj.id, adj.dist))

    links = {}
    target = set(maze.pois)
    for start_id in maze.poi_ids:
        start_poi = maze.nodes[start_id].poi
        links[start_poi] = {}
        pois_found = set([start_poi])
        nodes_found = set()

        queue = PriorityQueue()

        queue.put((0, start_id))

        while not pois_found == target:
            (t, id) = queue.get()
            print("Starting at {} {}".format(t, id))
            if id in nodes_found:
                continue
            else:
                nodes_found.add(id)

            poi = maze.nodes[id].poi
            if poi != None and poi not in pois_found:
                pois_found.add(poi)
                links[start_poi][poi] = (t, id)
                print("dist from {} to {} is {}".format(start_poi, poi, t))

            for a in maze.nodes[id].adjs:
                new_t = t + a.dist
                new_id = a.id
                poi = maze.nodes[new_id].poi
                queue.put((new_t, new_id))

    queue = PriorityQueue()
    queue.put((0, (0, set(["0"]))))
    found = set()
    while not queue.empty():
        (t, state) = queue.get()
        print("state", t, state)
        (id, pois_found) = state
        hash_state = (id, frozenset(pois_found))
        if hash_state in found:
            continue
        found.add(hash_state)

        if pois_found == target and (part == "a" or id == 0):
            return t
        print(links[maze.nodes[id].poi])
        for poi, link in links[maze.nodes[id].poi].items():
            new_pois_found = pois_found.copy()
            new_pois_found.add(poi)
            (dist, new_id) = link

            queue.put((t + dist, (new_id, new_pois_found)))


def part_b(input):
    return part_a(input, part="b")


def notes():
    """
    Works, but want to do the dead end elimination. Second case is if something has two edges,
    then we just omit it.
    """


if __name__ == "__main__":
    Run_2016_24().run_cmdline()
