from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2021_25(DayBase):
    YEAR = "2021"
    DAY = "25"


def part_a(input):
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)

    # TODO: tidy up and make more efficient

    step = 0
    done = False
    while not done:
        print(step)
        # print(grid.to_string_as_characters(width, height))
        done = True
        step = step + 1
        for y in range(0, height):
            move_done = False
            can_move = [False] * width
            while not move_done:
                move_done = True
                for x in range(0, width):
                    this = grid.get(Vec2d(x, y))
                    right = grid.get(Vec2d((x + 1) % width, y))
                    if not can_move[x] and this == ">" and (right == "."):
                        can_move[x] = True
                        move_done = False
            for x in range(0, width):
                left = (x + width - 1) % width
                if can_move[x]:
                    grid.set(Vec2d(x, y), ".")
                if can_move[x - 1]:
                    grid.set(Vec2d(x, y), ">")
                    done = False
        for x in range(0, width):
            move_done = False
            can_move = [False] * height
            while not move_done:
                move_done = True
                for y in range(0, height):
                    this = grid.get(Vec2d(x, y))
                    right = grid.get(Vec2d(x, (y + 1) % height))
                    # print(x,y,this,right)
                    if not can_move[y] and this == "v" and (right == "."):
                        can_move[y] = True
                        move_done = False
            for y in range(0, height):
                left = (y + height - 1) % height
                if can_move[y]:
                    grid.set(Vec2d(x, y), ".")
                if can_move[y - 1]:
                    grid.set(Vec2d(x, y), "v")
                    done = False
    return step


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2021_25().run_cmdline()
