from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_19(DayBase):
    YEAR = "2025"
    DAY = "19"
    PREFIX = "ec"


class Slit:
    def __init__(self, x, min_y, max_y):
        self.x = x
        self.min_y = min_y
        self.max_y = max_y

    def project(self, other):
        w = other.x - self.x
        max_y = self.max_y + w
        min_y = self.min_y - w

        new_max_y = min(max_y, other.max_y)
        if (new_max_y - other.x) % 2:
            new_max_y -= 1
        new_min_y = max(min_y, other.min_y)
        if (new_min_y - other.x) % 2:
            new_min_y += 1
        if new_min_y <= new_max_y:
            return Slit(other.x, new_min_y, new_max_y)
        else:
            return None

    def __repr__(self):
        return "slit ({}:{},{})".format(self.x, self.min_y, self.max_y)


class SlitList:
    def __init__(self):
        self.x = None
        self.ranges = []

    def try_add(self, slit):
        if self.x and slit.x != self.x:
            return False
        self.x = slit.x
        for i in range(len(self.ranges)):
            if slit.max_y < self.ranges[i][0]:
                self.ranges = (
                    self.ranges[:i] + [[slit.min_y, slit.max_y]] + self.ranges[i:]
                )
                return True
            if slit.max_y >= self.ranges[i][0] and slit.min_y <= self.ranges[i][1]:
                # Combine
                self.ranges[i][0] = min(self.ranges[i][0], slit.min_y)
                self.ranges[i][1] = max(self.ranges[i][1], slit.max_y)
                while (
                    i < len(self.ranges) - 1
                    and self.ranges[i][1] >= self.ranges[i + 1][0]
                ):
                    # Combine with the next one up
                    self.ranges[i][1] = self.ranges[i + 1][i]
                    self.ranges = self.ranges[: i + 1] + self.ranges[i + 2 :]
                return True
        # Add to end
        self.ranges.append([slit.min_y, slit.max_y])
        return True

    def project(self, other):
        project = SlitList()
        for i in range(len(self.ranges)):
            for j in range(len(other.ranges)):
                project_slit = Slit(
                    self.x, self.ranges[i][0], self.ranges[i][1]
                ).project(Slit(other.x, other.ranges[i][0], other.ranges[i][1]))
                if project_slit:
                    project.try_add(project_slit)
        return project

    def get_min_y(self):
        return self.ranges[0][0]

    def __repr__(self):
        return "{} {}".format(self.x, self.ranges)


def part_1(input):
    current = Slit(0, 0, 0)
    for line in input_generator(input):
        (slit_x, slit_base, slit_size) = [int(n) for n in line.split(",")]
        slit_min = slit_base
        slit_max = slit_base + slit_size - 1
        other = Slit(slit_x, slit_min, slit_max)
        project = current.project(other)
        current = project
    return (current.x + current.min_y) // 2


def part_2(input):
    current = SlitList()
    assert current.try_add(Slit(0, 0, 0))
    other = SlitList()
    for line in input_generator(input):
        (slit_x, slit_base, slit_size) = [int(n) for n in line.split(",")]
        slit = Slit(slit_x, slit_base, slit_base + slit_size - 1)
        if other.try_add(slit):
            continue
        current = current.project(other)
        other = SlitList()
        other.try_add(slit)
    current = current.project(other)
    return (current.x + current.get_min_y()) // 2


def part_3(input):
    return part_2(input)


def notes():
    """
    Reasonably efficient. Refactor range list out into a utility.

    Ought to write Slit and SlitList in the same way (0,1 for both)
    """


if __name__ == "__main__":
    Run_2025_19().run_cmdline()
