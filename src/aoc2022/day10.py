from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2022_10(DayBase):
    YEAR = "2022"
    DAY = "10"


def part_a(input, part_b=False):
    reg = 1
    values = [1, 1]
    times = [20, 60, 100, 140, 180, 220]
    for line in input_generator(input):
        cycle = 0
        if line == "noop":
            values.append(reg)
        elif line[0:4] == "addx":
            arg = int(line[5:])
            values.append(reg)
            reg += arg
            values.append(reg)
        else:
            assert 0
    if not part_b:
        total = 0
        for t in times:
            total += t * values[t]
        return total
    else:
        output = ""
        x = 0
        for cycles in range(1, 241):
            if abs(values[cycles] - x) <= 1:
                output += "#"
            else:
                output += "."
            x += 1
            if x == 40:
                output += "\n"
                x = 0
        print(output)
        return output


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2022_10().run_cmdline()
