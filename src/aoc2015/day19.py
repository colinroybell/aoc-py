from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2015_19(DayBase):
    YEAR = "2015"
    DAY = "19"


def replacement(string, transitions):
    outputs = set()
    for (t0, t1) in transitions:
        length = len(t0)
        for m in re.finditer(t0, string):
            new_string = string[: m.start()] + t1 + string[m.end() :]
            outputs.add(new_string)
    return len(outputs)


def backward_steps(inputs, transitions):
    outputs = set()
    for (t0, t1) in transitions:
        length = len(t1)
        for string in inputs:
            for m in re.finditer(t1, string):
                new_string = string[: m.start()] + t0 + string[m.end() :]
                outputs.add(new_string)
    return outputs


def part_a(input):
    transitions = []
    transitions_collection = True
    for line in input_generator(input):
        if transitions_collection:
            if line == "":
                transitions_collection = False
            else:
                fields = line.split(" => ")
                transitions.append((fields[0], fields[1]))
        else:
            return replacement(line, transitions)


def part_b(input):
    transitions = []
    transitions_collection = True
    for line in input_generator(input):
        if transitions_collection:
            if line == "":
                transitions_collection = False
            else:
                fields = line.split(" => ")
                transitions.append((fields[0], fields[1]))
        else:
            molecules = set()
            molecules.add(line)
            step = 0
            while "e" not in molecules:
                molecules = backward_steps(molecules, transitions)
                step += 1
                print(step, len(molecules))
            return step


if __name__ == "__main__":
    Run_2015_19().run_cmdline()

# Idea: at top level work out a list of first steps. Take the best one, come up with a new list below. Backtrack and ensure we block out rejected ones. Also never do an e one unless that's everything.
# Parsing in such a way that we break into the elements first might be nice, but not essential.
