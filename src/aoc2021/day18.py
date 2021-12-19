from utils.day_base import DayBase
from utils.data_input import input_generator


class String:
    def __init__(self, line):
        self.chars = [c for c in line]

    def pop(self):
        c = self.chars.pop(0)
        print(c)
        return c


class Node:
    def __init__(self):
        self.items = [None, None]
        self.parent = None
        self.index = None

    @staticmethod
    def parse_line(line_in):
        line = String(line_in)
        print(line)
        assert line.pop() == "[", "not ["
        return Node.parse_line_recurse(line)

    @staticmethod
    def parse_line_recurse(line):
        node = Node()
        c = line.pop()
        if c == "[":
            node.items[0] = node.parse_line_recurse(line)
            node.items[0].parent = node
            node.items[0].index = 0
        else:
            node.items[0] = int(c)

        c = line.pop()
        while c != ",":
            node.items[0] = node.items[0] * 10 + int(c)
            c = line.pop()

        c = line.pop()
        if c == "[":
            node.items[1] = node.parse_line_recurse(line)
            node.items[1].parent = node
            node.items[1].index = 1
        else:
            node.items[1] = int(c)

        c = line.pop()
        while c != "]":
            node.items[1] = node.items[1] * 10 + int(c)
            c = line.pop()

        return node

    @staticmethod
    def parse(input):
        node = None
        for line in input_generator(input):
            new_node = Node.parse_line(line)
            if node == None:
                node = new_node
            else:
                node = Node.plus(node, new_node)
        return node

    @staticmethod
    def plus(n1, n2):
        node = Node()
        node.items[0] = n1
        n1.parent = node
        n1.index = 0
        node.items[1] = n2
        n2.parent = node
        n2.index = 1
        node.reduce()
        return node

    def string(self):
        return self.__str__()

    def __str__(self):
        return "[{},{}]".format(self.items[0], self.items[1])

    def try_explode(self, level):
        if level < 4:
            for i in range(2):
                if type(self.items[i]) == Node:
                    if self.items[i].try_explode(level + 1):
                        if level == 3:
                            self.items[i] = 0
                        return True
            return False
        else:
            for s in range(2):
                node = self
                while node and node.index == s:
                    node = node.parent
                if node and node.parent:
                    node = node.parent
                    if type(node.items[s]) != Node:
                        node.items[s] += self.items[s]
                    else:
                        node = node.items[s]
                        while type(node.items[1 - s]) == Node:
                            node = node.items[1 - s]
                        node.items[1 - s] += self.items[s]
            return True

    def try_split(self):
        print(self)
        for s in range(2):
            if type(self.items[s]) == Node:
                if self.items[s].try_split():
                    return True
            else:
                v = self.items[s]
                if v >= 10:
                    self.items[s] = Node()
                    self.items[s].parent = self
                    self.items[s].index = s
                    self.items[s].items[0] = v // 2
                    self.items[s].items[1] = v - self.items[s].items[0]
                    return True
        return False

    def reduce(self):
        done = False
        while not done:
            done = True
            if self.try_explode(0):
                done = False
            elif self.try_split():
                done = False

    def magnitude(self):
        v = [0, 0]
        for s in range(2):
            v[s] = self.items[s]
            if type(v[s]) == Node:
                v[s] = v[s].magnitude()
        return 3 * v[0] + 2 * v[1]


class Run_2021_18(DayBase):
    YEAR = "2021"
    DAY = "18"


def part_a(input):
    node = Node.parse(input)
    return node.magnitude()


def part_b(input):
    lines = []
    for line in input_generator(input):
        lines.append(line)

    maximum = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                node = Node.parse([lines[i], lines[j]])
                maximum = max(maximum, node.magnitude())
    return maximum


if __name__ == "__main__":
    Run_2021_18().run_cmdline()
