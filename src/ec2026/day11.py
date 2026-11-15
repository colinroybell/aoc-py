from utils.day_base import DayBase
from utils.data_input import input_generator
from copy import deepcopy


class Run_2026_11(DayBase):
    YEAR = "2026"
    DAY = "11"
    PREFIX = "ec"


# TODO: can this be made more efficient? Takes about 10s to run


def portal_strain(portal, links):
    total = 0
    found = set()
    queue = [(portal, 0)]
    while queue:
        (item, score) = queue[0]
        queue = queue[1:]
        if item not in found:
            total += score
            found.add(item)

            for node in links[item]:
                if node not in found:
                    queue.append((node, score + 1))
    return total


def strain(portals, links):
    return sum(portal_strain(portal, links) for portal in range(1, portals + 1))


def compute_crystal_pairings(n, used):
    first = None
    ret = []
    for p in range(8):
        if p in used:
            continue
        elif first == None:
            first = p
            used.add(p)
        else:
            if n == 1:
                ret.append([(first, p)])
            else:
                used.add(p)
                sub_pairing = compute_crystal_pairings(n - 1, used)
                for sp in sub_pairing:
                    ret.append([(first, p)] + sp)
                used.remove(p)
    used.remove(first)
    return ret


def part_1(input):
    generator = input_generator(input)
    portals = int(next(generator).split(" ")[1])

    links = {}
    for i in range(1, portals + 1):
        if i == 1:
            links[i] = [2, portals]
        elif i == portals:
            links[i] = [1, portals - 1]
        else:
            links[i] = [i - 1, i + 1]
    base_strain = strain(portals, links)
    _ = next(generator)
    for line in generator:
        nodes = [int(x) for x in line.split(" ")]
        links[nodes[0]].append(nodes[1])
        links[nodes[1]].append(nodes[0])
    reduced_strain = strain(portals, links)

    return base_strain - reduced_strain


def part_2(input, part=2):
    generator = input_generator(input)
    portals = int(next(generator).split(" ")[1])

    links = {}
    for i in range(1, portals + 1):
        links[i] = []
        for j in range(-3, 4):
            if j != 0:
                links[i].append((i + j - 1) % portals + 1)
    base_strain = strain(portals, links)
    _ = next(generator)
    for line in generator:
        nodes = [int(x) for x in line.split(" ")]
        links[nodes[0]].append(nodes[1])
        links[nodes[1]].append(nodes[0])

    min_reduced_strain = base_strain

    if part == 2:

        for i in range(1, portals + 1):
            for j in range(i + 1, portals + 1):
                links_copy = deepcopy(links)
                links_copy[i].append(j)
                links_copy[j].append(i)
                min_reduced_strain = min(
                    min_reduced_strain, strain(portals, links_copy)
                )
    else:
        crystal_pairings = compute_crystal_pairings(4, set())
        print(crystal_pairings)
        for i in range(1, portals // 8 + 1):
            for pairings in crystal_pairings:
                links_copy = deepcopy(links)
                for p, q in pairings:
                    p = i + p * portals // 8
                    q = i + q * portals // 8
                    links_copy[p].append(q)
                    links_copy[q].append(p)
                    min_reduced_strain = min(
                        min_reduced_strain, strain(portals, links_copy)
                    )

    return base_strain - min_reduced_strain


def part_3(input):
    return part_2(input, part=3)


if __name__ == "__main__":
    Run_2026_11().run_cmdline()
