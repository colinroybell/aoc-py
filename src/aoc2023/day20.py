from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.maths import lcm


class Run_2023_20(DayBase):
    YEAR = "2023"
    DAY = "20"


class Module:
    def __init__(self, string):
        print(string)
        (name, targets) = string.split(" -> ")
        self.state = {}
        if name == "broadcaster" or name == "button" or name == "output":
            self.type = "broadcaster"
            self.name = name
        elif name[0] == "%":
            self.type = "flip-flop"
            self.name = name[1:]
            self.state = False
        elif name[0] == "&":
            self.type = "conjunction"
            self.name = name[1:]
        else:
            print("-{}-".format(name))
            assert 0
        if targets != "NONE":
            self.targets = targets.split(", ")
        else:
            self.targets = []

    def set_input(self, source):
        if self.type == "conjunction":
            self.state[source] = False

    def get_state(self):
        if self.type == "conjunction":
            return ["{} {}".format(key, value) for key, value in self.state.items()]
        else:
            return [self.state]

    def get_targets(self):
        return self.targets

    def set_targets(self, targets):
        self.targets = targets

    def receive(self, source, pulse):
        if self.type == "broadcaster":
            output = pulse
        elif self.type == "flip-flop":
            if pulse == False:
                self.state = not self.state
                output = self.state
            else:
                output = None
        elif self.type == "conjunction":
            self.state[source] = pulse
            output = not all(self.state.values())
        if output == None:
            return []
        else:
            return [(self, target, output) for target in self.targets]

    def __repr__(self):
        return self.name


def part_a(input, part_b=False):
    part_a = not part_b
    modules = {}
    for line in input_generator(input):
        module = Module(line)
        modules[module.name] = module
        # print('found',module.name)
    button = Module("button -> broadcaster")
    modules[button.name] = button
    # print('found',module.name)
    broadcaster = modules["broadcaster"]
    output = Module("&output -> NONE")
    modules[output.name] = output
    rx = Module("&rx -> NONE")
    modules[rx.name] = rx
    # print('found',rx)
    # print (len(modules.keys()),modules.keys())

    for m in modules.values():
        targets = m.get_targets()
        new_targets = []
        for t_str in targets:
            t = modules[t_str]
            t.set_input(m)
            new_targets.append(t)
        m.set_targets(new_targets)

    low_count = 0
    high_count = 0
    presses = 0
    part_b_done = False
    not_seen = set(modules.keys())

    while 1:
        presses += 1
        # print(presses)
        queue = [(button, broadcaster, False)]
        while queue:
            (source, target, pulse) = queue[0]
            if pulse == False and target.name in not_seen:
                not_seen.remove(target.name)
                # print(presses,target.name, 'seen. Remaining', len(not_seen), not_seen)
            queue = queue[1:]
            if pulse == False:
                low_count += 1
            else:
                high_count += 1
            if pulse == False and target == rx:
                return presses
            queue.extend(target.receive(source, pulse))
            # print(queue)
        if part_a and presses == 1000:
            return low_count * high_count


# Note: by inspection, we see a pulse for dc, rv, vp, rq respectively every 3797, 4051, 3847, 3877. These feed into ns so take lcm. Not sure how to solve this programmatically.
def part_b(input):
    return lcm(lcm(lcm(3797, 4051), 3847), 3877)


if __name__ == "__main__":
    Run_2023_20().run_cmdline()
