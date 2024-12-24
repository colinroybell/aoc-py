from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_24(DayBase):
    YEAR = "2024"
    DAY = "24"


def compute_value(reg, values, gates):
    if reg in values:
        return values[reg]
    r0 = gates[reg][0]
    v0 = compute_value(r0, values, gates)
    r1 = gates[reg][2]
    v1 = compute_value(r1, values, gates)
    op = gates[reg][1]
    if op == "AND":
        v = v0 & v1
    elif op == "OR":
        v = v0 | v1
    elif op == "XOR":
        v = v0 ^ v1
    else:
        assert 0, op
    print("reg {} value {}".format(reg, v))
    values[reg] = v
    return v


def part_a(input):
    values = {}
    gates = {}
    generator = input_generator(input)
    zeds = []
    for line in generator:
        if line == "":
            break
        reg = line[0:3]
        val = line[5]
        values[reg] = int(val)
        if reg[0] == "z":
            zeds.append(reg)

    for line in generator:
        fields = line.split()
        reg = fields[4]
        gates[reg] = (fields[0], fields[1], fields[2])
        if reg[0] == "z":
            zeds.append(reg)

    print(values)
    print(zeds)
    total = 0
    for z in zeds:
        value = compute_value(z, values, gates)
        total += value * 1 << int(z[1:])
    return total


def part_b(input):
    values = {}
    gates = {}
    gates_rev = {}
    generator = input_generator(input)
    for line in generator:
        if line == "":
            break
        pass

    swaps = {
        "z09": "nnf",
        "nnf": "z09",
        "z20": "nhs",
        "nhs": "z20",
        "ddn": "kqh",
        "kqh": "ddn",
        "wrc": "z34",
        "z34": "wrc",
    }
    for line in generator:
        fields = line.split()
        reg = fields[4]
        if reg in swaps:
            reg = swaps[reg]
        lhs = (fields[0], fields[1], fields[2])
        lhs_flipped = (fields[2], fields[1], fields[0])
        gates[reg] = lhs
        gates_rev[lhs] = reg
        gates_rev[lhs_flipped] = reg

    carry = [None for _ in range(45)]
    sum = [None for _ in range(45)]
    carry_and_sum = [None for _ in range(45)]
    and_ = [None for _ in range(45)]

    for b in range(45):
        print("bit", b)
        bn = "{0:02d}".format(b)
        xb = "x" + bn
        yb = "y" + bn
        zb = "z" + bn
        if b == 0:
            carry[b] = gates_rev[(xb, "AND", yb)]
            print("carry", b, carry[b])
            assert gates_rev[(xb, "XOR", yb)] == zb
        else:
            sum[b] = gates_rev[(xb, "XOR", yb)]
            print("sum", b, sum[b])
            carry_and_sum[b] = gates_rev[sum[b], "AND", carry[b - 1]]
            print("carry_and_sum", b, carry_and_sum[b])
            assert gates_rev[sum[b], "XOR", carry[b - 1]] == zb
            and_[b] = gates_rev[(xb, "AND", yb)]
            print("and_", b, and_[b])
            carry[b] = gates_rev[and_[b], "OR", carry_and_sum[b]]
            print("carry", b, carry[b])

    output = ",".join(sorted(swaps.keys()))

    return output


if __name__ == "__main__":
    Run_2024_24().run_cmdline()
