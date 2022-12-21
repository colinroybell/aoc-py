from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2022_05(DayBase):
    YEAR = "2022"
    DAY = "05"


def disp(crates, n):
    for i in range(1, n + 1):
        print(i, ": ", crates[i])


def part_a(input, part_b=False):
    init = []
    move_re = re.compile(r"move (\d+) from (\d+) to (\d+)")
    state = 0
    crates = {}
    for line in input_generator(input):
        if not line:
            print((init[:-1]).reverse())
            nums = init[-1]
            crate_inits = init[:-1]
            crate_inits.reverse()
            n = len(nums.split())
            print(n)
            for i in range(1, n + 1):
                crates[i] = ""
            for line in crate_inits:
                # Add whitespace to aid parsing
                line += " " * (4 * n)
                for i in range(1, n + 1):
                    c = line[i * 4 - 3]
                    if c != " ":
                        crates[i] += c
            disp(crates, n)
            state = 1
        elif state == 0:
            init.append(line)
        else:
            m = move_re.match(line)
            assert m
            count = int(m.group(1))
            stack_from = int(m.group(2))
            stack_to = int(m.group(3))
            if not part_b:
                for _ in range(count):
                    c = crates[stack_from][-1]
                    crates[stack_from] = crates[stack_from][:-1]
                    crates[stack_to] += c
            else:
                c = crates[stack_from][-count:]
                crates[stack_from] = crates[stack_from][:-count]
                crates[stack_to] += c
            disp(crates, n)

    output = ""
    for i in range(1, n + 1):
        output += crates[i][-1]
    return output


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2022_05().run_cmdline()
