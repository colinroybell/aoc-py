from utils.day_base import DayBase
from utils.data_input import input_generator


# This link gives the chemical element tables and transitions.
# https://les-mathematiques.net/vanilla/uploads/editor/j3/70da7l3911wx.pdf


class Run_2015_10(DayBase):
    YEAR = "2015"
    DAY = "10"

def update(string):
    last = None
    count = 0
    output = ""
    for s in string:
        if s == last:
            count += 1
        else:
            if last != None:
                output += "{}{}".format(count,last)
            last = s
            count = 1
    output += "{}{}".format(count,last)                
    return output

def part_a(input, part_b = False):
    string = next(input_generator(input))
    rounds = 40
    if part_b:
        rounds = 50
    for _ in range(rounds):
        string = update(string)
    return len(string)    

def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2015_10().run_cmdline()
