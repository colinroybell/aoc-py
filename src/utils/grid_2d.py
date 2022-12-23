from utils.vec_2d import Vec2d
from collections import defaultdict
from utils.data_input import input_generator


class Grid2d:
    def __init__(self, unset=0):
        self.c = defaultdict(lambda: unset)

    def read_from_file(self, input):
        y = 0
        for line in input_generator(input):
            for x, v in enumerate(line):
                self.set(Vec2d(x, y), int(v))
                x += 1
            y += 1
        return (x, y)

    def read_from_file_strings(self, input):
        y = 0
        for line in input_generator(input):
            for x, v in enumerate(line):
                self.set(Vec2d(x, y), v)
                x += 1
            y += 1
        return (x, y)

    def read_from_generator(self, generator):
        y = 0
        for line in generator:
            if not line:
                break
            for x, v in enumerate(line):
                print(x, v)
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

    def unset(self, vec):
        del self.c[vec.tuple()]

    def get(self, vec):
        return self.c[vec.tuple()]

    def __repr__(self):
        string = ""
        for p, v in self.c.items():
            string += "{}, {} ".format(p, v)
        string = string[:-1]
        return string

    def __contains__(self, vec):
        return vec.tuple() in self.c

    def to_hash_dot(self, width, height, x_start=0, y_start=0):
        string = ""
        for y in range(x_start, height):
            for x in range(y_start, width):
                v = Vec2d(x, y)
                if self.get(v):
                    string += "#"
                else:
                    string += "."
            string += "\n"
        return string

    def to_string_as_characters(self, width, height, x_start=0, y_start=0):
        string = ""
        for y in range(x_start, height):
            for x in range(y_start, width):
                v = Vec2d(x, y)
                if self.get(v):
                    string += self.get(v)
                else:
                    string += " "
            string += "\n"
        return string

    def generator(self):
        for item in self.c.items():
            yield item