from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_12(DayBase):
    YEAR = "2024"
    DAY = "12"


def perimeter_score(boundaries: set):
    count = 0
    while len(boundaries):
        (pos, d) = boundaries.pop()
        count += 1
        if d in "UD":
            cand = "LR"
        else:
            cand = "UD"
        for c in cand:
            p = pos.move(c)
            n = (p, d)
            while n in boundaries:
                boundaries.remove(n)
                p = p.move(c)
                n = (p, d)
    return count


def part_a(input, part_b=False):
    grid = Grid2d()
    width, height = grid.read_from_file_strings(input)
    score = 0
    for y in range(height):
        for x in range(width):
            v = Vec2d(x, y)
            c = grid.get(v)
            if "*" not in c:
                area = 0
                perimeter = 0
                boundaries = set()
                cands = [v]
                done = c + "*"
                while cands:
                    v = cands[0]
                    cands.pop(0)
                    val = grid.get(v)
                    if val == c:
                        area += 1
                        for dir in "UDLR":
                            a = v.move(dir)
                            val_a = grid.get(a)
                            if val_a == c:
                                cands.append(a)
                            elif val_a == done:
                                pass
                            else:
                                perimeter += 1
                                boundaries.add((v, dir))
                        grid.set(v, done)
                    elif val == done:
                        pass
                    else:
                        assert 0
                if part_b:
                    perimeter = perimeter_score(boundaries)
                score += area * perimeter
    return score


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2024_12().run_cmdline()
