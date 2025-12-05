from utils.vec_2d import Vec2d, opposite_direction
from utils.grid_2d import Grid2d
from collections import namedtuple

MazeAdjacency = namedtuple("MazeAdjacency", ["id", "dist"])


class MazeNode:
    def __init__(self, id, loc, poi):
        self.id = id
        self.loc = loc
        self.poi = poi
        self.adjs = []


class MazeStructure:
    def __init__(self):
        self.nodes = {}
        self.next_id = 0
        self.pois = []
        self.poi_ids = []

    def get_next_id(self):
        self.next_id += 1
        return self.next_id - 1

    def add_node(self, node):
        self.nodes[node.id] = node

    def remove_dead_ends(self):
        nodes = list(self.nodes.keys())
        while nodes:
            id = nodes.pop()
            node = self.nodes[id]
            if node.poi == None and len(node.adjs) == 1:
                # Dead end
                del self.nodes[id]
                nodes.append(node.adjs[0].id)

    def find_node_with_location(self, pos):
        for id in self.nodes.keys():
            if self.nodes[id].loc == pos:
                return id
        return None


def grid_to_maze(grid, start, start_poi="start"):

    structure = MazeStructure()
    start_id = structure.get_next_id()
    start_node = MazeNode(start_id, start, start_poi)
    structure.nodes[start_id] = start_node
    structure.pois.append(start_poi)
    structure.poi_ids.append(start_id)
    edges_found = set()

    print(grid.get(start))
    assert grid.get(start) == "0"

    start_positions = []
    for dir in "UDLR":
        if grid.get(start.move(dir)) != "#":
            start_positions.append((start_node.id, dir))

    while start_positions:
        start_pos = start_positions.pop()
        if start_pos in edges_found:
            continue
        edges_found.add(start_pos)
        dist = 1
        (start_id, start_dir) = start_pos
        start_node = structure.nodes[start_id]
        dir = start_dir
        pos = start_node.loc.move(dir)
        dist = 1
        done = False
        print("starting at {} {}".format(start_id, pos, dir))
        while not done:
            next_dirs = []
            for new_dir in "UDLR":
                if new_dir != opposite_direction(dir):
                    if grid.get(pos.move(new_dir)) != "#":
                        next_dirs.append(new_dir)

            poi = grid.get(pos)
            if poi != "." or len(next_dirs) != 1:
                # New node
                id = structure.find_node_with_location(pos)
                if id == None:
                    new_id = structure.get_next_id()
                    id = new_id
                    if poi == ".":
                        poi = None
                    else:
                        structure.pois.append(poi)
                        structure.poi_ids.append(id)
                    new_node = MazeNode(new_id, pos, poi)
                    structure.nodes[new_id] = new_node

                    for next_dir in next_dirs:
                        start_positions.append((new_id, next_dir))
                else:
                    new_node = structure.nodes[id]
                adj_forward = MazeAdjacency(id=id, dist=dist)
                start_node.adjs.append(adj_forward)
                adj_backward = MazeAdjacency(id=start_id, dist=dist)
                new_node.adjs.append(adj_backward)
                edges_found.add((id, opposite_direction(dir)))
                done = True
            else:
                pos = pos.move(next_dirs[0])
                dist += 1
    # structure.remove_dead_ends()
    return structure
