from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2022_15(DayBase):
    YEAR = "2022"
    DAY = "15"


class RangeUnion:
    def __init__(self):
        self.ranges = []

    def append(self, new):
        new_ranges = []
        print("adding", new)
        for r in self.ranges:
            if r[1] < new[0] or r[0] > new[1]:
                # no union
                new_ranges.append((r[0], r[1]))
            else:
                new = (min(r[0], new[0]), max(r[1], new[1]))
        new_ranges.append(new)
        self.ranges = new_ranges
        print(self.ranges)

    def count(self):
        return sum([r[1] - r[0] for r in self.ranges])


def part_a(input, y=2000000):
    range_union = RangeUnion()
    y_beacons = set()
    match_re = re.compile(r".+?(\-?\d+).+?(\-?\d+).+?(\-?\d+).+?(\-?\d+)")
    for line in input_generator(input):
        m = match_re.match(line)
        assert m
        sx = int(m.group(1))
        sy = int(m.group(2))
        bx = int(m.group(3))
        by = int(m.group(4))
        if by == y:
            y_beacons.add(bx)
        range = abs(sx - bx) + abs(sy - by)

        y_range = range - abs(sy - y)
        print(sx, sy, bx, by, range, y_range)
        if y_range >= 0:
            range_union.append((sx - y_range, sx + y_range + 1))

    return range_union.count() - len(y_beacons)


def manhattan(x0, y0, x1, y1):
    return abs(x1 - x0) + abs(y1 - y0)


def edges(x, y, range):
    p0 = (x + range + 1, y)
    p1 = (x, y + range + 1)
    p2 = (x - range - 1, y)
    p3 = (x, y - range - 1)
    return [(p0, p1, False), (p1, p2, True), (p2, p3, False), (p3, p0, True)]


def edges_intersect(e1, e2):
    # can't be same angle
    if e1[2] == e2[2]:
        return None
    # and must be same parity
    if (e1[0][0] + e1[0][1] + e2[0][0] + e2[0][1]) % 2:
        return None
    # somewhat hacky intersection (ought to combine the two cases)
    if e1[2] == False:  # then edge has property that sum is constant
        sum = e1[0][0] + e1[0][1]
        d = (e2[0][0] + e2[0][1] - sum) // 2
        px = e2[0][0] - d
        py = e2[0][1] - d
        # check we actually intersect
        if (px - e2[0][0]) * (px - e2[1][0]) <= 0 and (px - e1[0][0]) * (
            px - e1[1][0]
        ) <= 0:
            return (px, py)
        else:
            return None
    else:
        sum = e2[0][0] + e2[0][1]
        d = (e1[0][0] + e1[0][1] - sum) // 2
        px = e1[0][0] - d
        py = e1[0][1] - d
        # check we actually intersect
        if (px - e2[0][0]) * (px - e2[1][0]) <= 0 and (px - e1[0][0]) * (
            px - e1[1][0]
        ) <= 0:
            return (px, py)
        else:
            return None


def part_b(input, max_coord=4000000):
    match_re = re.compile(r".+?(\-?\d+).+?(\-?\d+).+?(\-?\d+).+?(\-?\d+)")
    sensors = []
    for line in input_generator(input):
        m = match_re.match(line)
        assert m
        sx = int(m.group(1))
        sy = int(m.group(2))
        bx = int(m.group(3))
        by = int(m.group(4))
        range = manhattan(sx, sy, bx, by)
        e = edges(sx, sy, range)
        sensors.append((sx, sy, range, e))
        print(sx, sy, range)

    # Look for the one or two points which are just out of range
    for i, s1 in enumerate(sensors):
        for j, s2 in enumerate(sensors):
            if j >= i:
                break
            for e1 in s1[3]:
                for e2 in s2[3]:
                    p = edges_intersect(e1, e2)
                    if p:
                        (px, py) = p
                        print(i, j, p)
                        if 0 <= px <= max_coord and 0 <= py <= max_coord:
                            ok = True
                            for k, s3 in enumerate(sensors):
                                m = manhattan(s3[0], s3[1], px, py)
                                print(k, m)
                                if m <= s3[2]:
                                    print(
                                        "Failed on {}: {} {} {} d {}".format(
                                            k, s3[0], s3[1], s3[2], m
                                        )
                                    )
                                    ok = False
                                    # break
                            if ok:
                                return px * 4000000 + py

    assert 0


if __name__ == "__main__":
    Run_2022_15().run_cmdline()
