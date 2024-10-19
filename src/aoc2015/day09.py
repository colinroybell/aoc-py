from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_09(DayBase):
    YEAR = "2015"
    DAY = "09"


def recurse(node, dist, found, num_left, node_links, part_b):
    # print("node {} dist {} found {} num_left {}".format(node,dist,found,num_left))
    if num_left == 0:
        # print("End {}".format(dist))
        return dist
    best_dist = None
    for link, d in node_links[node].items():
        # print(link, d)
        if link not in found:
            new_dist = recurse(
                link, dist + d, found + [link], num_left - 1, node_links, part_b
            )
            if (
                best_dist == None
                or (not part_b and new_dist < best_dist)
                or (part_b and new_dist > best_dist)
            ):
                best_dist = new_dist
    # print("Returning {}".format(best_dist))
    return best_dist


def part_a(input, part_b=False):
    node_names = []
    node_links = {}
    for line in input_generator(input):
        fields = line.split()
        node1 = fields[0]
        node2 = fields[2]
        dist = fields[4]
        # print(node1,node2,dist)
        if node1 not in node_names:
            node_names.append(node1)
            node_links[node1] = {}
        if node2 not in node_names:
            node_names.append(node2)
            node_links[node2] = {}
        node_links[node1][node2] = int(dist)
        node_links[node2][node1] = int(dist)

    # print(node_links)

    best_dist = None
    for name in node_names:
        new_dist = recurse(name, 0, [name], len(node_names) - 1, node_links, part_b)
        if (
            best_dist == None
            or (not part_b and new_dist < best_dist)
            or (part_b and new_dist > best_dist)
        ):
            best_dist = new_dist
    return best_dist


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2015_09().run_cmdline()
