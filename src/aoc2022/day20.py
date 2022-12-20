from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2022_20(DayBase):
    YEAR = "2022"
    DAY = "20"


def output(vals, fwd):
    for i in fwd:
        print(vals[i], end=",")
    print()


# Note: don't fully understand how the mixing operation is meant to work. I think it involves removing the element from the list, moving things around and then dropping things back in (which would explain the modulo one less). If this is the case it can be made a lot more efficient.


def part_a(input, part_b=False):
    vals = []
    fwd = []
    rev = []
    count = 0
    zero = None
    for line in input_generator(input):
        val = int(line)
        if part_b:
            val *= 811589153
        vals.append(val)
        fwd.append(count)
        rev.append(count)
        if val == 0:
            zero = count
        count += 1

    if part_b:
        rounds = 10
    else:
        rounds = 1
    # output(vals,fwd)
    for _ in range(rounds):
        for i in range(count):
            val = vals[i]
            pos = rev[i]
            if val > 0:
                for _ in range(val % (count - 1)):
                    newpos = (pos + 1) % count
                    other = fwd[newpos]
                    fwd[newpos] = i
                    fwd[pos] = other
                    rev[other] = pos
                    rev[i] = newpos
                    pos = newpos
            else:
                for _ in range(-val % (count - 1)):
                    newpos = (pos - 1) % count
                    other = fwd[newpos]
                    fwd[newpos] = i
                    fwd[pos] = other
                    rev[other] = pos
                    rev[i] = newpos
                    pos = newpos
            # output(vals,fwd)
    return (
        vals[fwd[(1000 + rev[zero]) % count]]
        + vals[fwd[(2000 + rev[zero]) % count]]
        + vals[fwd[(3000 + rev[zero]) % count]]
    )


def part_b(input):
    return part_a(input, part_b=True)
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2022_20().run_cmdline()
