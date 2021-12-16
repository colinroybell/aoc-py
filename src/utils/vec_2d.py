class Vec2d:
    def __init__(self, pos):
        (self.x, self.y) = pos

    def tuple(self):
        return (self.x, self.y)

    def move(self, dir):
        if dir == "^":
            return Vec2d((self.x, self.y + 1))
        elif dir == ">":
            return Vec2d((self.x + 1, self.y))
        elif dir == "v":
            return Vec2d((self.x, self.y - 1))
        elif dir == "<":
            return Vec2d((self.x - 1, self.y))
        else:
            assert "Bad direction"

    def get_adjacent_diagonals(self):
        vecs = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x or y:
                    vecs.append(Vec2d((self.x + x, self.y + y)))
        return vecs

    def __add__(self, other):
        return Vec2d((self.x + other.x, self.y + other.y))

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
