from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_12(DayBase):
    YEAR = "2017"
    DAY = "12"


def part_a(input, part_b=False):
    part_a = not part_b
    connections = []
    found = []
    for node, line in enumerate(input_generator(input)):
        fields = line.split("<->")
        assert int(fields[0]) == node
        connections.append([int(n) for n in fields[1].split(",")])
        found.append(False)

    groups = 0
    for start_node in range(len(connections)):
        if found[start_node]:
            continue
        queue = [start_node]
        count = 0
        groups += 1
        while queue:
            node = queue.pop()
            if found[node]:
                continue
            found[node] = True
            count += 1
            for n in connections[node]:
                if not found[n]:
                    queue.append(n)
        if part_a:
            return count
    return groups


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_12().run_cmdline()
