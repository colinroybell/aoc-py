from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_24(DayBase):
    YEAR = "2015"
    DAY = "24"


# 0 unused
# 1 used
# 2 shelved for now
def recurse_1(part_b, target, sizes, states_in, total, length, shortest, best_qe):
    # print('. '*length,target,total,states_in,length,shortest,best_qe)
    states = states_in.copy()
    for i, a in enumerate(sizes):
        if states[i] == 0:
            if total + a > target:
                states[i] = 2
            elif total + a == target:
                # solution
                states[i] = 1
                states_new = states.copy()
                for i, a in enumerate(states):
                    if a == 2:
                        states[i] = 0
                if part_a:
                    groups = 1
                else:
                    groups = 2
                if recurse_2(groups, target, sizes, states, 0, length + 1):
                    qe = 1
                    for j in range(0, i + 1):
                        if states[j] == 1:
                            qe *= sizes[j]
                    if best_qe == None or qe < best_qe:
                        best_qe = qe
                    return (length + 1, best_qe)
            else:
                if shortest == None or length < shortest - 1:
                    states[i] = 1
                    (shortest, best_qe) = recurse_1(
                        part_b,
                        target,
                        sizes,
                        states,
                        total + a,
                        length + 1,
                        shortest,
                        best_qe,
                    )
                    states[i] = 2
    return (shortest, best_qe)


def recurse_2(
    groups, target, sizes, states_in, total, length
):  # length just for debugging
    # print('+ '*length,target,total,states_in,length)
    states = states_in.copy()
    for i, a in enumerate(sizes):
        if states[i] == 0:
            if total + a > target:
                states[i] = 2
            elif total + a == target:
                if groups == 1:
                    return True
                else:
                    states_new = states.copy()
                    for i, a in enumerate(states):
                        if a == 2:
                            states[i] = 0
                    return recurse_2(groups - 1, target, sizes, states, 0, length + 1)
            else:
                states[i] = 1
                if recurse_2(groups, target, sizes, states, total + a, length + 1):
                    return True
                states[i] = 2
    return False


def part_a(input, part_b=False):
    part_a = not part_b
    sizes = []
    for line in input_generator(input):
        sizes.append(int(line))
    if part_a:
        target = sum(sizes) // 3
    else:
        target = sum(sizes) // 4
    sizes.reverse()

    states = [0 for _ in range(len(sizes))]
    (length, qe) = recurse_1(part_b, target, sizes, states, 0, 0, None, None)
    return qe


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2015_24().run_cmdline()
