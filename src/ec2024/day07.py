from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_07(DayBase):
    YEAR = "2024"
    DAY = "07"
    PREFIX = "ec"

class Squire:
    def __init__(self,name,plan):
        self.name = name
        self.power = 10
        self.plan = plan
        self.score = 0

    def update_power(self,time, force = None):
        pos = (time-1) % len(self.plan)
        c = self.plan[pos]
        if force == '+' or force == '-':
            c = force
        if c == '+':
            self.power += 1
        elif c == '-' and self.power > 0:
            self.power -= 1
        self.score += self.power    



def part_1(input):
    squires = {}
    for line in input_generator(input):
        name = line[0]
        plan = line[2:].split(',')
        squires[name] = Squire(name, plan)

    for time in range(1,11):
        for s in squires.values():
            s.update_power(time)

    return ''.join(sorted(squires, key=lambda key: squires[key].score, reverse=True))        

def part_2(input):
    track = ""
    end_track = ""
    track_done = False
    first = True
    squires = {}
    for line in input_generator(input):
        if first:
            track = line[1:]
            end_track = line[0]
            first = False
        elif not track_done:
            if ' ' in line:
                track += line[-1]
                end_track = line[0] + end_track
            else:
                track += line[::-1] + end_track
                track_done = True
        else:
            if line == '':
                next       
            else:
                name = line[0]
                plan = line[2:].split(',')
                squires[name] = Squire(name, plan)
    time = 0
    for loop in range(10):
        for t in track:
            time += 1
            for s in squires.values():
                s.update_power(time, force = t)
    return ''.join(sorted(squires, key=lambda key: squires[key].score, reverse=True))        

def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2024_07().run_cmdline()
