from utils.day_base import DayBase
from utils.data_input import input_generator
import functools


class Run_2022_13(DayBase):
    YEAR = "2022"
    DAY = "13"


class Node:
    def __init__(self, parent, value, divider=False):
        self.value = value
        self.children = []
        self.parent = parent
        if parent != None:
            self.parent.children.append(self)
        self.divider = divider

    def __str__(self):
        if self.value:
            return str(self.value)
        else:
            if self.divider:
                string = "D"
            else:
                string = ""
            string += "["
            for i in range(len(self.children)):
                string += self.children[i].__str__()
                if i < len(self.children) - 1:
                    string += ","
            string += "]"
            return string


def parse(line, parent=None):
    while line:
        c = line.pop(0)
        if c == "[":
            node = Node(parent, None)
            parse(line, node)
        elif c.isnumeric():
            val = int(c)
            while line[0].isnumeric():
                c = line.pop(0)
                val = val * 10 + int(c)
            node = Node(parent, val)
        elif c == "]":
            return
        elif c == ",":
            pass
        else:
            assert 0


def compare(left, right):
    if left.value != None and right.value != None:
        if left.value < right.value:
            return -1
        elif left.value > right.value:
            return 1
        else:
            return 0
    if left.value == None and right.value != None:
        node = Node(right, right.value)
        right.value = None
    if left.value != None and right.value == None:
        node = Node(left, left.value)
        left.value = None
    index = 0
    while 1:
        if index == len(left.children) and index < len(right.children):
            return -1
        if index < len(left.children) and index == len(right.children):
            return 1
        if index == len(left.children) and index == len(right.children):
            return 0
        cmp = compare(left.children[index], right.children[index])
        if cmp != 0:
            return cmp
        index += 1


def part_a(input):
    index = 1
    count = 0
    total = 0
    for line in input_generator(input):
        if count == 0:
            left = Node(None, None)
            parse(list(line), left)
        elif count == 1:
            right = Node(None, None)
            parse(list(line), right)
            if compare(left, right) == -1:
                total += index
        else:
            count = -1
            index += 1
        count += 1
    return total


def part_b(input):
    nodes = []
    for line in input_generator(input):
        if line:
            node = Node(None, None)
            parse(list(line), node)
            nodes.append(node)
    for line in ("[[2]]", "[[6]]"):
        node = Node(None, None, divider=True)
        parse(list(line), node)
        nodes.append(node)

    nodes_sorted = sorted(nodes, key=functools.cmp_to_key(compare))
    div = 1
    for i, node in enumerate(nodes_sorted):
        if node.divider:
            div *= i + 1
    return div


if __name__ == "__main__":
    Run_2022_13().run_cmdline()
