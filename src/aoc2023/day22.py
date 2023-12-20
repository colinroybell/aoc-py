from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_3d import Grid3d
from utils.vec_3d import Vec3d


class Run_2023_22(DayBase):
    YEAR = "2023"
    DAY = "22"


class Brick:
    def __init__(self, id, string, grid, bricks):
        self.id = id
        self.grid = grid
        self.bricks = bricks
        coords = string.split("~")
        c1 = [int(n) for n in coords[0].split(",")]
        c2 = [int(n) for n in coords[1].split(",")]
        self.base = Vec3d(c1[0], c1[1], c1[2])
        self.extent = Vec3d(c2[0] + 1, c2[1] + 1, c2[2] + 1) - self.base
        # print(self.base, self.extent)
        for x in range(self.extent.x):
            for y in range(self.extent.y):
                for z in range(self.extent.z):
                    self.grid.set(self.base + Vec3d(x, y, z), self.id)
                    # print("Setting ", self.base + Vec3d(x,y,z), "to ",self.id)
        self.supports = []
        self.supported_by = []
        self.round_moved = None
        self.safe = True

    def __repr__(self):
        return self.id

    def check_supports(self):
        self.supported_by = []
        for x in range(self.extent.x):
            for y in range(self.extent.y):
                id = self.grid.get(self.base + Vec3d(x, y, -1))
                if id and self.bricks[id] not in self.supported_by:
                    self.supported_by.append(self.bricks[id])
                    self.bricks[id].supports.append(self)

    def can_move(self, round, ignore=None):
        # On floor or already processed
        if self.base.z == 1 or self.round_moved == round:
            return (False, None)
        # print("can_move trying", self)
        for b in self.supported_by:
            if b.round_moved != round and b != ignore:
                # print("blocked by", self)
                return (False, None)
        # print("ok")
        self.round_moved = round
        return (True, self.supports)

    def move(self):
        assert self.supported_by == []
        for b in self.supports:
            b.supported_by.remove(self)
        self.supports = []
        for x in range(self.extent.x):
            for y in range(self.extent.y):
                for z in range(self.extent.z):
                    self.grid.unset(self.base + Vec3d(x, y, z))
        self.base.z -= 1
        for x in range(self.extent.x):
            for y in range(self.extent.y):
                for z in range(self.extent.z):
                    self.grid.set(self.base + Vec3d(x, y, z), self.id)

        self.check_supports()


def part_a(input, part_b=False):
    part_a = not part_b
    bricks = {}
    grid = Grid3d()
    count = 0
    for line in input_generator(input):
        if count <= 26:
            id = chr(65 + count)
        else:
            id = str(count)
        brick = Brick(id, line, grid, bricks)
        bricks[brick.id] = brick
        count += 1

    for b in bricks.values():
        b.check_supports()

    done = False
    round = 0
    can_move_list = []
    while not done:
        # print("Round ", round)
        queue = []
        for b in bricks.values():
            # print(b, b.supported_by)
            if b.supported_by == []:
                queue.append(b)
        can_move_list = []
        while queue:
            b = queue[0]
            queue = queue[1:]
            (can_move, new_bricks) = b.can_move(round)
            if can_move:
                assert b not in can_move_list, b
                can_move_list.append(b)
                queue.extend(new_bricks)
        done = True
        for b in can_move_list:
            # print(b.id," moves")
            b.move()
            done = False
        round += 1

    for b in bricks.values():
        if len(b.supported_by) == 1:
            b.supported_by[0].safe = False

    if part_a:
        safe_count = 0
        for b in bricks.values():
            if b.safe:
                safe_count += 1
        return safe_count
    else:
        score = 0
        for test_b in bricks.values():
            if not test_b.safe:
                # this is all copied from above - refactor
                # there is going to be a nice graph parsing way of doing this
                round = "B" + test_b.id
                can_move_list = []
                done = False
                while not done:
                    # print("Round ", round)
                    queue = []
                    for b in bricks.values():
                        # print(b, b.supported_by)
                        if b.supported_by == [test_b]:
                            queue.append(b)
                    can_move_list = []
                    while queue:
                        b = queue[0]
                        queue = queue[1:]
                        (can_move, new_bricks) = b.can_move(round, ignore=test_b)
                        if can_move:
                            assert b not in can_move_list, b
                            can_move_list.append(b)
                            queue.extend(new_bricks)
                    done = True
                    score += len(can_move_list)
                    # print(test_b, len(can_move_list),score)
        return score


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_22().run_cmdline()
