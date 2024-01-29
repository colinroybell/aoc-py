from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2017_18(DayBase):
    YEAR = "2017"
    DAY = "18"


def part_a(input):
    commands = []
    commands = [line for line in input_generator(input)]
    vars = {}

    def getVar(a):
        nonlocal vars
        try:
            return int(a)
        except ValueError:
            if a in vars:
                return vars[a]
            else:
                return 0

    def setVar(a, b):
        nonlocal vars
        print("Setting {} to {}".format(a, b))
        vars[a] = b

    pos = 0
    while True:
        if pos < 0:
            print("Off front")
            exit(0)
        elif pos > len(commands):
            print("Off back")
            exit(0)
        else:
            array = commands[pos].split(" ")
            print("{}: {}".format(pos, commands[pos]))
            if array[0] == "snd":
                lastFreq = getVar(array[1])
            elif array[0] == "set":
                setVar(array[1], getVar(array[2]))
            elif array[0] == "add":
                setVar(array[1], getVar(array[1]) + getVar(array[2]))
            elif array[0] == "mul":
                setVar(array[1], getVar(array[1]) * getVar(array[2]))
            elif array[0] == "mod":
                setVar(array[1], getVar(array[1]) % getVar(array[2]))
            elif array[0] == "rcv":
                if getVar(array[1]):
                    print("Recovering {}".format(lastFreq))
                    return lastFreq
            elif array[0] == "jgz":
                if getVar(array[1]) > 0:
                    pos += getVar(array[2]) - 1
                    print("Pos change to {}".format(pos))
            pos += 1


def part_b(input):
    commands = []
    vars = [{} for i in range(2)]

    vars[0]["p"] = 0
    vars[1]["p"] = 1

    commands = []
    commands = [line for line in input_generator(input)]

    lastFreq = 0

    # Can't get nonlocal prog here
    def getVar(prog, a):
        nonlocal vars
        try:
            return int(a)
        except ValueError:
            if a in vars[prog]:
                return vars[prog][a]
            else:
                return 0

    def setVar(prog, a, b):
        nonlocal vars
        print("Setting {} to {}".format(a, b))
        vars[prog][a] = b

    pos = [0] * 2
    queue = [[] for i in range(2)]

    deadlocked = 0
    sends1 = 0

    while deadlocked < 2:
        deadlocked = 0
        for prog in range(2):
            if pos[prog] < 0:
                print("Off front")
                exit(0)
            elif pos[prog] > len(commands):
                print("Off back")
                exit(0)
            else:
                array = commands[pos[prog]].split(" ")
                print("{} {}: {}".format(prog, pos[prog], commands[pos[prog]]))
                if array[0] == "snd":
                    queue[1 - prog].append(getVar(prog, array[1]))
                    if prog == 1:
                        sends1 += 1
                elif array[0] == "set":
                    setVar(prog, array[1], getVar(prog, array[2]))
                elif array[0] == "add":
                    setVar(
                        prog, array[1], getVar(prog, array[1]) + getVar(prog, array[2])
                    )
                elif array[0] == "mul":
                    setVar(
                        prog, array[1], getVar(prog, array[1]) * getVar(prog, array[2])
                    )
                elif array[0] == "mod":
                    setVar(
                        prog, array[1], getVar(prog, array[1]) % getVar(prog, array[2])
                    )
                elif array[0] == "rcv":
                    if len(queue[prog]) > 0:
                        setVar(prog, array[1], queue[prog][0])
                        queue[prog] = queue[prog][1:]
                    else:
                        deadlocked += 1
                        pos[prog] -= 1
                elif array[0] == "jgz":
                    if getVar(prog, array[1]) > 0:
                        pos[prog] += getVar(prog, array[2]) - 1
                        print("Pos change to {}".format(pos[prog]))
                pos[prog] += 1
    return sends1


if __name__ == "__main__":
    Run_2017_18().run_cmdline()
