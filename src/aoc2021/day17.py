from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
import re


class Run_2021_17(DayBase):
    YEAR = "2021"
    DAY = "17"


def part_a(input, part_b=False):
    line = next(input_generator(input))
    m = re.search(r"x=(\d+)..(\d+), y=(-\d+)..(-\d+)", line)
    assert m
    box_min = Vec2d(int(m.group(1)), int(m.group(3)))
    box_max = Vec2d(int(m.group(2)), int(m.group(4)))
    # max_height assumes box below starting position (i.e., we've reached max height before we get to the target area
    assert box_max.y < 0
    record = 0
    count = 0
    for vx in range(0, box_max.x + 1):
        total_x = (vx * (vx + 1)) // 2
        if total_x < box_min.x:
            # Won't reach the box
            continue
        vy = box_min.y
        done_vy = False
        for vy in range(box_min.y, -box_min.y):
            # Below minimum means we drop below box in one step.
            # Maximum: y values form a parabola and go from 0 to -(vy+1) in one go, so above this we will not hit the y value of the box.
            # We filter out cases where we go above the box completely and stop increasing vy. There will be an equivalent way of filtering out low vys but I haven't seen it.
            p = Vec2d(0, 0)
            v = Vec2d(vx, vy)
            max_height = 0
            done = False
            steps = 0
            while not done:
                steps += 1
                assert steps < 1000
                p = p + v
                v.y -= 1
                if v.x > 0:
                    v.x -= 1
                max_height = max(max_height, p.y)
                if p.in_box(box_min, box_max):
                    record = max(record, max_height)
                    done = True
                    count += 1
                elif p.x > box_max.x or p.y < box_min.y:
                    # We've gone past the box, or below the box
                    done = True
                    if p.y > box_max.y:
                        # We've overshot the box, so no point exploring larger vy
                        done_vy = True
            if done_vy:
                break
    if not part_b:
        return record
    else:
        return count


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_17().run_cmdline()
