from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2026_12(DayBase):
    YEAR = "2026"
    DAY = "12"
    PREFIX = "ec"


# TODO: part 1 and 2 work. part 3 doesn't. I've ended up with a hacky set of cases - sure there must be a better way to think about this.


def part_1(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    total = 0
    for y in range(height):
        for x in range(width):
            if grid.get(Vec2d(x, y)) == "#":
                w = 1
                while grid.get(Vec2d(x + w, y)) == "#":
                    w += 1
                h = 1
                while grid.get(Vec2d(x, y + h)) == "#":
                    h += 1
                total += min(w, h)
                for xx in range(w):
                    for yy in range(h):
                        grid.set(Vec2d(x + xx, y + yy), ".")
    return total


def num_missing(found, pos, dir):
    count = 0
    while 1:
        loc = pos + count * dir
        if loc in found:
            return count
        count += 1
    return count


def part_2(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    total = 0
    for y in range(height):
        for x in range(width):
            if grid.get(Vec2d(x, y)) == "#":
                min_x = max_x = x
                min_y = max_y = y
                queue = [Vec2d(x, y)]
                found = set()
                while queue:
                    pos = queue.pop()
                    if grid.get(pos) == "#":
                        grid.set(pos, ".")
                        found.add(pos)
                        min_x = min(min_x, pos.x)
                        max_x = max(max_x, pos.x)
                        min_y = min(min_y, pos.y)
                        max_y = max(max_y, pos.y)
                        queue.extend(pos.get_adjacent_orthogonal())
                w = max_x - min_x + 1
                h = max_y - min_y + 1
                print(x, y, min_x, max_x, min_y, max_y)
                single_dir_score = min(w, h)

                # Look for the missing corner and work out arm lengths of L. Could be generalised better.
                double_dir_score = single_dir_score

                case_found = False
                pos = Vec2d(min_x, min_y)
                if pos not in found:
                    y_arm = w - num_missing(found, pos, Vec2d(1, 0))
                    x_arm = h - num_missing(found, pos, Vec2d(0, 1))
                    double_dir_score = y_arm + x_arm
                    case_found = True
                pos = Vec2d(max_x, min_y)
                if pos not in found:
                    y_arm = w - num_missing(found, pos, Vec2d(-1, 0))
                    x_arm = h - num_missing(found, pos, Vec2d(0, 1))
                    double_dir_score = y_arm + x_arm
                    case_found = True
                pos = Vec2d(min_x, max_y)
                if pos not in found:
                    y_arm = w - num_missing(found, pos, Vec2d(1, 0))
                    x_arm = h - num_missing(found, pos, Vec2d(0, -1))
                    double_dir_score = y_arm + x_arm
                    case_found = True
                pos = Vec2d(max_x, max_y)
                if pos not in found:
                    y_arm = w - num_missing(found, pos, Vec2d(-1, 0))
                    x_arm = h - num_missing(found, pos, Vec2d(0, -1))
                    double_dir_score = y_arm + x_arm
                    case_found = True

                if not case_found and len(found) < w * h:
                    # case 3. We have a hole
                    part3_score = None
                    for yy in range(1, h):
                        for xx in range(1, w):
                            pos = Vec2d(min_x + xx, min_y + yy)
                            if pos not in found:
                                x_gap = num_missing(found, pos, Vec2d(1, 0))
                                y_gap = num_missing(found, pos, Vec2d(0, 1))
                                print("part3", w, x_gap, h, y_gap)
                                part3_score = min(
                                    w + h - x_gap - y_gap, w + x_gap, h + y_gap
                                )
                                print("score", part3_score)
                                break
                        if part3_score:
                            break
                    total += part3_score
                else:
                    total += min(single_dir_score, double_dir_score)
                print("total", total, single_dir_score, double_dir_score)
    return total


def part_3(input):
    return part_2(input)


if __name__ == "__main__":
    Run_2026_12().run_cmdline()
