from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_19(DayBase):
    YEAR = "2024"
    DAY = "19"
    PREFIX = "ec"


def part_1(input):
    generator = input_generator(input)
    inst = next(generator)
    _ = next(generator)
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings_generator(generator)
    adjs = [
        Vec2d(1, 0),
        Vec2d(1, 1),
        Vec2d(0, 1),
        Vec2d(-1, 1),
        Vec2d(-1, 0),
        Vec2d(-1, -1),
        Vec2d(0, -1),
        Vec2d(1, -1),
    ]
    count = 0
    print(grid.to_string_as_characters(width, height))
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            base = Vec2d(x, y)
            dir = inst[count % len(inst)]
            input = []
            for a in adjs:
                adj = base + a
                input.append(grid.get(adj))
            for i, a in enumerate(adjs):
                adj = base + a
                if dir == "R":
                    grid.set(adj, input[(i - 1) % 8])
                else:
                    grid.set(adj, input[(i + 1) % 8])
            count += 1
            print(grid.to_string_as_characters(width, height))
    message = ""
    for x in range(1, width - 1):
        message += grid.get(Vec2d(x, 1))
    return message


class Permutation:
    def __init__(self, grid, width, height):
        self.grid = grid
        self.width = width
        self.height = height

    def add(self, other):
        new_grid = Grid2d()
        for y in range(self.height):
            for x in range(self.width):
                new_grid.set(Vec2d(x, y), other.grid.get(self.grid.get(Vec2d(x, y))))
        return Permutation(new_grid, self.width, self.height)

    def mul(self, factor):
        p = self.add(self)
        for _ in range(factor - 2):
            p = p.add(self)
        return p

    def apply(self, grid):
        output = Grid2d()
        for y in range(self.height):
            for x in range(self.width):
                output.set(Vec2d(x, y), grid.get(self.grid.get(Vec2d(x, y))))
        return output


def part_2(input, part=2):
    generator = input_generator(input)
    inst = next(generator)
    _ = next(generator)
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings_generator(generator)
    adjs = [
        Vec2d(1, 0),
        Vec2d(1, 1),
        Vec2d(0, 1),
        Vec2d(-1, 1),
        Vec2d(-1, 0),
        Vec2d(-1, -1),
        Vec2d(0, -1),
        Vec2d(1, -1),
    ]

    perm_grid = Grid2d()
    for y in range(height):
        for x in range(width):
            perm_grid.set(Vec2d(x, y), Vec2d(x, y))
    print(perm_grid)
    count = 0
    for y in range(1, height - 1):
        print("y=", y)
        for x in range(1, width - 1):
            base = Vec2d(x, y)
            dir = inst[count % len(inst)]
            input = []
            for a in adjs:
                adj = base + a
                pos = perm_grid.get(adj)
                # print(adj,pos)
                input.append(perm_grid.get(adj))
            # print(base,input)
            for i, a in enumerate(adjs):
                adj = base + a
                if dir == "R":
                    perm_grid.set(adj, input[(i - 1) % 8])
                else:
                    perm_grid.set(adj, input[(i + 1) % 8])
            count += 1

    p = Permutation(perm_grid, width, height)
    if part == 2:
        p5 = p.mul(5)
        p10 = p5.mul(2)
        p20 = p10.mul(2)
        p100 = p20.mul(5)
        output = p100.apply(grid)
    else:
        for r in range(23):
            print(r)
            p = p.mul(2)
        for _ in range(3):
            p = p.mul(5)
        output = p.apply(grid)
    print(output.to_string_as_characters(width, height))
    message = ""
    in_message = False
    for y in range(0, height):
        for x in range(0, width):
            c = output.get(Vec2d(x, y))
            if c == ">":
                in_message = True
            elif c == "<":
                in_message = False
            elif in_message:
                message += c

    return message


def part_3(input):
    return part_2(input, part=3)


if __name__ == "__main__":
    Run_2024_19().run_cmdline()
