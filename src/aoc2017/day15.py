from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_15(DayBase):
    YEAR = "2017"
    DAY = "15"


def generatorStep(last, mult):
    mul = last * mult
    sum = mul + (mul >> 31)
    fast = (mul + (sum >> 31)) & ((1 << 31) - 1)
    # slow = mul % 2147483647
    # if (fast != slow):
    #    print (mul, slow, fast, sum, mul >> 31, mul & ((1<<31)-1), mul // 0x7FFFFFFF)
    # assert(fast == slow)
    return fast


def part_a(input, part_b=False):
    part_a = not part_b
    lines = []
    generator = input_generator(input)
    lines.append(next(generator))
    lines.append(next(generator))

    n = [int(line[24:]) for line in lines]
    mults = [16807, 48271]

    count = 0
    if part_a:
        iterations = 40000000
    else:
        iterations = 5000000
    for _ in range(iterations):
        for i in range(2):
            done = False
            while not done:
                n[i] = generatorStep(n[i], mults[i])
                done = (
                    part_a or (i == 0 and n[i] % 4 == 0) or (i == 1 and n[i] % 8 == 0)
                )
        if (n[1] - n[0] & 0xFFFF) == 0:
            count += 1
    return count


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_15().run_cmdline()
