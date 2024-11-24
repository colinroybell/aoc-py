class Vec3d:
    def __init__(self, x, y, z):
        (self.x, self.y, self.z) = (x, y, z)

    def set(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z

    def tuple(self):
        return (self.x, self.y, self.z)

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __add__(self, other):
        return Vec3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3d(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, mul):
        return Vec3d(self.x * mul, self.y * mul, self.z * mul)

    def __truediv__(self, div):
        return Vec3d(self.x / div, self.y / div, self.z / div)

    def __repr__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __lt__(self, other):
        # Don't care
        return 0

    def adjacencies():
        return [
            Vec3d(1, 0, 0),
            Vec3d(-1, 0, 0),
            Vec3d(0, 1, 0),
            Vec3d(0, -1, 0),
            Vec3d(0, 0, 1),
            Vec3d(0, 0, -1),
        ]
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))