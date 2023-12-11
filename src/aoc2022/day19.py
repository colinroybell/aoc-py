from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2022_19(DayBase):
    YEAR = "2022"
    DAY = "19"


# Create a state space hash as we don't care about resources over the maximum required to build something.


class State:
    def __init__(
        self,
        id,
        costs,
        time=0,
        robots=[1, 0, 0, 0],
        resources=[0, 0, 0, 0],
        prog_min=0,
        prog_max=1,
    ):
        self.id = id
        self.costs = costs
        self.time = time
        self.robots = robots
        self.resources = resources
        self.prog_min = 0
        self.prog_max = 1
        self.robots_max = [max([costs[i][j] for i in range(4)]) for j in range(4)]

    def __str__(self):
        return "id {} time {} robots {} resources {} progress {},{}".format(
            self.id,
            self.time,
            self.robots,
            self.resources,
            self.prog_min,
            self.prog_max,
        )

    def copy(self):
        return State(
            self.id, self.costs, self.time, self.robots.copy(), self.resources.copy()
        )

    def advance(self):
        # print("From {}".format(self))
        next_step = []
        none = self.copy()
        none.time += 1
        next_step.append(none)
        for i in range(4):
            none.resources[i] += none.robots[i]
        for i in range(4):
            if i < 3 and self.robots[i] == self.robots_max[i]:
                continue
            if none.time == 24:
                continue
            if none.time >= 23 and (i == 0 or i == 2):
                continue
            if none.time >= 22 and i == 1:
                continue
            if all([self.resources[j] >= self.costs[i][j] for j in range(4)]):
                robot_build = none.copy()
                robot_build.robots[i] += 1
                for j in range(4):
                    robot_build.resources[j] -= robot_build.costs[i][j]
                next_step.append(robot_build)
        for i in range(len(next_step)):
            next_step[i].prog_min = self.prog_min + i * (
                self.prog_max - self.prog_min
            ) / len(next_step)
            next_step[i].prog_max = self.prog_min + (i + 1) * (
                self.prog_max - self.prog_min
            ) / len(next_step)
        # next_step.reverse()
        return next_step


def incomplete_part_a(input):
    total = 0
    for line in input_generator(input):
        state_queue = []
        words = line.split()
        id = int(words[1][:-1])
        ore_ore = int(words[6])
        clay_ore = int(words[12])
        ob_ore = int(words[18])
        ob_clay = int(words[21])
        ge_ore = int(words[27])
        ge_ob = int(words[30])
        costs = [
            [ore_ore, 0, 0, 0],
            [clay_ore, 0, 0, 0],
            [ob_ore, ob_clay, 0, 0],
            [ge_ore, 0, ge_ob, 0],
        ]
        initial_state = State(id, costs)
        state_queue.append(initial_state)

        best = 0
        count = 0
        while state_queue and count < 10000000:
            state = state_queue.pop()
            if state.time == 24:
                count += 1
                geodes = state.resources[3]
                improved = geodes > best
                best = max(best, geodes)
                if count % 100000 == 0 or improved:
                    print(
                        "{}: {} done with {} best {}".format(count, state, geodes, best)
                    )
            else:
                advances = state.advance()
                state_queue.extend(advances)

        total += id * best
    return total


def part_a(input):
    assert 0, "not implemented"


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2022_19().run_cmdline()
