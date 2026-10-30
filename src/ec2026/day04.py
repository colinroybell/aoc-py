from utils.day_base import DayBase
from utils.data_input import input_generator

class Run_2026_04(DayBase):
    YEAR = "2026"
    DAY = "04"
    PREFIX = "ec"

def extract_n(string):
    fields = string.split('=')
    return int(fields[1])

def part_1(input):

    generator = input_generator(input)
    total = 0
    scores = {}
    for line in generator:
        values = [extract_n(s) for s in line.split(' ')]
        id = values[0]
        quest = values[1]
        part = values[2]
        time = values[3]
        if id not in scores:
            scores[id] = [0,0]
        scores[id][1] += time
        scores[id][0] += 1

    sorted_scores = sorted(scores.items(), key=lambda item:(-item[1][0],item[1][1]))

    print(sorted_scores)
    for i in range(len(sorted_scores)):
        total += (i+1) * sorted_scores[i][1][1]
    
    return total    

def part_2(input):
   return part_1(input)

def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_2026_04().run_cmdline()
