from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_03(DayBase):
    YEAR = "2017"
    DAY = "03"


def part_a(input):
    a = int(next(input_generator(input)))
    if a == 1:
        return 0
    a -= 2
    level = 1
    while a >= 8 * level:
        a -= 8 * level
        level += 1
    # access points are at level - 1, then every 2*level
    print("Level {} offset {}".format(level, a))
    a = (a + 2 * level - (level - 1)) % (level * 2)

    if a <= level:
        return a + level
    else:
        return (2 * level) - a + level


# TODO: convert this to standard grid
def part_b(input):
    a = int(next(input_generator(input)))
    mem = [[0] * 100 for x in range(100)]

    def addSum(a, b):
        sum_ = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                sum_ += mem[a + i][b + j]
        mem[a][b] = sum_
        return sum_

    xPos = 50
    yPos = 50
    round = 1
    mem[xPos][yPos] = 1
    while 1:
        for i in range(round):
            xPos += 1
            sum_ = addSum(xPos, yPos)
            if sum_ > a:
                return sum_
        for i in range(round):
            yPos -= 1
            sum_ = addSum(xPos, yPos)
            if sum_ > a:
                return sum_
        round += 1
        for i in range(round):
            xPos -= 1
            sum_ = addSum(xPos, yPos)
            if sum_ > a:
                return sum_
        for i in range(round):
            yPos += 1
            sum_ = addSum(xPos, yPos)
            if sum_ > a:
                return sum_
        round += 1


if __name__ == "__main__":
    Run_2017_03().run_cmdline()
