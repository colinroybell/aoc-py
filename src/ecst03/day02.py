from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d

class Run_st03_02(DayBase):
    YEAR = "st03"
    DAY = "02"
    PREFIX = "ec"

def update_grids(grid,adj_grid,pos):
    print("Setting",pos)
    grid.set(pos,'+')
    if adj_grid:
        for d in 'URDL':
            adj = pos.move(d)
            count = adj_grid.get(adj)
            count += 1
            adj_grid.set(adj,count)
            print("Setting adj",adj,count)
            if count == 4 and grid.get(adj) != '+':
                update_grids(grid,adj_grid,adj)

def part_1(input, part = 1):
    start = None
    target = None
    count_adj = 0
    for y,line in enumerate(input_generator(input)):
        for x,c in enumerate(line):
            if c == '#':
                target = Vec2d(x,y)
            if c == '@':
                start = Vec2d(x,y)

    assert(target)
    assert(start)
    grid = Grid2d()
    if part == 2:
        adj_grid = Grid2d(unset = 0)
    else:
        adj_grid = None    
    dirs = 'URDL'
    update_grids(grid,adj_grid,start)
    if part == 2:
        update_grids(grid,adj_grid,target)
    pos = start
    steps = 0
    last_steps = None
    while 1:
        if steps == 1000 or steps == last_steps:
            return 0
        last_steps = steps
        for d in dirs:
            new_pos = pos.move_y_flipped(d)
            if grid.get(new_pos) == None:
                pos = new_pos           
                update_grids(grid,adj_grid,new_pos)
                steps += 1
                pos = new_pos
                print(part,steps, pos, d, target.manhattan(pos))
                if part == 1:
                    if pos == target:
                        return steps 
                elif part == 2:
                    if adj_grid.get(target) == 4:
                        return steps
   


def part_2(input):
    return part_1(input, part = 2)


def part_3(input):
    assert 0, "not implemented"


if __name__ == "__main__":
    Run_st03_02().run_cmdline()
