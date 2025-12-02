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
        self.energy_options = []

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
        # print("incoming", incoming)
        # print("Energy", self.energy, " for plant", self.id)

    def compute_energy_options_recurse(self, plants, pos, last, state):
        (energy, on, off) = state
        if pos < 3:
            print("id, pos", self.id, pos)
        # print('in',pos,energy,on,off)
        if pos == len(self.branch):
            if energy >= self.thickness:
                return (energy, [(energy, on, off)])
            else:
                return (0, [])
        elif plants[self.branch[pos][0]].energy_options == []:
            return self.compute_energy_options_recurse(plants, pos + 1, last, state)
        else:

            this_plant = plants[self.branch[pos][0]]
            maximum = 0
            options = []
            # Put a no-options in here for the more advanced plants. Guaranteed to be ok - we will either get a match, or the real match is positive.
            if this_plant.free_thickness == 0:
                (maximum, options) = self.compute_energy_options_recurse(
                    plants, pos + 1, last, state
                )
                if not last:
                    options = ret
            for eo in this_plant.energy_options:
                (eo_energy, eo_on, eo_off) = eo
                # print('trying',eo,'with',on,off)
                if not on.intersection(eo_off) and not off.intersection(eo_on):
                    new_state = (
                        energy + eo_energy * self.branch[pos][1],
                        on.union(eo_on),
                        off.union(eo_off),
                    )
                    (this_maximum, this_options) = self.compute_energy_options_recurse(
                        plants, pos + 1, last, new_state
                    )

                    maximum = max(maximum, this_maximum)
                    if not last:
                        options = options + this_options

        return (maximum, options)

    def compute_energy_options(self, plants, last):
        if self.free_thickness:
            # On off for these plants
            self.energy_options = [
                (self.free_thickness, set([self.id]), set()),
                (0, set(), set([self.id])),
            ]
            return self.free_thickness
        else:
            state = (0, set(), set())
            (self.maximum, self.energy_options) = self.compute_energy_options_recurse(
                plants, 0, last, state
            )
            if last:
                assert self.maximum >= self.thickness
                return self.maximum
            else:
                return self.energy_options


def part_1(input, part=1):

    incoming = [None]
    thickness = [None]
    plant_energy = [None]

    plants = {}

    state = 1
    id = 1
    # This is a long and long and long and long  and long and long and long  and long and long and long  and long and long and long  and long and long and long  and long and long and long  and long and long and long  and long and long and long comment
    state_1_re = re.compile(r"Plant (\d+) with thickness (-?\d+):")
    state_2_free_re = re.compile(r"- free branch with thickness (-?\d+)")
    state_2_branch_re = re.compile(r"- branch to Plant (\d+) with thickness (-?\d+)")
    generator = input_generator(input, terminate_with_empty=(part == 1))
    for line in generator:
        print(line)
        if state == 1:
            if line == "" and part > 1:
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
    if part == 3:
        for id in range(1, last_id + 1):
            maximum = plants[id].compute_energy_options(plants, id == last_id)
            print(plants[id].energy_options)
        print(maximum)
        total = 0
        for line in generator:
            muls = [int(n) for n in line.split(" ")]
            for id in range(1, last_id + 1):
                mul = 0
                if muls:
                    mul = muls[0]
                    muls = muls[1:]
                plants[id].compute_energy(plants, mul)
            last_energy = plants[last_id].energy
            if last_energy:
                total += maximum - last_energy
        return total


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


def notes():
    """
    What we have I think works but run-time very slow. Need to do some culling to get the maximum.
    Then track potential maximum left from later plants and we don't need to go down the list if we can't reach the known maximum.
    """


if __name__ == "__main__":
    Run_2025_18().run_cmdline()
