from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2016_01(DayBase):
    YEAR = "2016"
    DAY = "01"


def part_a(input, part_b = False):
    line = next(input_generator(input))
    instructions = line.split(', ')
    x = 0 
    y = 0
    dir = "up"
    visited = set()
    done = False
    for instruction in instructions:
        turn = instruction[0]
        distance = int(instruction[1:])
        if turn == 'R':
            if dir == 'up':
                dir = 'right'
            elif dir == 'right':
                dir = 'down'
            elif dir == 'down':
                dir = 'left'    
            else: 
                assert(dir == 'left')
                dir = 'up'
        else:
            if dir == 'up':
                dir = 'left'
            elif dir == 'left':
                dir = 'down'
            elif dir == 'down':
                dir = 'right'    
            else: 
                assert(dir == 'right')
                dir = 'up'
        if part_b == False:        
            if dir == 'up':
                y += distance
            elif dir == 'right':
                x += distance 
            elif dir == 'down':
                y -= distance 
            else:    
                x -= distance
        else:
            for d in range(0,distance):
                if dir == 'up':
                    y += 1
                elif dir == 'right':
                    x += 1 
                elif dir == 'down':
                    y -= 1 
                else:    
                    x -= 1
                pos = (x,y)
                if pos in visited:
                    done = True
                    break
                else:
                    visited.add(pos)
        if done == True:
            break            

        print("turn {} distance {} dir {} position ({},{})".format(turn, distance, dir, x, y))
    return abs(x) + abs(y) 


def part_b(input):
    return part_a(input, part_b = True)


if __name__ == "__main__":
    Run_2016_01().run_cmdline()
