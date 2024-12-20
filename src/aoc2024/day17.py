from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_17(DayBase):
    YEAR = "2024"
    DAY = "17"


reg = {}


def init():
    reg["A"] = 0
    reg["B"] = 0
    reg["C"] = 0


def set_register(r, val):
    reg[r] = val


def get_register(r):
    return reg[r]


def run_program(p):
    pc = 0
    output = ""
    while pc < len(p):
        opcode = p[pc]
        operand = p[pc + 1]

        if operand < 4:
            val = operand
        elif operand == 4:
            val = reg["A"]
        elif operand == 5:
            val = reg["B"]
        elif operand == 6:
            val = reg["C"]
        else:
            val = 0

        if opcode == 0:
            reg["A"] = reg["A"] // (1 << val)
        elif opcode == 1:
            reg["B"] ^= operand
        elif opcode == 2:
            reg["B"] = val & 7
        elif opcode == 3:
            if reg["A"]:
                pc = operand - 2
        elif opcode == 4:
            reg["B"] ^= reg["C"]
        elif opcode == 5:
            if output:
                output += ","
            output += str(val % 8)
            # print(reg['A'],oct(reg['A']),reg['B'],oct(reg['B']),reg['C'],oct(reg['C']))
        elif opcode == 6:
            reg["B"] = reg["A"] // (1 << val)
        else:
            reg["C"] = reg["A"] // (1 << val)
        pc += 2
    return output


def part_a(input):
    generator = input_generator(input)
    v = int(next(generator).split()[-1])
    set_register("A", v)
    v = int(next(generator).split()[-1])
    set_register("B", v)
    v = int(next(generator).split()[-1])
    set_register("C", v)
    _ = next(generator)
    p_string = next(generator).split()[1]
    p = [int(n) for n in p_string.split(",")]
    return run_program(p)


def part_b_recurse(n, pos, desired_output, program):
    for d in range(8):
        a = n + d * (8 ** pos)
        if pos == 16:
            print(n, d, a, pos)
        a_mod = a
        if pos < 16:
            a_mod += 8 ** 15
        init()
        set_register("A", a_mod)
        output = run_program(program)
        if pos == 16:
            print(a_mod, oct(a_mod), output)
        match_digits = pos - 3
        if pos == 16:
            if output == desired_output:
                return n
            else:
                return None
        if match_digits > 0:
            if output[: match_digits * 2 - 1] != desired_output[: match_digits * 2 - 1]:
                return None
            else:
                pass
                # print(output,desired_output)
        res = part_b_recurse(a, pos + 1, desired_output, program)
        if res:
            return res
    return None


def part_b(input):
    generator = input_generator(input)
    v = int(next(generator).split()[-1])
    set_register("A", v)
    v = int(next(generator).split()[-1])
    set_register("B", v)
    v = int(next(generator).split()[-1])
    set_register("C", v)
    _ = next(generator)
    p_string = next(generator).split()[1]
    p = [int(n) for n in p_string.split(",")]

    desired_output = p_string

    return part_b_recurse(0, 0, desired_output, p)


if __name__ == "__main__":
    Run_2024_17().run_cmdline()
