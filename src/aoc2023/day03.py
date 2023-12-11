from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d
from math import prod


class Run_2023_03(DayBase):
    YEAR='2023'
    DAY='03'


# Note: horribly hacky in places. Best solution would be to put a ring of . around the grid, and combine a and b logic in a nicer way.


def test_grid_a(grid, x, y):
    (min_x, min_y, max_x, max_y) = grid.get_dimensions()
    if min_x <= x < max_x and min_y <= y < max_y:
        char = grid.get(Vec2d(x,y))
        if not char.isdigit() and char != '.':
          return True
    return False

def adjacent_a(grid, row, start_col, end_col):
    if test_grid_a(grid, start_col - 1, row):
        return True
    if test_grid_a(grid, end_col + 1, row):
        return True
    for row_delta in [-1, 1]:
        for col in range(start_col - 1 , end_col + 2):
            if test_grid_a(grid, col, row + row_delta):
                return True
    return False

def test_grid_b(grid, x, y):
    (min_x, min_y, max_x, max_y) = grid.get_dimensions()
    if min_x <= x < max_x and min_y <= y < max_y:
        char = grid.get(Vec2d(x,y))
        if char == '*':
          return Vec2d(x,y).tuple()
    return None

def adjacent_b(grid, row, start_col, end_col):
    v = test_grid_b(grid, start_col - 1, row)
    if v:
        return v
    v = test_grid_b(grid, end_col + 1, row)
    if v:
        return v
    for row_delta in [-1, 1]:
        for col in range(start_col - 1 , end_col + 2):
            v = test_grid_b(grid, col, row + row_delta)
            if v:
                return v
    return False

def part_a(input, part_b = False):
    part_a = not part_b
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings(input)
    total = 0
    adj_list = {}
    for row in range(height):
        value = 0
        in_schematic = False
        for col in range(width):


            char = grid.get(Vec2d(col,row))
            if char.isdigit():
                value = value * 10 + int(char)
                if not in_schematic:
                    start_col = col
                    in_schematic = True
            else:
                if in_schematic:
                    #print('testing',value)
                    if part_a:
                        if adjacent_a(grid,row, start_col, col-1):
                            total += value
                    else:
                        pos = adjacent_b(grid, row, start_col, col-1)
                        if pos:
                            if pos in adj_list:
                                adj_list[pos].append(value)
                            else:
                                adj_list[pos] = [value]

                    in_schematic = False
                    value = 0
        if in_schematic:
            if part_a:
                print(value)
                if adjacent_a(grid,row, start_col, col-1):
                    total += value
            else:
                pos = adjacent_b(grid, row, start_col, col-1)
                print(pos, value)
                if pos:
                    if pos in adj_list:
                        adj_list[pos].append(value)
                    else:
                        adj_list[pos] = [value]
    if part_b:
        for _, value_list in adj_list.items():
            if (len(value_list)==2):
                print(value_list)
                total += prod(value_list)

    return total


def part_b(input):
    return part_a(input, True)
if __name__ == "__main__":
    Run_2023_03().run_cmdline()
