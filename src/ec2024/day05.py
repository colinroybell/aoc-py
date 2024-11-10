from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2024_05(DayBase):
    YEAR = "2024"
    DAY = "05"
    PREFIX = "ec"


def part_1(input, rounds=10, part=1):
    cols = 4
    clappers = [[] for _ in range(cols)]
    for line in input_generator(input):
        fields = line.split()
        for i in range(cols):
            clappers[i].append(int(fields[i]))
    round = 0

    record = defaultdict(lambda: 0)
    maximum = 0
    maximum_states = []

    while 1:
        from_col = round % cols
        to_col = (round + 1) % cols
        dancer = clappers[from_col][0]
        clappers[from_col] = clappers[from_col][1:]

        length = len(clappers[to_col])
        dancer_pos = ((dancer - 1) % (length * 2)) + 1
        if dancer_pos <= length:
            pos = dancer_pos - 1
        else:
            pos = 2 * length - dancer_pos + 1
        clappers[to_col] = clappers[to_col][:pos] + [dancer] + clappers[to_col][pos:]

        round += 1
        string = ""
        for col in range(cols):
            string += str(clappers[col][0])

        value = int(string)

        if part == 1 and round == rounds:
            return value
        if part == 2:
            record[value] += 1
            if record[value] == 2024:
                return round * value
        if part == 3:
            print(round, value)
            if value > maximum:
                print(round, value)
                maximum = value
                maximum_states = [(round % cols, clappers.copy())]
            elif value == maximum:
                print(round, value)
                if (round % cols, clappers) in maximum_states:
                    return value
                else:
                    maximum_states.append((round % cols, clappers.copy()))
                    print(round, maximum, len(maximum_states))
            else:
                # TODO: we are getting into a loop but maximum value isn't in it.
                if (round % cols, clappers) in maximum_states:
                    return maximum
                maximum_states.append((round % cols, clappers.copy()))


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2024_05().run_cmdline()
