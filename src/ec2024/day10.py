from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2024_10(DayBase):
    YEAR = "2024"
    DAY = "10"
    PREFIX = "ec"


# TODO: Not working. Think likely issue is that we're doing a first round solve on second round which is then filling in a ? so we need to check for this case.

# Fixed first round so we only check correct spaces. 
# Need to account for rule that everything is unique, which may address 42 18
# problem.

def grid_solve(grid, x_offset, y_offset, part):
    size = 8
    update = False
    for y in range(2, 6):
        for x in range(2, 6):
            if grid.get(Vec2d(x + x_offset, y + y_offset)) == ".":
                verts = []
                for yy in [0,1,6,7]:
                    s = grid.get(Vec2d(x + x_offset, yy + y_offset))
                    if s != "." and s != "*":
                        verts.append(s)
                for xx in [0,1,6,7]:
                    s = grid.get(Vec2d(xx + x_offset, y + y_offset))
                    if s in verts:
                        grid.set(Vec2d(x + x_offset, y + y_offset), s)
                        print(
                            "first round {} at {} {}".format(
                                s, x + x_offset, y + y_offset
                            )
                        )
                        update = True
                        break

    if part == 3:
        for y in range(2, 6):
            for x in range(2, 6):
                if grid.get(Vec2d(x + x_offset, y + y_offset)) == ".":
                    h_q = None
                    h_mult = False
                    print("h_q search", x + x_offset, y + y_offset)
                    for xx in [0, 1, 6, 7]:
                        if grid.get(Vec2d(xx + x_offset, y + y_offset)) == "?":
                            print("? at ", xx)
                            if h_q == None:
                                h_q = xx
                            else:
                                h_mult = True
                    if h_q != None and not h_mult:
                        print("h_q", x + x_offset, y + y_offset, h_q + x_offset)
                        ok = True
                        cands = []
                        for yy in [0, 1, 6, 7]:
                            c = grid.get(Vec2d(x + x_offset, yy + y_offset))
                            if ord(c) < 65 or ord(c) > 90:
                                ok = False
                                break
                            else:
                                cands.append(c)

                        if ok:
                            print("cands", x + x_offset, y + y_offset, cands)
                            for yy in range(2, 6):
                                if yy != y:
                                    c = grid.get(Vec2d(x + x_offset, yy + y_offset))
                                    pos = [
                                        i for i, x in enumerate(cands) if cands[i] == c
                                    ]
                                    if pos != []:
                                        cands.pop(pos[0])
                                        print("cull", pos[0], c, cands)
                            if ok:
                                val = cands[0]
                                print(
                                    "found {} at {} {} ? {} {}".format(
                                        val,
                                        x + x_offset,
                                        y + y_offset,
                                        h_q + x_offset,
                                        y + y_offset,
                                    )
                                )
                                grid.set(Vec2d(x + x_offset, y + y_offset), val)
                                grid.set(Vec2d(h_q + x_offset, y + y_offset), val)
                                update = True
                # Vertical
                if grid.get(Vec2d(x + x_offset, y + y_offset)) == ".":
                    v_q = None
                    v_mult = False
                    print("v_q search", x + x_offset, y + y_offset)
                    for yy in [0, 1, 6, 7]:
                        if grid.get(Vec2d(x + x_offset, yy + y_offset)) == "?":
                            print("? at ", yy)
                            if v_q == None:
                                v_q = xx
                            else:
                                v_mult = True
                    if v_q != None and not v_mult:
                        print("v_q", x + x_offset, y + y_offset, v_q + y_offset)
                        ok = True
                        cands = []
                        for xx in [0, 1, 6, 7]:
                            c = grid.get(Vec2d(xx + x_offset, y + y_offset))
                            if ord(c) < 65 or ord(c) > 90:
                                ok = False
                                break
                            else:
                                cands.append(c)

                        if ok:
                            print("cands", x + x_offset, y + y_offset, cands)
                            for xx in range(2, 6):
                                if xx != x:
                                    c = grid.get(Vec2d(xx + x_offset, y + y_offset))
                                    pos = [
                                        i for i, x in enumerate(cands) if cands[i] == c
                                    ]
                                    if pos == []:
                                        ok = False
                                        break
                                    cands.pop(pos[0])
                                    print("cull", pos[0], c, cands)
                            if ok:
                                val = cands[0]
                                print(
                                    "found {} at {} {} ? {} {}".format(
                                        val,
                                        x + x_offset,
                                        y + y_offset,
                                        x + x_offset,
                                        v_q + y_offset,
                                    )
                                )
                                grid.set(Vec2d(x + x_offset, y + y_offset), val)
                                grid.set(Vec2d(x + x_offset, v_q + y_offset), val)
                                update = True
        # Pick up extra ?
        for y in range (2,6):
            cands = []
            h_q = None
            for x in [0,1,6,7]:   
                c = grid.get(Vec2d(x + x_offset, y + y_offset)) 
                if c == "?":
                    print("h? case: ? at ", xx + x_offset, y+ y_offset)
                    if h_q == None:
                        h_q = xx
                    else:
                        h_mult = True
                else:
                    cands.append(c)        

            if h_q != None and not h_mult:
                ok = True
                for x in range(2,6):
                    c = grid.get(Vec2d(x+x_offset, y + y_offset))
                    print(cands,x,c)
                    if c != '.':
                        pos = [
                                i for i, x in enumerate(cands) if cands[i] == c
                            ]
                        if pos == []:
                            assert 0
                        cands.pop(pos[0])
                        print("cull", pos[0], c, cands)
                    else:
                        ok = False
                        break 
                if ok:
                    grid.set(Vec2d(h_q + x_offset, y+y_offset),pos[0])        




    return update


def grid_score(grid, x_offset, y_offset):
    count = 0
    score = 0
    for y in range(2, 6):
        for x in range(2, 6):
            s = grid.get(Vec2d(x + x_offset, y + y_offset))
            print(x + x_offset, y + y_offset, s)
            value = ord(s) - 64
            if value < 1 or value > 26:
                # Not solved
                return 0
            count += 1
            score += count * value
    print("score", score)
    return score


def grid_word(grid, x_offset, y_offset):
    word = ""
    for y in range(2, 6):
        for x in range(2, 6):
            s = grid.get(Vec2d(x + x_offset, y + y_offset))
            word += s
    return word


def part_1(input, part=1):
    grid = Grid2d()
    size = 8
    (x_max, y_max) = grid.read_from_file_strings(input, stop_at_blank=False)
    print(x_max, y_max)
    word = ""
    score = 0
    for y_offset in range(0, y_max + 1, 9):
        for x_offset in range(0, x_max + 1, 9):
            grid_solve(grid, x_offset, y_offset, part)
            score += grid_score(grid, x_offset, y_offset)
            word += grid_word(grid, x_offset, y_offset)

    if part == 1:
        return word
    else:
        return score


def part_2(input):
    return part_1(input, 2)


def part_3(input):
    grid = Grid2d()
    size = 8
    (x_max, y_max) = grid.read_from_file_strings(input, stop_at_blank=False)
    new_round = True
    while new_round:
        new_round = False
        for y_offset in range(0, y_max - 6, 6):
            for x_offset in range(0, x_max - 6, 6):
                print("solve", x_offset, y_offset)
                update = grid_solve(grid, x_offset, y_offset, 3)
                print("update", update)
                if update:
                    new_round = True

    score = 0
    for y_offset in range(0, y_max - 6, 6):
        for x_offset in range(0, x_max - 6, 6):
            print("score", x_offset, y_offset)
            score += grid_score(grid, x_offset, y_offset)
    return score


if __name__ == "__main__":
    Run_2024_10().run_cmdline()
