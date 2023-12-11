from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2023_08(DayBase):
    YEAR = "2023"
    DAY = "08"


def lcm(x, y):
    a = max(x, y)
    b = min(x, y)

    while b > 0:
        print("lcm", a, b)
        c = a % b
        a = b
        b = c
    return x * y // a


def steps(nodes, node, instructions, part_a):
    count = 0
    print(nodes)
    while 1:
        print(count, node)
        for c in instructions:
            node = nodes[node][c]
            count += 1
            if part_a and node == "ZZZ":
                return count
            if not part_a and node[2] == "Z":
                return count


def part_a(input, part_b=False):
    part_a = not part_b
    count = 0
    nodes = {}
    a_nodes = []
    for line in input_generator(input):
        print(count, line)
        if count == 0:
            instructions = line
        if count > 1:
            node = line[0:3]
            left = line[7:10]
            right = line[12:15]
            nodes[node] = {}
            nodes[node]["L"] = left
            nodes[node]["R"] = right
            if node[2] == "A":
                a_nodes.append(node)
            # print(nodes)
        count += 1

    if part_a:
        print("a")
        return steps(nodes, "AAA", instructions, part_a)
    else:
        answer = None
        for node in a_nodes:
            print("a_node", node)
            value = steps(nodes, node, instructions, part_a)
            if answer == None:
                answer = value
            else:
                answer = lcm(answer, value)
        return answer


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_08().run_cmdline()
