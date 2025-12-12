from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_10(DayBase):
    YEAR = "2025"
    DAY = "10"


def part_a_score(pattern, buttons):
    initial = ["." for _ in range(len(pattern))]
    queue = []
    queue.append((initial, 0, 0))
    cache = set()
    while queue:
        (state, count, first) = queue[0]
        # print(state,count,first)
        queue = queue[1:]
        for n in range(first, len(buttons)):
            new_state = state.copy()
            for b in buttons[n]:
                new_state[b] = {".": "#", "#": "."}[new_state[b]]
            if new_state == pattern:
                return count + 1
            # Avoid states we've already considered by computing a binary score
            # and caching
            score = 0
            for i, c in enumerate(new_state):
                score = score * 2
                if c == "#":
                    score += 1
            if score not in cache:
                cache.add(score)
                # print("append {}: {} {} {}".format(n,new_state,count+1,first+1))
                queue.append((new_state, count + 1, first + 1))
    assert 0


def part_a(input):
    total = 0
    for line in input_generator(input):
        print(line)
        fields = line.split(" ")
        pattern_string = fields[0][1:-1]
        pattern = [c for c in pattern_string]
        fields = fields[1:-1]
        buttons = []
        for f in fields:
            f = f[1:-1]
            buttons.append([int(n) for n in f.split(",")])
        total += part_a_score(pattern, buttons)
    return total


def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2025_10().run_cmdline()
