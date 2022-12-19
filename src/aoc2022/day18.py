from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_3d import Vec3d
from utils.grid_3d import Grid3d


class Run_2022_18(DayBase):
    YEAR = "2022"
    DAY = "18"


def part_a(input):
    cubes = []
    for line in input_generator(input):
        vals = line.split(",")
        ints = [int(val) for val in vals]
        p = Vec3d(ints[0], ints[1], ints[2])
        cubes.append(p)
    faces = 0
    for cube in cubes:
        for adj in Vec3d.adjacencies():
            c = cube + adj
            if c not in cubes:
                faces += 1
    return faces


def part_b(input):
    cubes = Grid3d()
    # States 1 is lava, 2 is to be considered, 3 is done
    max_d = 0
    for line in input_generator(input):
        vals = line.split(",")
        ints = [int(val) for val in vals]
        dims = max([abs(i) for i in ints])
        max_d = max(max_d, dims)
        p = Vec3d(ints[0], ints[1], ints[2])
        cubes.set(p, 1)
    max_d += 1
    for x in range(-max_d, max_d + 1):
        for y in range(-max_d, max_d + 1):
            for z in range(-max_d, max_d + 1):
                v = Vec3d(x, y, z)
                if not cubes.get(v):
                    cubes.set(v, 2)
                    print("set", v)
    stack = [Vec3d(max_d, max_d, max_d)]
    faces = 0
    while stack:
        v = stack.pop()
        if cubes.get(v) == 3:
            continue
        cubes.set(v, 3)
        for a in Vec3d.adjacencies():
            v_adj = v + a
            val = cubes.get(v_adj)
            if val == 1:
                faces += 1
            elif val == 2:
                stack.append(v_adj)
    return faces


if __name__ == "__main__":
    Run_2022_18().run_cmdline()
