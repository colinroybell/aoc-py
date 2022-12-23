from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from utils.grid_2d import Grid2d


class Run_2022_08(DayBase):
    YEAR = "2022"
    DAY = "08"


def part_a(input):
    grid = Grid2d()
    grid.read_from_file(input)
    count = 0
    for base_pos, height in grid.generator():
        visible = False
        for dir in "^>v<":
            pos = Vec2d.from_tuple(base_pos)
            while 1:
                pos = pos.move(dir)
                if pos not in grid:
                    visible = True
                    break
                elif grid.get(pos) >= height:
                    visible = False
                    break
            if visible:
                break
        if visible:
            count+= 1
    return count



def part_b(input):
    grid = Grid2d()
    grid.read_from_file(input)
    best = 0
    for base_pos, height in grid.generator():
        score = 1
        for dir in "^>v<":
            pos = Vec2d.from_tuple(base_pos)
            visible = 0
            while 1:
                visible += 1
                pos = pos.move(dir)
                if pos not in grid:
                    visible -= 1
                    break
                elif grid.get(pos) >= height:
                    break
            score *= visible
        best = max(best,score)
    return best

if __name__ == "__main__":
    Run_2022_08().run_cmdline()
