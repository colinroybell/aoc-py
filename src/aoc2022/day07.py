from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2022_07(DayBase):
    YEAR = "2022"
    DAY = "07"


class Node:
    def __init__(self, name, parent=None, dir=False, size=0):
        self.name = name
        self.parent = parent
        if parent:
            parent.add_child(name, self)
        self.children = {}
        self.size = size
        self.dir = dir

    def add_child(self, child_name, child):
        assert child_name not in self.children
        self.children[child_name] = child

    def get_size(self):
        print("get_size on {}".format(self.name))
        if self.dir:
            if self.size > 0:
                return self.size
            else:
                self.size = sum(child.get_size() for child in self.children.values())
                return self.size
        else:
            return self.size

    def get_recursive_size(self):
        limit = 100000
        if not self.dir:
            return 0

        print("Computing for {}".format(self.name))
        total = 0
        size = self.get_size()
        if size <= limit:
            total = size
        total += sum(child.get_recursive_size() for child in self.children.values())
        self.size = total
        return total

    def get_minimal_size(self, space):
        if not self.dir:
            return None
        else:
            best = None
            size = self.get_size()
            if size >= space:
                best = size
            for child in self.children.values():
                minimal = child.get_minimal_size(space)
                if minimal and (minimal < best or not best):
                    best = minimal
            print(self.name, size, space, best)
            return best

    def cd(self, name):
        if name == "/":
            if self.parent == None:
                return self
            else:
                return self.parent.cd("/")
        elif name == "..":
            return self.parent
        else:
            return self.children[name]


def part_a(input, part_b=False):
    top = Node(name="/", dir=True)
    current = top
    for line in input_generator(input):
        if line[0:4] == "$ cd":
            current = current.cd(line[5:])
        elif line[0:4] == "$ ls":
            pass
        else:
            fields = line.split()
            if fields[0] == "dir":
                child = Node(name=fields[1], parent=current, dir=True)
            else:
                child = Node(name=fields[1], parent=current, size=int(fields[0]))
    if not part_b:
        return top.get_recursive_size()
    else:
        free_space = 30000000 - (70000000 - top.get_size())
        print("top=", top.get_size(), free_space)
        return top.get_minimal_size(free_space)


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2022_07().run_cmdline()
