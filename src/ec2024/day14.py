from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_3d import Vec3d
from queue import PriorityQueue


class Run_2024_14(DayBase):
    YEAR = "2024"
    DAY = "14"
    PREFIX = "ec"


def part_1(input):
    dirs = {
        "L": Vec3d(-1, 0, 0),
        "R": Vec3d(1, 0, 0),
        "U": Vec3d(0, 1, 0),
        "D": Vec3d(0, -1, 0),
        "F": Vec3d(0, 0, 1),
        "B": Vec3d(0, 0, -1),
    }

    line = next(input_generator(input))
    pos = Vec3d(0, 0, 0)
    max_height = 0
    moves = line.split(",")
    for m in moves:
        dir = m[0]
        count = int(m[1:])
        delta = dirs[dir] * count
        pos += delta
        if pos.y > max_height:
            max_height = pos.y
    return max_height


def part_2(input):
    dirs = {
        "L": Vec3d(-1, 0, 0),
        "R": Vec3d(1, 0, 0),
        "U": Vec3d(0, 1, 0),
        "D": Vec3d(0, -1, 0),
        "F": Vec3d(0, 0, 1),
        "B": Vec3d(0, 0, -1),
    }

    segments = set()

    for line in input_generator(input):
        pos = Vec3d(0, 0, 0)
        moves = line.split(",")
        for m in moves:
            dir = m[0]
            count = int(m[1:])
            for _ in range(count):
                delta = dirs[dir]
                pos += delta
                segments.add(pos)

    return len(segments)


def part_3(input):
    dirs = {
        "L": Vec3d(-1, 0, 0),
        "R": Vec3d(1, 0, 0),
        "U": Vec3d(0, 1, 0),
        "D": Vec3d(0, -1, 0),
        "F": Vec3d(0, 0, 1),
        "B": Vec3d(0, 0, -1),
    }

    trunk = set()
    leaves = set()
    segments = set()

    for line in input_generator(input):
        pos = Vec3d(0, 0, 0)
        moves = line.split(",")
        for m in moves:
            dir = m[0]
            count = int(m[1:])
            for _ in range(count):
                delta = dirs[dir]
                pos += delta
                segments.add(pos)
                if pos.x == 0 and pos.z == 0:
                    trunk.add(pos)

        leaves.add(pos)

    best = None
    adj = Vec3d.adjacencies()
    for pos in trunk:
        score = 0
        found = set()
        queue = PriorityQueue()
        queue.put((0, pos))
        while not queue.empty():
            (d, pos) = queue.get()
            if pos in found:
                continue
            found.add(pos)
            if pos in leaves:
                score += d
            for delta in adj:
                new_pos = pos + delta
                if new_pos in segments and new_pos not in found:
                    queue.put((d + 1, new_pos))
        if best == None or score < best:
            best = score
    return best


if __name__ == "__main__":
    Run_2024_14().run_cmdline()
