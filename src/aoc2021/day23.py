from utils.day_base import DayBase
from utils.data_input import input_generator
from queue import PriorityQueue


class Run_2021_23(DayBase):
    YEAR = "2021"
    DAY = "23"


class State:
    # note: X means one that's already placed
    seen = set()
    next_id = 0
    valid_halls = [0, 1, 3, 5, 7, 9, 10]
    room_length = 2

    def __init__(self):
        self.rooms = [""] * 4
        self.hall = ["."] * 11
        self.id = State.next_id
        State.next_id += 1
        self.rooms_done = 0

    def copy(self):
        state = State()
        state.rooms = self.rooms[:]
        state.hall = self.hall[:]
        state.rooms_done = self.rooms_done
        return state

    def mark_processed(self):
        State.seen.add((tuple(self.rooms), tuple(self.hall)))

    def already_processed(self):
        return (tuple(self.rooms), tuple(self.hall)) in State.seen

    def __lt__(self, other):
        return self.id < other.id

    def parse(self, input, part_b):
        generator = input_generator(input)
        mods = ["DD", "CB", "BA", "AC"]
        for count in range(4):
            line = next(generator)
            if part_b:
                line = line[0] + mods[count] + line[1]

            self.rooms[count] = line

    def move_room_room_cost_if_possible(self, r1, r2):
        loc1 = r1 * 2 + 2
        loc2 = r2 * 2 + 2

        min_ = min(loc1, loc2)
        max_ = max(loc1, loc2)

        for i in range(min_, max_ + 1):
            if self.hall[i] != ".":
                return None
        return (
            max_
            - min_
            + State.room_length
            + 1
            - len(self.rooms[r1])
            + State.room_length
            - len(self.rooms[r2])
        )

    def move_room_hall_cost_if_possible(self, r, h):
        loc1 = r * 2 + 2
        loc2 = h

        min_ = min(loc1, loc2)
        max_ = max(loc1, loc2)

        for i in range(min_, max_ + 1):
            if self.hall[i] != ".":
                return None
        return max_ - min_ + State.room_length + 1 - len(self.rooms[r])

    def move_hall_room_cost_if_possible(self, h, r):
        loc1 = r * 2 + 2
        loc2 = h

        min_ = min(loc1, loc2)
        max_ = max(loc1, loc2)

        for i in range(min_, max_ + 1):
            if h != i and self.hall[i] != ".":
                return None
        return max_ - min_ + State.room_length - len(self.rooms[r])

    def head_amp_in_room(self, r):
        if self.rooms[r] == "":
            return None
        if self.rooms[r][0] == "X":
            return None
        return self.rooms[r][0]

    def valid_move_to_room(self, r):
        if self.rooms[r] == "":
            return True
        if len(self.rooms[r]) == State.room_length:
            return False
        return self.rooms[r][0] == "X"

    def find_valid_moves(self):
        amp_to_room = {"A": 0, "B": 1, "C": 2, "D": 3}
        move_costs = {"A": 1, "B": 10, "C": 100, "D": 1000}

        move_states = []

        for r in range(4):
            amp = self.head_amp_in_room(r)
            if amp == None:
                continue
            target_room = amp_to_room[amp]
            if self.valid_move_to_room(target_room):
                cost = self.move_room_room_cost_if_possible(r, target_room)
                if cost:
                    cost *= move_costs[amp]
                    state = self.copy()
                    state.rooms[target_room] = "X" + state.rooms[target_room]
                    if (
                        len(state.rooms[target_room]) == State.room_length
                        and state.rooms[target_room][0] == "X"
                    ):
                        state.rooms_done += 1
                    state.rooms[r] = state.rooms[r][1:]
                    move_states.append((cost, state))
                    # print("R->R generates {} {}".format(cost,state))

            for h in self.valid_halls:
                cost = self.move_room_hall_cost_if_possible(r, h)
                if cost:
                    cost *= move_costs[amp]
                    state = self.copy()
                    state.hall[h] = amp
                    state.rooms[r] = state.rooms[r][1:]
                    move_states.append((cost, state))
                    # print("R->H generates {} {}".format(cost,state))

        for h in self.valid_halls:
            amp = self.hall[h]
            if amp == ".":
                continue
            target_room = amp_to_room[amp]
            if self.valid_move_to_room(target_room):
                cost = self.move_hall_room_cost_if_possible(h, target_room)
                if cost:
                    cost *= move_costs[amp]
                    state = self.copy()
                    state.rooms[target_room] = "X" + state.rooms[target_room]
                    if (
                        len(state.rooms[target_room]) == State.room_length
                        and state.rooms[target_room][0] == "X"
                    ):
                        state.rooms_done += 1
                    state.hall[h] = "."
                    move_states.append((cost, state))
                    # print("H->R generates {} {}".format(cost,state))

        return move_states

    def __str__(self):
        return "{}: {} {} {}".format(self.id, self.rooms, self.rooms_done, self.hall)

    def __repr__(self):
        return self.__str__()


def part_a(input, part_b=False):
    to_process = PriorityQueue()
    if part_b:
        State.room_length = 4
    else:
        State.room_length = 2
    start = State()

    start.parse(input, part_b)
    to_process.put((0, start))

    while not to_process.empty():
        (cost, state) = to_process.get()
        if state.already_processed():
            continue
        # print("Starting at {}, {}".format(cost,state))
        state.mark_processed()
        if state.rooms_done == 4:
            break
        new_states = state.find_valid_moves()
        for move in new_states:
            cost_delta, new_state = move
            if not new_state.already_processed():
                to_process.put((cost + cost_delta, new_state))

    return cost


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_23().run_cmdline()
