from utils.day_base import DayBase
from utils.data_input import input_generator

class Run_2023_09(DayBase):
    YEAR='2023'
    DAY='09'


def part_a(input, part_b = False):
    part_a = not part_b
    total = 0
    for line in input_generator(input):
        numbers = line.split(' ')
        state = [[],[]]
        for n in numbers:
            state[1].append(int(n))

        while any(state[1]):
            print('down',state)
            new_state = [[],[]]
            new_state[0] = state[0]
            new_state[0].append(state[1][0])
            for i in range(len(state[1])-1):
                new_state[1].append(state[1][i+1]-state[1][i])
            state = new_state

        if part_a:
            state[1].append(0)
        else:
            state[1].insert(0,0)

        while len(state[0]):
            print('up',new_state)
            new_state = [[],[]]
            sum = state[0][-1]
            if part_b:
                sum -= state[1][0]
            new_state[0] = state[0][:-1]
            new_state[1].append(sum)
            for i in range(len(state[1])):
                sum += state[1][i]
                new_state[1].append(sum)
            state = new_state

        print('final',new_state)
        if part_a:
            total += state[1][-1]
        else:
            total += state[1][0]
    return total


    assert 0, "not implemented"

def part_b(input):
    return part_a(input, True)

if __name__ == "__main__":
    Run_2023_09().run_cmdline()
