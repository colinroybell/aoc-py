from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2016_07(DayBase):
    YEAR = "2016"
    DAY = "07"

def tls(string):
    outers = []
    inners = []
    sections = string.split('[')
    outers.append(sections[0])
    for s in sections[1:]:
        i,o = s.split(']')
        inners.append(i)
        outers.append(o)

    print("i:",inners)
    for i in inners:
        if abba(i):
            print("failed",i)
            return False
    print("o:", outers)
    for o in outers:
        if abba(o):
            print("passed",o)
            return True
    print("nothing")            
    return False

def ssl(string):
    outers = []
    inners = []
    sections = string.split('[')
    outers.append(sections[0])
    for s in sections[1:]:
        i,o = s.split(']')
        inners.append(i)
        outers.append(o)
    babs = set()    
    for o in outers:
        for n in range(len(o)-2):
            s = o[n:n+3]
            if s[0] == s[2] and s[0] != s[1]:
                bab = s[1]+s[0]+s[1]
                babs.add(bab)           
    for i in inners:
        for n in range(len(i)-2):
            s = i[n:n+3]
            if s in babs:
                return True
    return False                    
                
                


def abba(string):
    for i in range(len(string)-3):
        s = string[i:i+4]
        if s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
            return True
    return False        

def part_a(input):
    total = 0
    for line in input_generator(input):
        if tls(line):
            total+=1
    return total    


def part_b(input):
    total = 0
    for line in input_generator(input):
        if ssl(line):
            total+=1
    return total    


if __name__ == "__main__":
    Run_2016_07().run_cmdline()
