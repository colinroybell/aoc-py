from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_09(DayBase):
    YEAR = "2024"
    DAY = "09"


def part_a(input):
    line = next(input_generator(input))
    map = []
    line += "0"
    count = 0
    for i in range(0, len(line), 2):
        blocks = int(line[i])
        gaps = int(line[i + 1])
        map.extend([count for _ in range(blocks)])
        map.extend([None for _ in range(gaps)])
        count += 1

    fwd = 0
    bwd = len(map) - 1
    while fwd < bwd:
        if map[fwd] != None:
            fwd += 1
        elif map[bwd] == None:
            bwd -= 1
        else:
            map[fwd] = map[bwd]
            map[bwd] = None
            fwd += 1
            bwd -= 1
    while map[fwd]:
        fwd += 1
    checksum = 0
    for i in range(fwd):
        checksum += i * map[i]
    return checksum


def part_b(input):
    line = next(input_generator(input))
    line += "0"
    blocks = []
    gaps = []
    pos = 0
    for i in range(0, len(line), 2):
        block_count = int(line[i])
        blocks.append([pos, block_count])
        pos += block_count
        gap_count = int(line[i + 1])
        gaps.append([pos, gap_count])
        pos += gap_count
    print(gaps)

    for j in range(len(blocks) - 1, -1, -1):
        block_pos = blocks[j][0]
        block_count = blocks[j][1]
        for g in gaps:
            if g[0] > block_pos:
                break
            if g[1] >= block_count:
                print("move {} to {}".format(j, g[0]))
                blocks[j][0] = g[0]
                g[0] += block_count
                g[1] -= block_count
                break

    checksum = 0
    for i, b in enumerate(blocks):

        checksum += i * (b[0] * b[1] + (b[1] * (b[1] - 1)) // 2)
        print(i, b[0], b[1], checksum)
    return checksum


if __name__ == "__main__":
    Run_2024_09().run_cmdline()
