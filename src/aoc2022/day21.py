from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2022_21(DayBase):
    YEAR = "2022"
    DAY = "21"


def part_a(input, part_b=False, humn=0):
    deps = {}
    monkey = {}
    process_list = []
    simple_re = re.compile(r"(\w+): (\d+)")
    complex_re = re.compile(r"(\w+): (\w+) (.) (\w+)")
    for line in input_generator(input):
        m = simple_re.match(line)
        if m:
            value = int(m.group(2))
            if part_b and m.group(1) == "humn":
                value = humn
            monkey[m.group(1)] = [value]
            process_list.append(m.group(1))
        else:
            m = complex_re.match(line)
            assert m
            this = m.group(1)
            left = m.group(2)
            op = m.group(3)
            if part_b and this == "root":
                op = "-"
            right = m.group(4)

            monkey[this] = [left, op, right]
            if left not in deps:
                deps[left] = []
            deps[left].append(this)
            if right not in deps:
                deps[right] = []
            deps[right].append(this)

    while process_list:
        m = process_list.pop()
        if len(monkey[m]) > 1:
            left = monkey[monkey[m][0]]
            right = monkey[monkey[m][2]]
            if len(left) == 1 and len(right) == 1:
                string = "{}{}{}".format(left[0], monkey[m][1], right[0])
                monkey[m] = [eval(string)]
        if len(monkey[m]) == 1:
            if m in deps:
                process_list.extend(deps[m])

    return monkey["root"][0]


def part_b(input):
    # 2*50 empirically determined.
    h0 = 0
    h1 = 2 ** 50

    v0 = part_a(input, True, h0)
    v1 = part_a(input, True, h1)

    print(h0, v0)
    print(h1, v1)

    count = 0

    while 1:
        h2 = (h0 + h1) // 2
        v2 = part_a(input, True, h2)
        print(h2, v2)
        if v2 == 0:
            return h2
        if v0 * v2 > 0:
            h0 = h2
        else:
            h1 = h2
        count += 1
        # assert(count<25)


if __name__ == "__main__":
    Run_2022_21().run_cmdline()
