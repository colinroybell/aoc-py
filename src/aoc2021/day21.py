from os import SCHED_OTHER
from utils.day_base import DayBase
from utils.data_input import input_generator
from collections import defaultdict


class Run_2021_21(DayBase):
    YEAR = "2021"
    DAY = "21"


class Die:
    def __init__(self):
        self.number = 100
        self.count = 0

    def roll(self):
        self.count += 1
        self.number += 1
        if self.number == 101:
            self.number = 1
        return self.number

    def num_rolls(self):
        return self.count


class Player:
    def __init__(self, pos):
        self.pos = pos
        self.score = 0


def part_a(input):
    players = []
    for line in input_generator(input):
        pos = int(line[-1])
        players.append(Player(pos))

    active = 0
    done = False
    score = None
    die = Die()
    while not done:
        move = (die.roll() + die.roll() + die.roll()) % 10
        players[active].pos += move
        if players[active].pos > 10:
            players[active].pos -= 10
        players[active].score += players[active].pos
        if players[active].score >= 1000:
            done = True
            score = players[1 - active].score * die.num_rolls()
        else:
            active = 1 - active
    return score


score_array = defaultdict(lambda: 0)


class State:
    def __init__(self, positions, turn, wins):
        self.positions = positions
        self.turn = turn
        self.states = defaultdict(lambda: 0)
        self.wins = wins

    def add_state(self, scores, weight):
        self.states[scores] += weight

    def done(self):
        return len(self.states) == 0

    def advance(self):
        next_state = State(self.positions, 1 - self.turn, self.wins[:])
        for state, weight in self.states.items():
            score = [state[0], state[1]]
            pos = [state[2], state[3]]

            for die, die_weight in score_array.items():
                new_score = score[:]
                new_pos = pos[:]
                new_weight = weight * die_weight
                new_pos[self.turn] += die

                if new_pos[self.turn] > 10:
                    new_pos[self.turn] -= 10
                new_score[self.turn] += new_pos[self.turn]
                if new_score[self.turn] >= 21:
                    next_state.wins[self.turn] += new_weight
                else:
                    next_state.add_state(
                        (new_score[0], new_score[1], new_pos[0], new_pos[1]), new_weight
                    )
        return next_state


def part_b(input):
    positions = []
    for line in input_generator(input):
        pos = int(line[-1])
        positions.append(pos)
    state = State(positions, 0, [0, 0])
    state.add_state((0, 0, positions[0], positions[1]), 1)
    if len(score_array) == 0:
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    score_array[a + b + c] += 1

    while not state.done():
        state = state.advance()
        print(state.wins)
    return max(state.wins)


if __name__ == "__main__":
    Run_2021_21().run_cmdline()
