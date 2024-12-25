from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_25(DayBase):
    YEAR = "2024"
    DAY = "25"


def part_a(input):
    lines = []
    keys = []
    locks = []
    for line_count, line in enumerate(input_generator(input)):
        if line:
            lines.append(line)
        print(line_count,lines)
        if line_count%8 == 6:
            c = lines[0][0]
            lens = []
            for col in range(5):
                r= 0
                while lines[r][col] == c:
                    r += 1
                if c == '#':
                    lens.append(r-1)
                else:
                    lens.append(6-r)
            if c == '#':
                locks.append(lens)
            else:
                keys.append(lens)
            lines = []            
    print(locks)
    print(keys)                                

    total = 0
    for lock in locks:
        for key in keys:
            overlap = max([lock[col] + key[col] -5 for col in range(5)])
            if overlap <=0:
                total += 1
    return total            
        



def part_b(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2024_25().run_cmdline()
