from utils.day_base import DayBase
from utils.data_input import input_generator
from typing import NamedTuple


class Run_st03_03(DayBase):
    YEAR = "st03"
    DAY = "03"
    PREFIX = "ec"

    NOTES = """ Mostly done. We will need to pass tnode back down as well, and think carefully about ordering.
    
    Can we parametrise left and right sensibly?"""


PART = 1


class Node(NamedTuple):
    id: int
    plug: str
    left: str
    right: str
    data: str


def strong_match(plug, socket):
    return plug == socket


def weak_match(plug, socket):
    pf = plug.split(" ")
    sf = socket.split(" ")
    return pf[0] == sf[0] or pf[1] == sf[1]


def plug_socket_match(plug, socket):
    if PART == 1:
        return strong_match(plug, socket)
    else:
        return weak_match(plug, socket)


class TreeNode:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

    def addNode(self, tnode):
        if self.left:
            tnode = self.left.addNode(tnode)
            if tnode == None:
                return None
        else:
            if plug_socket_match(self.node.left, tnode.node.plug):
                self.left = tnode
                print("Adding {} under {} left".format(tnode.node.id, self.node.id))
                return None

        if self.right:
            tnode = self.right.addNode(tnode)
            if tnode == None:
                return None
        else:
            if plug_socket_match(self.node.right, tnode.node.plug):
                self.right = tnode
                print("Adding {} under {} right".format(tnode.node.id, self.node.id))
                return None
        return tnode

    def compute_id(self, count):
        id = 0
        if self.left:
            (left_id, count) = self.left.compute_id(count)
            id += left_id
        count += 1
        id += count * self.node.id
        if self.right:
            (right_id, count) = self.right.compute_id(count)
            id += right_id
        return (id, count)


class Tree:
    def __init__(self):
        self.root = None

    def add(self, node):
        tnode = TreeNode(node)
        if self.root == None:
            self.root = tnode
        else:
            tnode = self.root.addNode(tnode)
            assert tnode==None

    def compute_id(self):
        assert self.root
        return self.root.compute_id(0)[0]


def part_1(input, part=1):
    PART = part
    tree = Tree()
    for line in input_generator(input):
        print(line)
        fields = line.split(",")
        data = [f.split("=")[1] for f in fields]
        node = Node(
            id=int(data[0]), plug=data[1], left=data[2], right=data[3], data=data[4]
        )
        tree.add(node)
    return tree.compute_id()


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_st03_03().run_cmdline()
