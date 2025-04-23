from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_12(DayBase):
    YEAR = "2025"
    DAY = "12"
    PREFIX = "codyssi"


def run_action(data, rows, cols, line):
    fields = line.split()
    if fields[0] == "SHIFT":
        num = int(fields[2]) - 1
        amount = int(fields[4])
        if fields[1] == "ROW":
            output = [0 for i in range(cols)]
            for i in range(cols):
                output[(i + amount) % cols] = data[num][i]
            for i in range(cols):
                data[num][i] = output[i]
        else:
            output = [0 for _ in range(rows)]
            for i in range(rows):
                output[(i + amount) % rows] = data[i][num]
            for i in range(cols):
                data[i][num] = output[i]
    else:
        target = fields[2]
        if target != "ALL":
            num = int(fields[3]) - 1
        op = fields[0]
        amount = int(fields[1])

        for i in range(rows):
            for j in range(cols):
                if (
                    target == "ALL"
                    or (target == "ROW" and i == num)
                    or (target == "COL" and j == num)
                ):
                    val = data[i][j]
                    if op == "ADD":
                        val += amount
                    elif op == "SUB":
                        val -= amount
                    else:
                        val *= amount
                    data[i][j] = val % 1073741824


def part_1(input, part=1):
    data = []
    rows = 0
    generator = input_generator(input)
    for line in generator:
        if not line:
            break
        fields = line.split()
        row = [int(n) for n in fields]
        data.append(row)
        rows += 1
        cols = len(row)

    actions = []

    for line in generator:
        if not line:
            break
        actions.append(line)

    if part == 1:
        for action in actions:
            run_action(data, rows, cols, action)
    elif part == 2:
        buffer = None
        for line in generator:
            if line == "TAKE":
                buffer = actions.pop(0)
            elif line == "CYCLE":
                actions.append(buffer)
            else:
                run_action(data, rows, cols, buffer)
    else:
        instructions = []
        for line in generator:
            instructions.append(line)

        while actions:
            for inst in instructions:
                if inst == "TAKE":
                    if actions:
                        buffer = actions.pop(0)
                    else:
                        break
                elif inst == "CYCLE":
                    actions.append(buffer)
                else:
                    run_action(data, rows, cols, buffer)

    row_max = max([sum(data[i][j] for j in range(cols)) for i in range(rows)])
    col_max = max([sum(data[i][j] for i in range(rows)) for j in range(cols)])
    return max(row_max, col_max)


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2025_12().run_cmdline()
