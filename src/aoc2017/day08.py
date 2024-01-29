from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_08(DayBase):
    YEAR = "2017"
    DAY = "08"


def part_a(input, part_b=False):
    part_a = not part_b
    values = {}
    max2_ = 0
    for line in input_generator(input):
        array = line.split()

        var1 = array[0]
        incdec = array[1]
        val1 = array[2]
        var2 = array[4]
        cond = array[5]
        val2 = array[6]

        if var1 not in values:
            values[var1] = 0
            print("New variable {}".format(var1))
        if var2 not in values:
            values[var2] = 0
            print("New variable {}".format(var2))
        change = int(val1)
        if incdec == "dec":
            change *= -1
        condition = str(values[var2]) + " " + cond + " " + val2
        if eval(condition):
            print(
                "{} true (v = {}), adding {} to {}".format(
                    condition, values[var2], change, var1
                )
            )
            values[var1] += change
            if (values[var1]) > max2_:
                max2_ = values[var1]
        else:
            print("{} false (v = {})".format(condition, values[var2]))

    max_ = 0
    for var in values:
        if values[var] > max_:
            max_ = values[var]
    if part_a:
        return max_
    else:
        return max2_


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2017_08().run_cmdline()
