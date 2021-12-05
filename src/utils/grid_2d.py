from utils.vec_2d import Vec2d
from collections import defaultdict


class Grid2d:
    def __init__(self):
        self.c = defaultdict(lambda: 0)

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
