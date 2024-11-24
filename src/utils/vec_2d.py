class Vec2d:
    def __init__(self, x, y):
        (self.x, self.y) = (x, y)

    # These two may not need using
    def tuple(self):
        return (self.x, self.y)

    def from_tuple(value):
        return Vec2d(value[0], value[1])

    def move(self, dir):
        if dir == "^" or dir == "U":
            return Vec2d(self.x, self.y + 1)
        elif dir == ">" or dir == "R":
            return Vec2d(self.x + 1, self.y)
        elif dir == "v" or dir == "D":
            return Vec2d(self.x, self.y - 1)
        elif dir == "<" or dir == "L":
            return Vec2d(self.x - 1, self.y)
        elif dir == ".":
            return Vec2d(self.x, self.y)
        else:
            assert "Bad direction"

    def move_y_flipped(self, dir):
        if dir == "^" or dir == "U":
            return Vec2d(self.x, self.y - 1)
        elif dir == ">" or dir == "R":
            return Vec2d(self.x + 1, self.y)
        elif dir == "v" or dir == "D":
            return Vec2d(self.x, self.y + 1)
        elif dir == "<" or dir == "L":
            return Vec2d(self.x - 1, self.y)
        elif dir == ".":
            return Vec2d(self.x, self.y)
        else:
            assert "Bad direction"

    def get_adjacent_diagonals(self):
        vecs = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x or y:
                    vecs.append(Vec2d(self.x + x, self.y + y))
        return vecs

    def get_adjacent_orthogonal(self):
        vecs = []
        for d in "^>v<":
            vecs.append(self.move(d))
        return vecs

    def in_box(self, box_min, box_max):
        return box_min.x <= self.x <= box_max.x and box_min.y <= self.y <= box_max.y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __mul__(self, mul):
        return Vec2d(self.x * mul, self.y * mul)

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __hash__(self):
        return hash((self.x,self.y))