from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_09(DayBase):
    YEAR = "2025"
    DAY = "09"


def part_a(input):
    corners = [[int(n) for n in line.split(",")] for line in input_generator(input)]
    best = 0
    for c0 in corners:
        for c1 in corners:
            score = abs((c0[0] - c1[0] + 1) * (c0[1] - c1[1] + 1))
            best = max(score, best)
    return best


def part_b(input):
    corners = [[int(n) for n in line.split(",")] for line in input_generator(input)]
    hlines = []
    vlines = []
    count = len(corners)
    for i in range(count):
        (x0, y0) = corners[i]
        (x1, y1) = corners[(i + 1) % count]
        if x0 == x1:
            vlines.append(x0, min(y0, y1), max(y0, y1))
        else:
            hlines.append(y0, min(x0, x1), max(x0, x1))

    hlines.sort(key=lambda n: n[0])
    vlines.sort(key=lambda n: n[0])

    for i in range(count):
        (x, y) = corners[i]
        (xp, yp) = corners[(i - 1) % count]
        (xn, yn) = corners[(i + 1) % count]

        # Assume clockwise on picture, then right is inside
        # We can work this out by projecting a point from p0 to the outside
        if (y == yp and xp < x and x == xn and yn > y) or (
            x == xp and yp < y and y == yn and xn < x
        ):  # or flip this if not found to be clockwise
            vpos = 0

            # Search through rightwards vlines to find one that is right of us and intersects us. This gives us the max x we are looking at. If it matches our y we have a point to consider.

            while vlines[pos] < y:
                pos += 1
            for dir in [-1, 1]:
                pass
                # In each direction we are looking for one which is right of us, and has a minimum less or equal than the current max. This gives us a candidate.
                # Or we find one which intersects our x. in which case we stop. Again an exact match gives us a point to consider.


if __name__ == "__main__":
    Run_2025_09().run_cmdline()
