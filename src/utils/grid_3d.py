from utils.vec_3d import Vec3d
from collections import defaultdict
from utils.data_input import input_generator

# TODO: Combine with Grid3d to make a generic grid class


class Grid3d:
    def __init__(self, unset=0):
        self.c = defaultdict(lambda: unset)

    def increment(self, vector):
        vec = vector.tuple()
        if vec not in self.c:
            self.c[vec] = 1
        else:
            self.c[vec] += 1

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

    def count_non_zero_range_50(self):
        count = 0
        for vec, v in self.c.items():
            coords = list[vec.tuple()]
            d = max([abs(c) for c in coords])
            if d <= 50 and v:
                count += 1
        return count

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
