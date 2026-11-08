from utils.day_base import DayBase
from utils.data_input import input_generator
from queue import PriorityQueue


class Run_2026_09(DayBase):
    YEAR = "2026"
    DAY = "09"
    PREFIX = "ec"


def parse_fields(line):
    strings = line.split(", ")
    fields = {}
    for string in strings:
        id, value = string.split("=")
        value = int(value)
        fields[id] = value
    return fields


def time_to_limit(growth, limit, part):
    if part > 1:
        return time_to_limit_part2_fast(growth, limit)
    counts = [0 for _ in range(growth)]
    if part == 1:
        score = 0
    else:
        score = 1
    counts[0] = 1
    time = 0
    split = (growth - 1) // 2
    print(f"growth {growth} limit {limit}")
    while score < limit:
        new_counts = [0 for _ in range(growth)]
        for n, count in enumerate(counts):
            if n < growth - 1:
                if part == 1:
                    score += count
                new_counts[n + 1] += count
            else:
                if part == 1:
                    score += 2 * count
                else:
                    score += count
                new_counts[split] += 2 * count
                new_counts[1] += count
        time += 1
        print(f"time {time} score {score}")
        counts = new_counts
    if part >= 2:
        t2 = time_to_limit_part2_fast(growth, limit)
        assert t2 == time
    return time


def time_to_limit_part2_fast(growth, limit):
    score = 1
    queue = PriorityQueue()
    futures = {}
    futures[growth] = 1
    queue.put((growth, None))
    t = 1
    print(score, limit)
    while score < limit:
        (t, _) = queue.get()
        v = futures[t]
        del futures[t]

        score += v

        main = t + growth // 2 + 1
        if main in futures:
            futures[main] += 2 * v
        else:
            futures[main] = 2 * v
            queue.put((main, None))

        branch = t + growth - 1
        if branch in futures:
            futures[branch] += v
        else:
            futures[branch] = v
            queue.put((branch, None))
    return t


def part_1(input, part=1):
    generator = input_generator(input)
    total = 0
    for line in generator:
        fields = parse_fields(line)
        total += time_to_limit(fields["growth"], fields["limit"], part)
    return total


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=2)


if __name__ == "__main__":
    Run_2026_09().run_cmdline()
