from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_3d import Vec3d
import re
from collections import defaultdict

ORIENTATIONS = 24


class Scanner:
    def __init__(self, id):
        self.position = None
        self.orientation = None
        self.id = id
        self.beacons = []

    def add_beacon(self, loc):
        self.beacons.append(loc)

    def transform(self, orientation, position):
        out = Scanner(self.id)
        out.position = position
        out.orientation = orientation
        out.beacons = []

        xyz_rot = orientation % 3
        yz_rot = (orientation // 3) % 2
        xy_flip = (orientation // 6) % 2
        xz_flip = (orientation // 12) % 2

        for i, b in enumerate(self.beacons):
            x, y, z = b.tuple()
            if xyz_rot == 1:
                x, y, z = y, z, x
            elif xyz_rot == 2:
                x, y, z = z, x, y
            if yz_rot:
                y, z = z, -y
            if xy_flip:
                x, y = -x, -y
            if xz_flip:
                x, z = -x, -z
            out.beacons.append(Vec3d(x, y, z) - position)
        return out

    def match(self, other):
        for orientation in range(ORIENTATIONS):
            trial = other.transform(orientation, Vec3d(0, 0, 0))
            diff_dict = defaultdict(lambda: 0)
            for b1 in self.beacons:
                for b2 in trial.beacons:
                    diff = b2 - b1
                    diff_dict[diff.tuple()] +=1 
                    if diff_dict[diff.tuple()] == 12:
                        # print("other beacons",other.beacons)
                        # print("trial beacons",trial.beacons)
                        # print("Found match", matches)
                        return (True, orientation, diff)
        return (False, None, None)

    @staticmethod
    def parse(input):
        scanners = []
        scanner = None
        scanner_re = re.compile(r"scanner (\d+)")
        for line in input_generator(input):
            m = scanner_re.search(line)
            if m:
                scanner = Scanner(int(m.group(1)))
                scanners.append(scanner)
            elif line:
                words = line.split(",")
                scanner.add_beacon(Vec3d(int(words[0]), int(words[1]), int(words[2])))
        return scanners


class Run_2021_19(DayBase):
    YEAR = "2021"
    DAY = "19"


def part_a(input, part_b=False):
    unknown_scanners = Scanner.parse(input)
    found_scanners = [unknown_scanners[0]]
    unknown_scanners = unknown_scanners[1:]
    done_scanners = []
    found_scanners[0].position = Vec3d(0, 0, 0)
    found_scanners[0].orientation = 0

    while found_scanners:
        source = found_scanners[0]
        found_scanners = found_scanners[1:]
        done_scanners.append(source)

        # print("Searching from",source.id)
        i = 0
        while i < len(unknown_scanners):
            dest = unknown_scanners[i]
            # print("Trying",dest.id)
            match, orientation, diff = source.match(dest)
            if match:
                # print("Match at {} {}".format(orientation,diff))
                found_scanners.append(dest.transform(orientation, diff))
                # print("New beacons:",found_scanners[-1].beacons)
                del unknown_scanners[i]
            else:
                i += 1

    assert not unknown_scanners

    if not part_b:
        found_beacons = set()
        for scanner in done_scanners:
            for beacon in scanner.beacons:
                found_beacons.add(beacon.tuple())

        return len(found_beacons)
    else:
        max_dist = 0
        for s1 in done_scanners:
            for s2 in done_scanners:
                max_dist = max(max_dist, s1.position.manhattan(s2.position))
        return max_dist


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_19().run_cmdline()
