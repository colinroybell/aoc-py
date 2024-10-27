from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_12(DayBase):
    YEAR = "2015"
    DAY = "12"


# TODO: parsing is very inefficient - ought to go down the tree. Do we have a generic parsing library we could use?


def part_a_old(input):
    string = next(input_generator(input))
    current = 0
    sign = 1
    in_number = False
    total = 0
    for c in string:
        if c == "-":
            in_number = True
            sign = -1
        elif c in "0123456789":
            if not in_number:
                in_number = True
                sign = 1
            current = current * 10 + int(c)
        else:
            if in_number:
                total += current * sign
                current = 0
                in_number = False
    return total


def split(string):
    output = []
    level = 0
    current = ""
    for c in string:
        if c == "[" or c == "{":
            level += 1
        elif c == "]" or c == "}":
            level -= 1
        if c == "," and level == 0:
            output.append(current)
            current = ""
        else:
            current += c
    output.append(current)
    return output


def score(string, part_a):
    print(string)
    if string == "":
        return 0
    if string[0] == "[":
        assert string[-1] == "]"
        fields = split(string[1:-1])
        sum = 0
        for field in fields:
            sum += score(field, part_a)
        return sum
    elif string[0] == "{":
        assert string[-1] == "}"
        fields = split(string[1:-1])
        values = []
        for field in fields:
            print(field)
            value = field[field.find(":") + 1 :]
            values.append(value)
        if '"red"' in values and not part_a:
            return 0
        else:
            sum = 0
            for value in values:
                sum += score(value, part_a)
        return sum
    else:
        if string.isnumeric() or string[0] == "-" and string[1:].isnumeric():
            return int(string)
        else:
            return 0


def part_a(input):
    string = next(input_generator(input))

    return score(string, True)


def part_b(input):
    string = next(input_generator(input))

    return score(string, False)


if __name__ == "__main__":
    Run_2015_12().run_cmdline()
