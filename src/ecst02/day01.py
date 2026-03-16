from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_st02_01(DayBase):
    YEAR = "st02"
    DAY = "01"
    PREFIX = "ec"


class MaxStructure:
    def __init__(self, score_lists):
        self.lists = []
        for s in score_lists:
            pairs = [(i, val) for i, val in enumerate(s)]
            self.lists.append(sorted(pairs, key=lambda pairs: pairs[1], reverse=True))

    def max_possible(self, total, used):
        """Work out quick maximum for culling"""
        for s in self.lists[len(used) :]:
            i = 0
            while s[i][0] in used:
                i += 1
            total += s[i][1]
        return total

    def find_max(self):
        return self.find_max_recurse(None, 0, [])

    def find_max_recurse(self, maximum, total, used):
        if len(used) == len(self.lists):
            if maximum == None or total > maximum:
                return total
            else:
                return maximum
        if maximum != None and self.max_possible(total, used) <= maximum:
            # cull
            return maximum
        for score in self.lists[len(used)]:
            if score[0] not in used:
                new_used = used + [score[0]]
                maximum = self.find_max_recurse(maximum, total + score[1], new_used)
        return maximum


def process_run(grid, inst, slot, trace):
    if trace:
        assert trace[0] == inst
        assert trace[1] == slot

    pos = Vec2d(slot * 2 - 2, 0)
    instpos = 0
    while 1:
        c = grid.get(pos)
        if c == None:
            break
        elif c == "*":
            dir = inst[instpos]
            instpos += 1
            if dir == "R":
                adj = Vec2d(1, 0)
            else:
                adj = Vec2d(-1, 0)
            if grid.get(pos + adj) == ".":
                pos = pos + adj
            else:
                # bounce off the wall
                pos = pos - adj
        else:
            pos = pos + Vec2d(0, 1)

    assert pos.x % 2 == 0
    end_slot = pos.x // 2 + 1
    score = max(end_slot * 2 - slot, 0)
    if trace:
        assert trace[2] == end_slot
        assert trace[3] == score
    return score


def part_1(input, part=1, **kwargs):
    generator = input_generator(input)
    grid = Grid2d()
    (width, height) = grid.read_from_file_strings_generator(
        generator, stop_at_blank=True
    )

    insts = [line for line in generator]
    # Modification to get test1 to choose a slot
    if insts[0].startswith("slot"):
        fields = insts[0].split()
        first_slot = int(fields[1])
        insts = insts[1:]
    else:
        first_slot = 1

    traces = None
    if "trace" in kwargs:
        trace_generator = input_generator(kwargs["trace"])
        _ = next(trace_generator)
        traces = []
        for line in trace_generator:
            if not line:
                break
            fields = line.split()
            traces.append([fields[0], int(fields[1]), int(fields[2]), int(fields[3])])
        assert len(traces) == len(insts)

    total = 0
    if part == 1:
        for run in range(len(insts)):
            trace = None
            if traces:
                trace = traces[run]
            total += process_run(grid, insts[run], run + first_slot, trace)
        return total
    elif part == 2:
        slots = (width + 1) // 2
        for run in range(len(insts)):
            best_slot = None
            best_score = 0
            for slot in range(1, slots + 1):
                score = process_run(grid, insts[run], slot, None)
                if score > best_score:
                    best_slot = slot
                    best_score = score
            if traces:
                trace = traces[run]
                assert best_slot == trace[1]
                assert best_score == trace[3]
            total += best_score
        return total
    else:
        assert part == 3
        slots = (width + 1) // 2
        max_lists = []
        min_lists = []
        for run in range(len(insts)):
            max_list = []
            min_list = []
            for slot in range(1, slots + 1):
                score = process_run(grid, insts[run], slot, None)
                max_list.append(score)
                min_list.append(-score)
            max_lists.append(max_list)
            min_lists.append(min_list)
        max_calc = MaxStructure(max_lists)
        maximum = max_calc.find_max()
        min_calc = MaxStructure(min_lists)
        minimum = -min_calc.find_max()
        ret = "{} {}".format(minimum, maximum)
        return ret


def part_2(input, **kwargs):
    return part_1(input, part=2, **kwargs)


def part_3(input, **kwargs):
    return part_1(input, part=3, **kwargs)


if __name__ == "__main__":
    Run_st02_01().run_cmdline()
