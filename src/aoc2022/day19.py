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
        end_time,
        time=0,
        robots=[1, 0, 0, 0],
        resources=[0, 0, 0, 0],
        prog_min=0,
        prog_max=1,
    ):
        self.id = id
        self.costs = costs
        self.end_time = end_time
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
            self.id,
            self.costs,
            self.end_time,
            self.time,
            self.robots.copy(),
            self.resources.copy(),
        )

    def advance(self, best_so_far):
        time_remaining = self.end_time - self.time
        max_possible = (
            self.resources[3]
            + time_remaining * self.robots[3]
            + time_remaining * (time_remaining - 1) // 2
        )
        # print("From {} {}".format(self,max_possible))
        if max_possible < best_so_far:
            return []
        next_step = []

        for i in range(4):
            if i < 3 and self.robots[i] == self.robots_max[i]:
                continue
            max_t = 0
            for j in range(4):
                if self.costs[i][j] > self.resources[j]:
                    if self.robots[j] == 0:
                        max_t = 100
                    else:
                        t = (
                            1
                            + (self.costs[i][j] - self.resources[j] - 1)
                            // self.robots[j]
                        )
                        max_t = max(max_t, t)
            proposed_time = self.time + max_t
            if (
                proposed_time >= self.end_time
                or proposed_time >= self.end_time - 1
                and (i == 0 or i == 2)
                or proposed_time >= self.end_time - 2
                and i == 1
            ):
                continue
            robot_build = self.copy()
            robot_build.time = proposed_time + 1
            for j in range(4):
                robot_build.resources[j] += (
                    robot_build.robots[j] * (max_t + 1) - robot_build.costs[i][j]
                )
            robot_build.robots[i] += 1
            next_step.append(robot_build)
        if not next_step:
            # can't build anything, so just advance to 24
            no_build = self.copy()
            for j in range(4):
                no_build.resources[j] += no_build.robots[j] * (
                    self.end_time - self.time
                )
            no_build.time = self.end_time
            next_step.append(no_build)
        # print(next_step)
        return next_step

    def __repr__(self):
        return self.__str__()


def part_a(input, part_b=False):
    part_a = not part_b
    if part_a:
        end_time = 24
    else:
        end_time = 32
    total = 0
    product = 1
    line_count = 0
    for line in input_generator(input):
        if part_b and line_count == 3:
            break
        line_count += 1
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
        initial_state = State(id, costs, end_time)
        state_queue.append(initial_state)

        best = 0
        count = 0
        while state_queue and count < 10000000:
            state = state_queue.pop()
            if state.time == end_time:
                count += 1
                geodes = state.resources[3]
                improved = geodes > best
                best = max(best, geodes)
                if count % 100000 == 0 or improved:
                    print(
                        "{}: {} done with {} best {}".format(count, state, geodes, best)
                    )
            else:
                advances = state.advance(best)
                state_queue.extend(advances)

        total += id * best
        product *= best
    if part_a:
        return total
    else:
        return product


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2022_19().run_cmdline()
