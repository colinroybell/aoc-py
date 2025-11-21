from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_11(DayBase):
    YEAR = "2025"
    DAY = "11"
    PREFIX = "ec"


def part_1(input, rounds=10, return_ducks=False):
    ducks = [int(n) for n in input_generator(input)]
    columns = len(ducks)
    phase = 1
    r = 0
    while r < rounds and phase < 3:
        r += 1
        change = False
        for i in range(columns - 1):
            if phase == 1:
                if ducks[i] > ducks[i + 1]:
                    change = True
                    ducks[i] -= 1
                    ducks[i + 1] += 1
            else:
                if ducks[i] < ducks[i + 1]:
                    change = True
                    ducks[i] += 1
                    ducks[i + 1] -= 1
        if not change:
            phase += 1
            r -= 1  # Doesn't count as a round if we do nothing
    if not return_ducks:
        checksum = sum([(c + 1) * ducks[c] for c in range(columns)])
        print(ducks, phase, checksum)
        return checksum
    else:
        return ducks


class Duckset:
    def __init__(self, count, dir):
        self.count = count
        self.columns = 1
        self.dir = dir

    def __repr__(self):
        return "[count {} columns {} dir {}]".format(self.count, self.columns, self.dir)

    def combine(self, other):
        self.count += other.count
        self.columns += other.columns

    def catch_up(self, other):
        """how many steps until we can merge"""
        if self.dir == -1 and other.dir == 0:
            other_base = other.count // other.columns
            # Need to reduce to a point where one of our numbers is other_base
            required_count = other_base * self.columns + (self.columns - 1)
            return self.count - required_count
        elif self.dir == 1 and other.dir == 0:
            other_base = other.count // other.columns
            # Need to increase to a point where one of our numbers is other_base
            required_count = other_base * self.columns + 1
            return required_count - self.count
        elif self.dir == 0 and other.dir == 1:
            # Need other to increase where all of their numbers is self_base
            self_base = self.count // self.columns

            required_count = (self_base) * other.columns
            return required_count - other.count

        elif self.dir == -1 and other.dir == 1 or self.dir == 1 and other.dir == -1:
            # first case yes, second case may not work
            total_count = self.count + other.count
            total_columns = self.columns + other.columns
            total_base = total_count // total_columns
            excess = total_count % total_columns
            other_required_count = total_base * other.columns + min(
                excess, other.columns
            )
            print(
                "orc",
                other_required_count,
                total_base,
                other.columns,
                excess,
                other.columns,
            )
            return abs(other_required_count - other.count)
        elif self.dir == 0 and other.dir == 0:
            self_base = self.count // self.columns
            other_base = other.count // other.columns
            if self_base == other_base or self_base == other_base - 1:
                return 0
        return None

    def moves(self, other):
        """will ducks move from us to the other"""
        print(
            "moves",
            self.count * other.columns > self.columns * other.count,
            self.count * other.columns,
            self.columns * other.count,
        )
        return self.count * other.columns > self.columns * other.count

    def array(self, phase):
        base = self.count // self.columns
        excess = self.count % self.columns
        if phase == 1 and self.dir == -1:
            return [(base + 1) for _ in range(excess)] + [
                base for _ in range(self.columns - excess)
            ]
        else:
            return [base for _ in range(self.columns - excess)] + [
                (base + 1) for _ in range(excess)
            ]


# Part 2/3 gives the correct answer, but running the real data for part 2 I
# get a mismatch, so have some perhaps unimportant edge case I'm not getting right.

# Seen elsewhere - in phase 2 only one duck moves each time to the equilibrium state. So this would simplify things considerably


def part_2(input, comparison_on=False):
    ducks = [int(n) for n in input_generator(input)]
    sets = [Duckset(d, 0) for d in ducks]

    # Deal with duplicates in input

    s = 0
    while s < len(sets) - 1:
        done = False
        while not done:
            if sets[s].count // sets[s].columns == sets[s + 1].count:
                sets[s].combine(sets[s + 1])
                sets = sets[0 : s + 1] + sets[s + 2 :]
            else:
                done = True
                s += 1

    rounds = 0
    phase = 1
    while phase < 3:
        for s in range(len(sets)):
            sets[s].dir = 0
        for s in range(len(sets) - 1):
            if sets[s].moves(sets[s + 1]):
                sets[s].dir -= 1
                sets[s + 1].dir += 1
        min_steps = None
        min_loc = None
        for s in range(len(sets) - 1):
            print(s, "dir", sets[s].dir)
            steps = sets[s].catch_up(sets[s + 1])
            print(s, steps)
            if steps != None and (min_steps == None or steps < min_steps):
                print("best")
                min_steps = steps
                min_loc = s
        if min_loc == None:
            print("done")
            sets = sets[::-1]
            phase += 1
            continue
        rounds += min_steps
        print(
            "Merging at {} after {} steps. Rounds now {}".format(
                min_loc, min_steps, rounds
            )
        )
        for s in range(len(sets)):
            sets[s].count += min_steps * sets[s].dir
        sets[min_loc].combine(sets[min_loc + 1])
        sets = sets[0 : min_loc + 1] + sets[min_loc + 2 :]
        if comparison_on:
            # Recompute dirs
            for s in range(len(sets)):
                sets[s].dir = 0
            for s in range(len(sets) - 1):
                if sets[s].moves(sets[s + 1]):
                    sets[s].dir -= 1
                    sets[s + 1].dir += 1
            array = []
            for s in range(len(sets)):
                array += sets[s].array(phase)
            comparison_array = part_1(input, rounds=rounds, return_ducks=True)
            if phase == 2:
                comparison_array = comparison_array[::-1]
            print(sets)
            print(array, comparison_array)
            assert array == comparison_array
    return rounds


def part_3(input):
    return part_2(input)


if __name__ == "__main__":
    Run_2025_11().run_cmdline()
