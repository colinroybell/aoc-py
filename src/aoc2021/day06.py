from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2021_06(DayBase):
    YEAR = "2021"
    DAY = "06"


def part_a(input, days=80):
    line = next(input_generator(input))
    words=line.split(',')
    state = [int(word) for word in words]
    for day in range(0,days):
        new_state = []
        for fish in state:
            if fish > 0:
                new_state.append(fish-1)
            else:
                # Note: this puts things in the middle of the list, not at the end, but that's fine for counting
                new_state.append(6)
                new_state.append(8)
        state = new_state
        print(new_state)
    return len(state)                

def part_b(input,days=256):
    line = next(input_generator(input))
    counts = [0] * 9
    words=line.split(',')
    for word in words:
        counts[int(word)]+=1
    for day in range(0,days):
        split = counts[0]
        counts = counts[1:]
        counts.append(split)
        counts[6] += split
    return sum(counts)    
        



if __name__ == "__main__":
    Run_2021_06().run_cmdline()
