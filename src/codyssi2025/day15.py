from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_15(DayBase):
    YEAR = "2025"
    DAY = "15"
    PREFIX = "codyssi"


class BinaryTreeNode:
    def __init__(self, id, value, level):
        self.id = id
        self.value = value
        self.level = level
        self.sub = [None, None]
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, id, value):
        if not self.root:
            self.root = BinaryTreeNode(id, value, 0)
            return 0, ""
        else:
            node = self.root
            trace = node.id
            while 1:
                if value < node.value:
                    pos = 0
                else:
                    pos = 1
                if node.sub[pos]:
                    node = node.sub[pos]
                    trace = trace + "-" + node.id
                else:
                    node.sub[pos] = BinaryTreeNode(id, value, node.level + 1)
                    return node.level + 1, trace


def part_1(input, part=1):
    counts = []
    traces = {}
    highest = 0
    tree = BinaryTree()
    generator = input_generator(input)
    for line in generator:
        if not line:
            break
        fields = line.split()
        # TODO: notation above has id for name
        id = int(fields[2])
        level, trace = tree.add(fields[0], id)
        traces[fields[0]] = trace

        if len(counts) > level:
            counts[level] += id
        else:
            counts.append(id)
        # print(level, id, counts[level])
        if counts[level] > highest:
            highest = counts[level]
    if part == 1:
        return highest * (len(counts))
    elif part == 2:
        _, trace = tree.add(None, 500000)
        return trace
    else:
        path0 = traces[next(generator).split()[0]].split("-")
        path1 = traces[next(generator).split()[0]].split("-")
        lca = None
        count = 0
        while (
            count < len(path0) and count < len(path1) and path0[count] == path1[count]
        ):
            lca = path0[count]
            count += 1
        return lca


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2025_15().run_cmdline()
