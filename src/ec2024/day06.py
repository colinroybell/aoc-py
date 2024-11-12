from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_06(DayBase):
    YEAR = "2024"
    DAY = "06"
    PREFIX = "ec"


def recurse(part, nodes, node, count, string):
    fruits = {}
    if node == "@":
        fruits[count] = string
    elif node == "ANT" or node == "BUG":
        pass
    elif node in nodes:
        for s in nodes[node]:
            if part == 1:
                new_string = string + s
            else:
                new_string = string + s[0]
            s_fruits = recurse(part, nodes, s, count + 1, new_string)
            for s_count, s_string in s_fruits.items():
                if s_count not in fruits:
                    fruits[s_count] = s_string
                else:
                    fruits[s_count] = "DUP"
    return fruits


def part_1(input, part=1):
    nodes = {}
    for line in input_generator(input):
        fields = line.split(":")
        subnodes = fields[1].split(",")
        nodes[fields[0]] = subnodes
    if part == 1:
        base_string = "RR"
    else:
        base_string = "R"
    fruits = recurse(part, nodes, "RR", 1, base_string)
    for count, string in fruits.items():
        if string != "DUP":
            return string
    return "none"


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2024_06().run_cmdline()
