from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_3d import Vec3d
from collections import defaultdict


class Run_2025_08(DayBase):
    YEAR = "2025"
    DAY = "08"


def part_a(input, junctions=1000):
    points = []
    dists = []
    for line in input_generator(input):
        (x, y, z) = [int(n) for n in line.split(",")]
        points.append(Vec3d(x, y, z))

    for i, p in enumerate(points):
        for j, q in enumerate(points[i + 1 :]):
            diff = p - q
            dists.append((diff.dot(diff), i, j + i + 1))
            # print(diff.dot(diff),p,q,i,j)

    dists.sort(key=lambda x: x[0])
    dists = dists[:junctions]
    print("best")
    for d in dists:
        print(d[0], d[1], d[2], points[d[1]], points[d[2]])
    connections = defaultdict(list)
    for d in dists:
        (_, i, j) = d
        connections[i].append(j)
        connections[j].append(i)

    print(connections)

    done = set()
    counts = []
    for i in range(len(points)):
        if i in done:
            continue
        queue = [i]
        count = 0
        print("start", i)
        while queue:
            p = queue.pop()
            if p in done:
                continue
            print("add", p)
            count += 1
            done.add(p)
            queue += connections[p]
        print("count", count)
        counts.append(count)
    counts.sort(reverse=True)
    result = counts[0] * counts[1] * counts[2]
    return result


def top(links, i):
    if links[i] == None:
        return i
    else:
        return top(links, links[i])


def part_b(input, junctions=1000):
    points = []
    dists = []
    for line in input_generator(input):
        (x, y, z) = [int(n) for n in line.split(",")]
        points.append(Vec3d(x, y, z))

    for i, p in enumerate(points):
        for j, q in enumerate(points[i + 1 :]):
            diff = p - q
            dists.append((diff.dot(diff), i, j + i + 1))
            # print(diff.dot(diff),p,q,i,j)

    dists.sort(key=lambda x: x[0])

    links = [None for _ in range(len(points))]
    links_made = 0
    for d in dists:
        (_, i, j) = d

        top_i = top(links, i)
        top_j = top(links, j)

        if top_i != top_j:
            links[top_i] = top_j
            print("link3", top_i, top_j)
            links_made += 1
            print("linking", i, j, links_made)
            if links_made == len(points) - 1:
                return points[i].x * points[j].x


def notes():
    """
    Part a done, although not in the cleanest way. We ought to bucket together distances
    for efficiency (although it's taking only 0.7s for the sort)

    Same for part b
    """


if __name__ == "__main__":
    Run_2025_08().run_cmdline()
