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

    def __add__(self, other):
        return Vec2d((self.x + other.x, self.y + other.y))
