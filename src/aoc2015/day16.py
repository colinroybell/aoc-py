from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2015_16(DayBase):
    YEAR = "2015"
    DAY = "16"


def part_a(input, part_b=False):
    collection_mode = True
    items = {}
    sue_re = re.compile(r"Sue (\d+):(.+)")
    for line in input_generator(input):
        if collection_mode:
            if line == "":
                collection_mode = False
            else:
                fields = line.split()
                items[fields[0]] = int(fields[1])
        else:
            m = sue_re.match(line)
            number = int(m.group(1))
            fields = m.group(2).split(", ")
            ok = True
            for f in fields:
                f2 = f.split()
                key = f2[0]
                value = int(f2[1])
                if part_b and key in ["cats:", "trees:"]:
                    if items[key] >= value:
                        ok = False
                        break
                elif part_b and key in ["pomeranians:", "goldfish:"]:
                    if items[key] <= value:
                        ok = False
                        break
                elif items[key] != value:
                    ok = False
                    break
            if ok:
                return number
    assert 0, "not found"


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2015_16().run_cmdline()
