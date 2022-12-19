from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2022_03(DayBase):
    YEAR = "2022"
    DAY = "03"


def part_a(input):
    total = 0
    for line in input_generator(input):
        length = len(line)
        fh = line[: length // 2]
        sh = line[length // 2 :]
        print(fh, sh)
        for c in fh:
            if c in sh:
                if c.islower():
                    total += ord(c) - ord("a") + 1
                else:
                    total += ord(c) - ord("A") + 27
                break
    return total


def part_b(input):
    total = 0
    elf = 0
    sacks = []
    for line in input_generator(input):
        sack = set()
        for c in line:
            sack.add(c)
        sacks.append(sack)
        if len(sacks) == 3:
            badge = sacks[0].intersection(sacks[1], sacks[2])
            assert len(badge) == 1
            c = list(badge)[0]
            if c.islower():
                total += ord(c) - ord("a") + 1
            else:
                total += ord(c) - ord("A") + 27
            sacks = []
    return total


if __name__ == "__main__":
    Run_2022_03().run_cmdline()
