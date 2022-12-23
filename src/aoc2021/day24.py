from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2021_24(DayBase):
    YEAR = "2021"
    DAY = "24"


class State:
    def __init__(self, input):
        self.var = {}
        for v in ["w", "x", "y", "z"]:
            self.var[v] = 0
        self.input = input[:]

    def read(self, v):
        return self.var[v]

    def write(self, v, val):
        self.var[v] = val

    def get_input(self):
        v = self.input[0]
        self.input = self.input[1:]
        return v


class Instruction:
    def __init__(self, line):
        words = line.split()
        self.val = []
        for i, w in enumerate(words):
            if i == 0:
                self.op = w
            else:
                # surely a better way
                if w.isnumeric() or w[0] == "-":
                    self.val.append(int(w))
                else:
                    self.val.append(w)

    def run(self, state):
        if self.op == "inp":
            reg = self.val[0]
            val = state.get_input()
            print("inp {} {}".format(reg, val))
            state.write(reg, val)
            return True
        else:
            val = [0, 0]
            reg = self.val[0]
            for i in range(0, 2):
                if isinstance(self.val[i], int):
                    val[i] = self.val[i]
                else:
                    val[i] = state.read(self.val[i])
            print(self.op, val[0], val[1], "to", reg)
            assert isinstance(state.var["x"], int)
            output = 0
            if self.op == "add":
                output = val[0] + val[1]
            elif self.op == "mul":
                output = val[0] * val[1]
            elif self.op == "div":
                if val[1] == 0:
                    return False
                # Truncate towards 0
                if val[0] / val[1] >= 0:
                    output = val[0] // val[1]
                else:
                    output = -(-val[0]) // val[1]
            elif self.op == "mod":
                if val[1] <= 0:
                    return False

                output = val[0] % val[1]
            elif self.op == "eql":
                if val[0] == val[1]:
                    output = 1
                else:
                    output = 0
            else:
                assert 0
            print("output", output)
            assert isinstance(output, int)
            state.write(reg, output)
            return True


class Inst:
    def __init__(self):
        pass


def recurse(instructions, step, z, cmp_fn):
    if step > 9:
        print("Trying", step, z)
    if step == -1 and z == 0:
        # Done
        return 0
    # temporary to check things working
    if 0 and step == 6:
        if z == 0:
            print("Term with", z)
            return 0
        else:
            return None

    inst = instructions[step]
    best = None
    if inst.shift:
        for w in range(1, 10):
            # With a match
            z_mod = w - inst.x
            if 0 <= z_mod < 26:
                best_rec = recurse(instructions, step - 1, z * 26 + z_mod, cmp_fn)
                if best_rec != None:
                    val = best_rec * 10 + w
                    print(step, "Option", val)
                    if best == None:
                        best = val
                    else:
                        best = cmp_fn(best, val)
            # Without a match
            zz = z - w - inst.y
            if zz >= 0 and zz % 26 == 0:
                # print("don't match",w)
                for m in range(0, 26):
                    best_rec = recurse(instructions, step - 1, zz + m, cmp_fn)
                    if best_rec != None:
                        val = best_rec * 10 + w
                        if best == None:
                            best = val
                        else:
                            best = cmp_fn(best, val)

    else:
        for w in range(1, 10):
            zz = z - w - inst.y
            if zz >= 0 and zz % 26 == 0:
                best_rec = recurse(instructions, step - 1, zz // 26, cmp_fn)
                if best_rec != None:
                    val = best_rec * 10 + w
                    if best == None:
                        best = val
                    else:
                        best = cmp_fn(best, val)

    return best


def part_a(input, part_b = False):
    part_a = not part_b
    instructions = []
    for line in input_generator(input):
        words = line.split()
        inst = Inst()
        inst.x = int(words[0])
        inst.y = int(words[1])
        inst.shift = False
        if len(words) > 2:
            inst.shift = True
        instructions.append(inst)

    input = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 5, 9]
    z = 0
    for i, inst in enumerate(instructions):
        if i == 6:
            z = 0
        print(inst)
        w = input[i]
        x = (z % 26) + inst.x
        if inst.shift:
            z //= 26
        if x != w:
            z *= 26
            z += w + inst.y
        print(z, z % 26)

    # return
    if part_a:
        cmp_fn = max
    else:
        cmp_fn = min
    best = recurse(instructions, 13, 0, cmp_fn)
    return best

def part_b(input):
    return part_a(input, part_b = True)

if __name__ == "__main__":
    Run_2021_24().run_cmdline()
