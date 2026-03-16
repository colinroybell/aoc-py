from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_st02_02(DayBase):
    YEAR = "st02"
    DAY = "02"
    PREFIX = "ec"

    NOTES = """
    For part 3 we need at least a more efficient data structure that doesn't involve massive string 
    concatenation. I can't see any sensible patterns.
    """


def part_1(input):
    # Add an X to simplify edge conditions
    balloons = next(input_generator(input)) + "X"
    shots = "RGB"
    count = 0
    while 1:
        for shot in shots:
            count += 1
            while balloons[0] == shot:
                balloons = balloons[1:]
            balloons = balloons[1:]
            # If last balloon matched shot, we will also pop the X.
            if balloons == "" or balloons == "X":
                return count


def part_2(input, repeats=100):
    pattern = next(input_generator(input))
    balloons = pattern * repeats
    count = 0
    shots = "RGB"
    while balloons:
        shot = shots[count % 3]
        count += 1
        if count % 1000 == 0:
            print(count, len(balloons))
        length = len(balloons)
        if length % 2 == 0 and balloons[0] == shot:
            balloons = balloons[: length // 2] + balloons[length // 2 + 1 :]
        balloons = balloons[1:]
    return count


def part_3(input):
    for n in [1, 10, 100, 1000, 10000]:
        print("answer", n, part_2(input, repeats=n))
    return part_2(input, repeats=100000)


if __name__ == "__main__":
    Run_st02_02().run_cmdline()
