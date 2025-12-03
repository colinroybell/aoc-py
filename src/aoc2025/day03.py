from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_03(DayBase):
    YEAR = "2025"
    DAY = "03"


def joltage(string):
    batteries = [int(n) for n in string]
    max = 0
    max_pos = 0
    for i in range(len(batteries) - 1):
        if batteries[i] > max:
            max = batteries[i]
            max_pos = i
    max2 = 0
    for i in range(max_pos + 1, len(batteries)):
        if batteries[i] > max2:
            max2 = batteries[i]
    return max * 10 + max2


def joltageN(string, N):
    lists = [[] for n in range(10)]
    batteries = [int(n) for n in string]
    for i in range(len(batteries)):
        lists[batteries[i]].append(i)

    count = len(batteries)
    pos = 0
    value = 0
    for n in range(N):
        found = False
        search = 9
        while not found:
            # Cull anything which is left of the position
            cull = 0
            for i, p in enumerate(lists[search]):
                if p < pos:
                    cull += 1
                if p >= pos and p < count - N + n + 1:
                    value = value * 10 + search
                    # Cull anything left of the new position
                    lists[search] = lists[search][i + 1 :]
                    found = True
                    pos = p
                    break
            if not found:
                if cull:
                    lists[search] = lists[search][cull:]
                search -= 1
    return value


def part_a(input):
    total = 0
    for line in input_generator(input):
        total += joltage(line)
    return total


def part_b(input):
    total = 0
    for line in input_generator(input):
        total += joltageN(line, 12)
    return total


def notes():
    """Easier approach: maintain a stack of the potential answer, then pop if something better comes along. "Monotonic stack"."""


if __name__ == "__main__":
    Run_2025_03().run_cmdline()
