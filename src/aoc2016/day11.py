from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2016_11(DayBase):
    YEAR = "2016"
    DAY = "11"


# chip is 0, generator is 1


class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type  # "chip" or "generator"

    def __hash__(self):
        return hash((self.name, self.type))

    def __repr__(self):
        return "{} {}".format(self.name, self.type)


class State:
    def __init__(self, elevator, floors):
        self.elevator = elevator
        self.floors = floors

    def complete(self):
        for f in range(4):
            if self.floors[f]:
                return False
        return True

    def valid(self):
        for f in self.floors:
            for item in f:
                match_generator = False
                other_generator = False
                if item.type == "microchip":
                    for other in f:
                        if other.type == "generator":
                            if other.name == item.name:
                                match_generator = True
                            else:
                                other_generator = True
                    if other_generator and not match_generator:
                        return False
        return True

    def moves(self):
        new_states = []
        # single items
        new_el = []
        if self.elevator > 1:
            new_el.append(self.elevator - 1)
        if self.elevator < 4:
            new_el.append(self.elevator + 1)

        el_floor = self.floors[self.elevator]
        # Single
        for item in el_floor:
            for item2 in el_floor:
                for el in new_el:
                    new_floors = [set() for _ in range(5)]
                    for f in range(1, 5):
                        for it in self.floors[f]:
                            new_floors[f].add(it)

                    # print(item,self.elevator,new_floors)
                    new_floors[self.elevator].remove(item)
                    new_floors[el].add(item)
                    if item2 != item:
                        new_floors[self.elevator].remove(item2)
                        new_floors[el].add(item2)

                    if item != item2 and el > self.elevator:
                        new_states.append(State(el, new_floors))
                    if item == item2 and el < self.elevator:
                        new_states.append(State(el, new_floors))
        return new_states

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        string = "{}".format(self.elevator)
        for f in range(1, 5):
            string += "[{} {}]".format(f, self.floors[f])
        return string


def part_a(input):
    floors = [set() for _ in range(5)]
    floor = 1
    for line in input_generator(input):
        phrases = line.split(",")
        for p in phrases:
            words = p.split(" ")
            if words[0] == "The":
                words = words[4:]
            if words[1] == "and":
                words = words[2:]
            if words[0] == "":
                words = words[1:]
            if words[0] == "nothing":
                break
            print(words)
            type = words[2]
            if type[-1] == ".":
                type = type[:-1]
            if type == "microchip":
                name = words[1].split("-")[0]
            else:
                name = words[1]
            floors[floor].add(Item(name, type))
        floor += 1

    initial_state = State(1, floors)
    print(initial_state)

    done = {}
    queue = []
    queue.append((0, initial_state))
    rounds = 0
    time_report = None
    while queue:
        rounds += 1
        if 0 and rounds == 20:
            break
        (time, state) = queue[0]
        if time != time_report:
            print("time", time, "rounds", rounds)
            time_report = time

        queue = queue[1:]
        # print('State',time,state)
        if state.complete():
            print("Complete")
            return time
        if state.__repr__() in done:
            continue

        done[state.__repr__()] = time
        for new_state in state.moves():
            if new_state.__repr__() not in done:
                if new_state.valid():
                    queue.append((time + 1, new_state))
                else:
                    done[new_state] = "invalid"


def part_b(input):
    assert 0, "not implemented"


def notes():
    """
    Had to insert a comma before 'and' in test input. Ought to parse by counting words rather than splitting on commas.

    Pretty inefficient. We know that the items are equivalent, so could simplify state considerably.

    Second part is 61 - do first bit, then bring other bits up in a sensible order. Probably there's an analytical method?

    Hash stuff is not working with objects - this is worth finding out about.

    With the optimisation we put in (elevator going up always has two items, going down always has one) the number of steps is deterministic. Would be interesting to know if we can prove this.

    If not, a more efficient data structure would be to have a chip,generator pair as eg (1,3), then sort them lexicographically - this uses the items-are-equivalent property.
    """


if __name__ == "__main__":
    Run_2016_11().run_cmdline()
