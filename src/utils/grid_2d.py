from utils.vec_2d import Vec2d
from collections import defaultdict
from utils.data_input import input_generator


class Grid2d:
    def __init__(self, unset=0):
        self.c = defaultdict(lambda: unset)

    def copy(self):
        new_grid = __init__()
        for p, v in self.c.items():
            new_grid.c[p] = v
        return new_grid

    def read_from_file(self, input):
        y = 0
        for line in input_generator(input):
            for x, v in enumerate(line):
                try:
                    self.set(Vec2d(x, y), int(v))
                except ValueError:
                    pass
                x += 1
            y += 1
        return (x, y)

    def read_from_hash_dot_file(self, input):
        y = 0
        for line in input_generator(input):
            for x, v in enumerate(line):
                if v == "#":
                    self.set(Vec2d(x, y), 1)
                x += 1
            y += 1
        return (x, y)

    def read_from_hash_dot_list(self, input):
        y = 0
        for line in input:
            for x, v in enumerate(line):
                if v == "#":
                    self.set(Vec2d(x, y), 1)
                x += 1
            y += 1
        return (x, y)

    def read_from_file_strings(self, input, stop_at_blank=True):
        y = 0
        max_x = 0
        for line in input_generator(input):
            if line == "" and stop_at_blank:
                break
            max_x = max(max_x, len(line))
            for x, v in enumerate(line):

                self.set(Vec2d(x, y), v)
                x += 1
            y += 1
        return (max_x, y)

    def read_from_file_strings_generator(self, generator, stop_at_blank=True):
        y = 0
        max_x = 0
        for line in generator:
            if line == "" and stop_at_blank:
                break
            max_x = max(max_x, len(line))
            for x, v in enumerate(line):

                self.set(Vec2d(x, y), v)
                x += 1
            y += 1
        return (max_x, y)

    def read_from_generator(self, generator):
        y = 0
        for line in generator:
            if not line:
                break
            for x, v in enumerate(line):
                if v == "#":
                    self.set(Vec2d(x, y), 1)
                x += 1
            y += 1
        return (x, y)

    def increment(self, vector):
        vec = vector.tuple()
        if vec not in self.c:
            self.c[vec] = 1
        else:
            self.c[vec] += 1
        # print(vec, self.c[vec])

    def count_function(self, function):
        count = 0
        for _, v in self.c.items():
            if function(v):
                count += 1
        return count

    def count_non_zero(self):
        def non_zero(v):
            return v != 0

        return self.count_function(non_zero)

    def sum(self):
        total = 0
        for _, v in self.c.items():
            total += v
            print(total, v)
        return total

    def set(self, vec, v):
        self.c[vec.tuple()] = v

    def append(self, vec, v):
        if vec.tuple() not in self.c:
            self.c[vec.tuple()] = []
        self.c[vec.tuple()].append(v)

    def unset(self, vec):
        del self.c[vec.tuple()]

    def get(self, vec):
        if vec.tuple() in self.c:
            return self.c[vec.tuple()]
        else:
            return None

    def __repr__(self):
        string = ""
        for p, v in self.c.items():
            string += "{}, {} ".format(p, v)
        string = string[:-1]
        return string

    def __contains__(self, vec):
        return vec.tuple() in self.c

    def get_dimensions(self):
        x_max = None
        x_min = None
        y_max = None
        y_min = None
        x = []
        y = []
        for pos, _ in self.generator():
            x.append(pos[0])
            y.append(pos[1])

        return (min(x), min(y), max(x) + 1, max(y) + 1)

    def to_hash_dot(self, width, height, x_start=0, y_start=0):
        string = ""
        for y in range(y_start, height):
            for x in range(x_start, width):
                v = Vec2d(x, y)
                if self.get(v):
                    string += "#"
                else:
                    string += "."
            string += "\n"
        return string

    def to_string_as_characters(self, width, height, x_start=0, y_start=0):
        string = ""
        for y in range(y_start, height):
            for x in range(x_start, width):
                v = Vec2d(x, y)
                if self.get(v):
                    string += self.get(v)
                else:
                    string += " "
            string += "\n"
        return string

    def generator(self):
        # TODO: we get a problem using this if we then want to read the grid for empty items (which changes the dictionary). A couple of fixes for this but need to think through this better.
        for item in self.c.items():
            yield item
