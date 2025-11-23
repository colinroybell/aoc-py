from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from queue import PriorityQueue


class Run_2025_15(DayBase):
    YEAR = "2025"
    DAY = "15"
    PREFIX = "ec"


def dir_right(dir):
    return {"R": "D", "D": "L", "L": "U", "U": "R"}[dir]


def dir_left(dir):
    return {"R": "U", "D": "R", "L": "D", "U": "L"}[dir]


# TODO: tidy up a bit
# Algorithm: we must link up the insides of corners. Detect those, and then
# perform a ray-trace from each to see how far we can reach. We can then
# easily see if we can get from one point of interest to the next
#
# Needs tidying up, and the ray-trace should be reduced by 1 at each stage
# (otherwise we could go through/along a wall). But this case doesn't break
# our input.


def part_1(input):
    line = next(input_generator(input))
    instructions = line.split(",")
    points = []
    pos = Vec2d(0, 0)
    points.append(pos)
    lines = []
    rays = {}
    first = True
    dir = "U"

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for inst in instructions:
        rotate = inst[0]
        count = int(inst[1:])
        if not first:
            if dir == "U" and rotate == "R" or dir == "L" and rotate == "L":
                points.append(pos + Vec2d(-1, 1))
            if dir == "U" and rotate == "L" or dir == "R" and rotate == "R":
                points.append(pos + Vec2d(1, 1))
            if dir == "D" and rotate == "R" or dir == "R" and rotate == "L":
                points.append(pos + Vec2d(-1, -1))
            if dir == "D" and rotate == "L" or dir == "L" and rotate == "R":
                points.append(pos + Vec2d(1, -1))
        else:
            first = False
        if rotate == "R":
            dir = dir_right(dir)
        else:
            dir = dir_left(dir)
        newpos = pos.move(dir, count)
        lines.append([pos, newpos])
        pos = newpos
        min_x = min(min_x, pos.x)
        max_x = max(max_x, pos.x)
        min_y = min(min_y, pos.y)
        max_y = max(max_y, pos.y)

    end_pos = pos
    points.append(end_pos)
    print(points)
    min_x -= 1
    max_x += 1
    min_y -= 1
    max_y += 1
    for p in points:
        rays[p] = {}
        rays[p]["R"] = max_x
        rays[p]["L"] = min_x
        rays[p]["U"] = max_y
        rays[p]["D"] = min_y
    for line in lines:
        print("line", line)
        if line[0].x == line[1].x:
            # vertical
            x = line[0].x
            y0 = min(line[0].y, line[1].y)
            y1 = max(line[0].y, line[1].y)
            for p in points:
                if y0 <= p.y <= y1:
                    if x > p.x and x < rays[p]["R"]:
                        rays[p]["R"] = x
                        print(p, "R", x)
                    if x < p.x and x > rays[p]["L"]:
                        rays[p]["L"] = x
                        print(p, "L", x)
                    if x == p.x and y0 >= p.y and y0 < rays[p]["U"]:
                        rays[p]["U"] = y0
                    if x == p.x and y1 <= p.y and y0 > rays[p]["D"]:
                        rays[p]["D"] = y1

        else:
            # horizontal
            y = line[0].y
            x0 = min(line[0].x, line[1].x)
            x1 = max(line[0].x, line[1].x)
            for p in points:
                if x0 <= p.x <= x1:
                    if y > p.y and y < rays[p]["U"]:
                        rays[p]["U"] = y
                    if y < p.y and y > rays[p]["D"]:
                        rays[p]["D"] = y
                    if y == p.y and x0 >= p.x and x0 < rays[p]["R"]:
                        rays[p]["R"] = x0
                    if y == p.y and x1 <= p.x and x0 > rays[p]["L"]:
                        rays[p]["L"] = x1

    print(rays[Vec2d(0, 0)])
    found = set()
    queue = PriorityQueue()
    queue.put((0, Vec2d(0, 0)))
    while not queue.empty():
        (d, pos) = queue.get()
        print(d, pos)
        if pos in found:
            continue
        if pos == end_pos:
            return d
        found.add(pos)
        x0 = pos.x
        y0 = pos.y
        for p in points:
            if p not in found:
                x1 = p.x
                y1 = p.y
                if (
                    rays[pos]["L"] <= x1 <= rays[pos]["R"]
                    and rays[p]["D"] <= y0 <= rays[p]["U"]
                ) or (
                    rays[pos]["D"] <= y1 <= rays[pos]["U"]
                    and rays[p]["L"] <= x0 <= rays[p]["R"]
                ):
                    # Can get to this point in two straight lines
                    dd = pos.manhattan(p)
                    queue.put((d + dd, p))
                    print("Appending", d + dd, p)


def part_2(input):
    return part_1(input)


# Think the idea is that you have to either go in straight lines or round the edges
# Probably what we need to do is create a path that hugs the edge and then incrementally optimise by cutting off bits?


def part_3(input):
    return part_1(input)


if __name__ == "__main__":
    Run_2025_15().run_cmdline()
