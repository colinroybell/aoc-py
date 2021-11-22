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
        print(vec, self.c[vec])

    def count_non_zero(self):
        count = 0
        for p, v in self.c.items():
            if v:
                count += 1
        return count
