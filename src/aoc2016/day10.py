from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2016_10(DayBase):
    YEAR = "2016"
    DAY = "10"


def part_a(input, part_b=False):
    part_a = not part_b
    rules = {}
    bots = defaultdict(lambda: [])
    outputs = defaultdict(lambda: [])
    for line in input_generator(input):
        fields = line.split()
        if line.startswith("value"):
            v = int(fields[1])
            b = int(fields[5])
            bots[b].append(v)
        else:
            print(fields)
            b = int(fields[1])
            lowtype = fields[5]
            lowcount = int(fields[6])
            hightype = fields[10]
            highcount = int(fields[11])
            rules[b] = [[lowtype, lowcount], [hightype, highcount]]
            if lowtype == "bot" and lowcount not in bots:
                bots[lowcount] == []
            if hightype == "bot" and highcount not in bots:
                bots[highcount] == []

    c = [0, 0]
    done = False
    while not done:
        done = True
        for b, contents in bots.items():
            if len(contents) == 2:
                done = False
                c[0] = min(contents)
                c[1] = max(contents)
                if part_a and c[0] == 17 and c[1] == 61:
                    return b
                bots[b] = []
                for i in range(2):
                    r = rules[b][i]
                    if r[0] == "output":
                        print("bot {} gives {} to output {}".format(b, c[i], r[1]))
                        outputs[r[1]].append(c[i])
                    else:
                        print("bot {} gives {} to bot {}".format(b, c[i], r[1]))
                        bots[r[1]].append(c[i])
    return outputs[0][0] * outputs[1][0] * outputs[2][0]


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2016_10().run_cmdline()
