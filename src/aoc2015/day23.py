from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2015_23(DayBase):
    YEAR = "2015"
    DAY = "23"


def part_a(input, part_b=False):
    program = [line for line in input_generator(input)]
    length = len(program)
    offsets = [None for _ in range(length)]
    offset_re = re.compile(r"([\+\-]\d+)")
    for i in range(length):
        m = offset_re.search(program[i])
        if m:
            offsets[i] = int(m.group(1))
    pc = 0
    a = 0
    if part_b:
        a = 1
    b = 0

    while pc < length:
        command = program[pc]
        if command == "hlf a":
            assert a % 2 == 0
            a //= 2
        elif command == "tpl a":
            a *= 3
        elif command == "inc a":
            a += 1
        elif command == "inc b":
            b += 1
            print(a)
        elif command.startswith("jmp"):
            pc += offsets[pc] - 1
        elif command.startswith("jio"):
            if a == 1:
                pc += offsets[pc] - 1
        elif command.startswith("jie"):
            if a % 2 == 0:
                pc += offsets[pc] - 1
        else:
            assert 0
        pc += 1
    return b


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2015_23().run_cmdline()
