from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_09(DayBase):
    YEAR = "2017"
    DAY = "09"


def part_a(input, part_b=False):
    part_a = not part_b
    line = next(input_generator(input))
    level = 0
    sum = 0
    garbage_chars = 0
    in_garbage = False
    cancel_next = False
    for char in line:
        print(char, cancel_next, in_garbage)
        if cancel_next:
            cancel_next = False
        elif char == "!":
            cancel_next = True
        elif in_garbage:
            if char == ">":
                in_garbage = False
            else:
                garbage_chars += 1
        elif char == "<":
            in_garbage = True
        elif char == "{":
            level += 1
            sum += level
            print(level, sum)
        elif char == "}":
            level -= 1
        else:
            pass
    assert level == 0
    if part_a:
        return sum
    else:
        return garbage_chars


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_09().run_cmdline()
