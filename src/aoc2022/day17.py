from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2022_17(DayBase):
    YEAR = "2022"
    DAY = "17"


def part_a(input, part_b=False):
    part_a = not part_b
    if part_a:
        blocks = 2022
    else:
        blocks = 1000000000000
    wind = next(input_generator(input))
    grid = Grid2d()
    shapes = [
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]],
        [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]],
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [0, 1], [1, 1]],
    ]

    rock_max = 0
    wind_len = len(wind)
    wind_pos = 0
    wind_offs = {">": 1, "<": -1}
    wind_history = []
    height_history = []
    for count in range(blocks):
        print("count", count, rock_max)
        s = count % 5
        x_off = 2
        y_off = rock_max + 3
        # TODO: this is a hack. Things don't quite repeat at the beginning because of the floor, so we
        # need to assess things more accurately.
        for n in range(count - 5, 1000, -5):
            if wind_history[n] == wind_pos:
                print("Match {} with {}".format(count, n))
                rem_blocks = blocks - n
                cycles = rem_blocks // (count - n)
                offset = rem_blocks % (count - n)
                print(rem_blocks, cycles, offset, n + offset)
                print(height_history[n], height_history[n + offset], rock_max)
                return height_history[n + offset] + cycles * (
                    rock_max - height_history[n]
                )

        print("Start at", x_off, y_off)
        wind_history.append(wind_pos)
        height_history.append(rock_max)
        while 1:
            wind_off = wind_offs[wind[wind_pos]]
            wind_pos = (wind_pos + 1) % wind_len
            ok = True
            for b in shapes[s]:
                (x, y) = b
                new_x = x + x_off + wind_off
                new_y = y + y_off
                if new_x < 0 or new_x > 6 or grid.get(Vec2d(new_x, new_y)):
                    ok = False
                    break
            if ok:
                x_off += wind_off
                print("Blow to", wind_off, x_off, y_off)
            else:
                print("Wind blocked", wind_off)
            ok = True
            for b in shapes[s]:
                (x, y) = b
                new_x = x + x_off
                new_y = y + y_off - 1
                # print("Trying",new_x,new_y)
                if new_y < 0 or grid.get(Vec2d(new_x, new_y)):
                    ok = False
                    break
            if ok:
                y_off -= 1
                print("Drop to", x_off, y_off)
            else:
                print("Rest at", x_off, y_off)
                for b in shapes[s]:
                    (x, y) = b
                    grid.set(Vec2d(x + x_off, y + y_off), "#")
                    print("Setting", x + x_off, y + y_off)
                    rock_max = max(rock_max, y + y_off + 1)
                print("-" * 10)
                break

    return rock_max


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2022_17().run_cmdline()
