from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2025_18(DayBase):
    YEAR = "2025"
    DAY = "18"
    PREFIX = "ec"


class Plant:
    def __init__(self, id, thickness):
        self.id = id
        self.thickness = thickness
        self.free_thickness = 0
        self.branch = []

    def add_free_thickness(self, thickness):
        self.free_thickness += thickness

    def add_branch(self, plant, thickness):
        self.branch.append((plant, thickness))

    def compute_energy(self, plants, multiplier):
        incoming = self.free_thickness * multiplier
        for (p, t) in self.branch:
            incoming += plants[p].energy * t

        if incoming >= self.thickness:
            self.energy = incoming
        else:
            self.energy = 0
        print("incoming", incoming)
        print("Energy", self.energy, " for plant", self.id)


def part_1(input, part=1):

    incoming = [None]
    thickness = [None]
    plant_energy = [None]

    plants = {}

    state = 1
    id = 1
    state_1_re = re.compile(r"Plant (\d+) with thickness (-?\d+):")
    state_2_free_re = re.compile(r"- free branch with thickness (-?\d+)")
    state_2_branch_re = re.compile(r"- branch to Plant (\d+) with thickness (-?\d+)")
    generator = input_generator(input, terminate_with_empty=(part == 1))
    for line in generator:
        print(line)
        if state == 1:
            if line == "" and part == 2:
                break
            match = state_1_re.match(line)
            assert match
            assert int(match.group(1)) == id
            thickness = int(match.group(2))
            plant = Plant(id, thickness)
            plants[id] = plant
            state += 1
        elif state == 2:
            m_free = state_2_free_re.match(line)
            m_branch = state_2_branch_re.match(line)
            if m_free:
                plant.add_free_thickness(int(m_free.group(1)))
            elif m_branch:

                branch_plant = int(m_branch.group(1))
                branch_thickness = int(m_branch.group(2))
                plant.add_branch(branch_plant, branch_thickness)
            else:
                id += 1
                state = 1
    last_id = id - 1

    if part == 1:
        for id in range(1, last_id + 1):
            plants[id].compute_energy(plants, 1)
        return plants[last_id].energy
    if part == 2:
        total = 0
        for line in generator:
            muls = [int(n) for n in line.split(" ")]
            for id in range(1, last_id + 1):
                mul = 0
                if muls:
                    mul = muls[0]
                    muls = muls[1:]
                plants[id].compute_energy(plants, mul)
            total += plants[last_id].energy
        return total


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2025_18().run_cmdline()
