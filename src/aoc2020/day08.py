from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2020_08(DayBase):
    YEAR = "2020"
    DAY = "08"


class State:
    def __init__(self, program):
        self.acc = 0
        self.pos = 0
        self.program = []
        print(program)
        for line in program:
            line = line.rstrip()
            fields = line.split()
            self.program.append((fields[0], int(fields[1])))
        self.inst_counts = [0] * (len(program) + 1)

    def step(self):
        self.inst_counts[self.pos] += 1
        (command, field) = self.program[self.pos]
        if command == "nop":
            self.pos += 1
        if command == "acc":
            self.acc += field
            self.pos += 1
        if command == "jmp":
            self.pos += field

    def looped(self):
        return self.inst_counts[self.pos] > 0

    def done(self):
        return self.pos == len(self.program)

    def get_acc(self):
        return self.acc


def part_a(input):
    lines = [line for line in input_generator(input)]
    program = State(lines)
    while not program.looped():
        program.step()
    return program.get_acc()


def part_b(input):
    lines = [line for line in input_generator(input)]

    for i in range(0, len(lines)):
        cmd = lines[i][0:3]
        if cmd != "acc":
            mod_lines = lines[:]
            if cmd == "jmp":
                mod_lines[i] = "nop" + mod_lines[i][3:]
            else:
                mod_lines[i] = "jmp" + mod_lines[i][3:]
            program = State(mod_lines)
            while not program.looped() and not program.done():
                program.step()
            if program.done():
                return program.get_acc()
    return 0


if __name__ == "__main__":
    Run_2020_08().run_cmdline()
