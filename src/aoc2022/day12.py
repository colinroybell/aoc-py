from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_2d import Vec2d
from utils.grid_2d import Grid2d


class Run_2022_12(DayBase):
    YEAR = "2022"
    DAY = "12"


# Implemented as given. Part b reverse of part a so could combine the two easily if we treat a as a descent.


def part_a(input):
    grid = Grid2d()
    grid.read_from_file_strings(input)
    start_pos = [pos for pos, height in grid.generator() if height == "S"][0]
    start_pos = Vec2d(start_pos[0], start_pos[1])
    count_grid = Grid2d()
    count_grid.set(start_pos, 0)
    grid.set(start_pos, "a")

    queue = [(start_pos, 0)]

    while 1:
        pos, count = queue.pop(0)

        adjs = pos.get_adjacent_orthogonal()
        this_height = grid.get(pos)
        print(pos, count, this_height)
        for adj in adjs:
            height = grid.get(adj)
            print("Try", adj, count_grid.get(adj), height, this_height)
            if height == "E":
                if ord(this_height) >= ord("y"):
                    return count + 1
            elif (
                count_grid.get(adj) == None
                and height != None
                and ord(height) - ord(this_height) <= 1
            ):
                print("Yes")
                count_grid.set(adj, count + 1)
                queue.append((adj, count + 1))


def part_b(input):
    grid = Grid2d()
    grid.read_from_file_strings(input)
    start_pos = [pos for pos, height in grid.generator() if height == "E"][0]
    start_pos = Vec2d(start_pos[0], start_pos[1])
    count_grid = Grid2d()
    count_grid.set(start_pos, 0)
    grid.set(start_pos, "z")

    queue = [(start_pos, 0)]

    while 1:
        pos, count = queue.pop(0)

        adjs = pos.get_adjacent_orthogonal()
        this_height = grid.get(pos)
        print(pos, count, this_height)
        for adj in adjs:
            height = grid.get(adj)
            print("Try", adj, count_grid.get(adj), height, this_height)
            if height == "E" or height == "a":
                if ord(this_height) <= ord("b"):
                    return count + 1
            elif (
                count_grid.get(adj) == None
                and height != None
                and ord(height) - ord(this_height) >= -1
            ):
                print("Yes")
                count_grid.set(adj, count + 1)
                queue.append((adj, count + 1))


if __name__ == "__main__":
    Run_2022_12().run_cmdline()
