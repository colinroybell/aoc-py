from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_05(DayBase):
    YEAR = "2015"
    DAY = "05"


def nice(string):
    if sum([string.count(v) for v in 'aeiou'])<3:
        return False
    if sum([string.count(v) for v in ['ab','cd','pq','xy']]):
        return False
    for p in range(len(string)-1):
        if string[p] == string[p+1]:
            return True
    return False            

def nice_b(string):
    rule_1 = False
    for i in range(len(string)-3):
        p1 = string[i:i+2]
        for j in range(i+2,len(string)-1):
            p2 = string[j:j+2]
            if p1 == p2:
                rule_1 = True
                break
        if rule_1:
            break
    if not rule_1:
            return False
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False                        


    


def part_a(input):
    count = 0
    for line in input_generator(input):
        if nice(line):
            count+=1
    return count



def part_b(input):
    count = 0
    for line in input_generator(input):
        if nice_b(line):
            count+=1
    return count
    


if __name__ == "__main__":
    Run_2015_05().run_cmdline()
