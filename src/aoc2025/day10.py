from utils.day_base import DayBase
from utils.data_input import input_generator
from random import randint, seed


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


def button_options(buttons, targets, cache):
    parity = [c % 2 for c in targets]
    # if max(parity) == 0:
    #    return [(0,parity)]
    parity_hash = tuple(parity)
    if parity_hash in cache:
        return cache[parity_hash]
    # print('button_options',parity)
    options = []
    if max(parity) == 0:
        options.append((0, parity))
    initial = [0 for _ in range(len(targets))]
    queue = []
    queue.append((initial, 0, 0))
    state_count = 0
    while queue:
        (state, count, first) = queue[0]
        # print(state,count,first)
        state_count += 1
        assert state_count < 10000
        queue = queue[1:]
        for n in range(first, len(buttons)):
            new_state = state.copy()
            for b in buttons[n]:
                new_state[b] += 1
            match = True
            for i in range(len(parity)):
                if new_state[i] % 2 != parity[i]:
                    match = False
                    break

            if match:
                options.append((count + 1, new_state))
            # This needed as you need to cover parity counts of buttons too
            queue.append((new_state, count + 1, n + 1))
    # print(options)
    return options


def naive_recurse(buttons, targets, pos):
    # print(pos,targets)
    if max(targets) == 0:
        # print('done')
        return (0, [])
    maximum = min(targets[b] for b in buttons[pos])
    if pos == len(buttons) - 1:
        new_targets = targets.copy()
        for b in buttons[pos]:
            new_targets[b] -= maximum
        if max(new_targets) == 0:
            return (maximum, [maximum])
        else:
            return (None, None)

    best = None
    best_pattern = None
    new_targets = targets.copy()
    for c in range(0, maximum + 1):
        # print('recurse',c)
        (ret, pattern) = naive_recurse(buttons, new_targets, pos + 1)
        if ret != None:
            score = c + ret
            pattern = [c] + pattern
            if best == None or score < best:
                best = score
                best_pattern = pattern
        for b in buttons[pos]:
            new_targets[b] -= 1
    # print(pos,targets,'return',best)
    return (best, best_pattern)


def part_b_score_recurse(buttons, targets, parity_cache, target_cache):
    # print('targets:',targets)
    target_hash = tuple(targets)
    if target_hash in target_cache:
        return target_cache[target_hash]
    opts = button_options(buttons, targets, parity_cache)
    # print(targets,opts)
    best = None
    for (c, jolts) in opts:
        new_targets = [(targets[i] - jolts[i]) // 2 for i in range(len(targets))]
        if min(new_targets) < 0:
            continue
        if max(new_targets) == 0:
            score = c
        else:
            ret = part_b_score_recurse(buttons, new_targets, parity_cache, target_cache)
            if ret:
                score = c + 2 * ret
            else:
                score = None
        if best == None or score != None and score < best:
            best = score
    target_cache[target_hash] = best
    if 0:
        (naive_score, naive_pattern) = naive_recurse(buttons, targets, 0)
        print("res", targets, best, naive_score, naive_pattern)
        assert naive_score == best
    # print(target_cache)
    # print('targets:',targets,'best:',best)
    return best


def part_b_score(buttons, targets):
    parity_cache = {}
    target_cache = {}
    score = part_b_score_recurse(buttons, targets, parity_cache, target_cache)
    print(score)
    if score == None:
        return 0
    if 0 and score < 100:
        (naive_score, naive_pattern) = naive_recurse(buttons, targets, 0)
        print("res", targets, score, naive_score, naive_pattern)
        assert naive_score == score
    return score


def part_a(input, part="a"):
    total = 0
    for line in input_generator(input):
        print(line)
        fields = line.split(" ")
        pattern_string = fields[0][1:-1]
        pattern = [c for c in pattern_string]
        target_string = fields[-1][1:-1]
        targets = [int(c) for c in target_string.split(",")]
        # targets = [randint(10,40) for _ in targets]
        # print(targets)
        fields = fields[1:-1]
        buttons = []
        for f in fields:
            f = f[1:-1]
            buttons.append([int(n) for n in f.split(",")])
        if part == "a":
            total += part_a_score(pattern, buttons)
        else:
            total += part_b_score(buttons, targets)
    return total


def part_b(input):
    return part_a(input, part="b")


def notes():
    """
    This now works, but needs tidying up. Would be worth exploring linear algebra methods,
    but I'm unsure how we know that solutions are integral, if we rearrange how to get back to positive integers,
    and how to deal with potentially arbitrary numbers of solutions. To think about.
    """


if __name__ == "__main__":
    Run_2025_10().run_cmdline()
