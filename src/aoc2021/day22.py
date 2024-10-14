from typing import Sized
from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_3d import Grid3d
from utils.vec_3d import Vec3d
import re
from random import randrange, seed


class Run_2021_22(DayBase):
    YEAR = "2021"
    DAY = "22"


# Near copy of 2015/06


def bound_to_50(xmin, xmax):
    if xmax < -50 or xmin > 50:
        return (0, -1)
    return max(xmin, -50), min(xmax, 50)


def part_a(input):
    parse_re = re.compile(
        r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
    )
    grid = Grid3d(0)
    for line in input_generator(input):
        m = parse_re.match(line)
        print(line)
        assert m
        cmd = m.group(1)
        xmin, xmax = bound_to_50(int(m.group(2)), int(m.group(3)))
        ymin, ymax = bound_to_50(int(m.group(4)), int(m.group(5)))
        zmin, zmax = bound_to_50(int(m.group(6)), int(m.group(7)))

        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                for z in range(zmin, zmax + 1):
                    p = Vec3d(x, y, z)

                    if cmd == "on":
                        grid.set(p, 1)
                    elif cmd == "off":
                        grid.set(p, 0)
        print("Now", grid.count_non_zero())

    return grid.count_non_zero()


def intersect(base, size, bound):
    # between [base,base+size) and [bound[0],bound[1]]
    if bound[1] < base or bound[0] >= base + size:
        return "no"
    if bound[0] <= base and bound[1] >= base + size - 1:
        return "yes"
    else:
        return "part"


class OcttreeNode:
    def __init__(self, base, size):
        self.base = base
        self.size = size
        self.state = "off"
        self.children = []

    def count(self):
        # print("count",self.base,self.size,self.state)
        if self.state == "off":
            return 0
        elif self.state == "on":
            # print("count on",self.base,self.size)
            return self.size[0] * self.size[1] * self.size[2]
        else:
            count = 0
            # print("count part",self.base,self.size)
            for child in self.children:
                count += child.count()
            return count

    def count_nodes(self):
        if self.state == "part":
            count = 0
            for child in self.children:
                count += child.count_nodes()
            return count
        return 1

    def split(self, base_state, axis, point):

        new_base_1 = self.base[:]
        new_size_1 = self.size[:]
        new_size_1[axis] = point - self.base[axis]

        new_base_2 = self.base[:]
        new_size_2 = self.size[:]
        new_base_2[axis] = point
        new_size_2[axis] = self.size[axis] - new_size_1[axis]

        child1 = OcttreeNode(new_base_1, new_size_1)
        child1.state = base_state
        self.children.append(child1)
        child2 = OcttreeNode(new_base_2, new_size_2)
        child2.state = base_state
        self.children.append(child2)

    def optimise(self):
        if self.state == "part":
            for c in self.children:
                c.optimise()
            first = self.children[0].state
            for c in self.children:
                if c.state == "part" or c.state != first:
                    return
            # print("optimising",self.base,self.size,"to",self.state)
            self.children = []
            self.state = first

    def command(self, cmd, bounds):
        intersects = [
            intersect(self.base[i], self.size[i], bounds[i]) for i in range(3)
        ]
        # print (self.base,self.size,":",cmd,bounds,intersects)
        if "no" in intersects:
            pass
        else:
            if "part" in intersects:
                split_axis = intersects.index("part")
                if not self.children:
                    if bounds[split_axis][0] > self.base[split_axis]:
                        point = bounds[split_axis][0]
                    else:
                        point = bounds[split_axis][1] + 1
                    self.split(self.state, split_axis, point)
                    self.state = "part"
                for child in self.children:
                    child.command(cmd, bounds)
                self.optimise()
            else:
                # print("setting",self.base,self.size,"to",cmd)
                self.state = cmd
                self.children = []

    def is_set(self, v):
        intersects = [
            (self.base[i] <= v[i] and v[i] <= self.base[i] + self.size[i] - 1)
            for i in range(3)
        ]

        if False in intersects:
            # print("is_set:", self.base,self.size,"out of bounds")
            return False
        else:
            # print("is_set: ",self.base,self.size,self.state)
            if self.state == "off":

                return False
            elif self.state == "on":
                return True
            else:
                for child in self.children:
                    if child.is_set(v):
                        return True
                return False


def part_b(input):
    parse_re = re.compile(
        r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
    )
    root = OcttreeNode(
        [-(2 ** 20), -(2 ** 20), -(2 ** 20)], [2 ** 21, 2 ** 21, 2 ** 21]
    )
    # root = OcttreeNode([-2**4,-2**4,-2**4],2**5)
    count = 0
    samples = []
    samples_expected = []
    seed(10)
    for k in range(0, 10):
        samples.append(
            [
                randrange(-100000, 100000),
                randrange(-100000, 100000),
                randrange(-100000, 100000),
            ]
        )
        samples_expected.append(False)
    print(samples)
    for line in input_generator(input):
        count += 1
        m = parse_re.match(line)
        print(line)
        assert m
        cmd = m.group(1)
        bounds = [
            [int(m.group(2)), int(m.group(3))],
            [int(m.group(4)), int(m.group(5))],
            [int(m.group(6)), int(m.group(7))],
        ]

        root.command(cmd, bounds)
        print("Now", root.count())
        print("Nodes", root.count_nodes())
        for i, s in enumerate(samples):
            if (
                bounds[0][0] <= s[0] <= bounds[0][1]
                and bounds[1][0] <= s[1] <= bounds[1][1]
                and bounds[2][0] <= s[2] <= bounds[2][1]
            ):
                print("Switching {}: {} {}".format(i, s, cmd))
                samples_expected[i] = cmd == "on"
            print("Expecting {} {} {}".format(i, s, samples_expected[i]))
            assert root.is_set(s) == samples_expected[i]
    return root.count()


if __name__ == "__main__":
    Run_2021_22().run_cmdline()
