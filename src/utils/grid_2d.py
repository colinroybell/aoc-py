from utils.vec_2d import Vec2d
from collections import defaultdict


class Grid2d:
    def __init__(self, unset=0):
        self.c = defaultdict(lambda: unset)

    def increment(self, vector):
        vec = vector.tuple()
        if vec not in self.c:
            self.c[vec] = 1
        else:
            self.c[vec] += 1
        # print(vec, self.c[vec])

    def count_function(self, function):
        count = 0
        for p, v in self.c.items():
            if function(v):
                count += 1
        return count

    def count_non_zero(self):
        def non_zero(v):
            return v != 0

        return self.count_function(non_zero)

    def set(self, vec, v):
        self.c[vec.tuple()] = v

    def get(self, vec):
        return self.c[vec.tuple()]

    def __repr__(self):
        string = ""
        for p, v in self.c.items():
            string += "{}, {} ".format(p, v)
            if p == Vec2d((0, 0)):
                string += "yes "
        string = string[:-1]
        return string
