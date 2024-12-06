from utils.day_base import DayBase
from utils.data_input import input_generator
from queue import PriorityQueue


class Run_2015_22(DayBase):
    YEAR = "2015"
    DAY = "22"


class State:
    def __init__(self, hp=0, mana=0, boss_hp=0, boss_damage=0, hard_mode=False):
        self.turns = 0
        self.spent = 0
        self.hp = hp
        self.mana = mana
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.shield_turns = 0
        self.poison_turns = 0
        self.recharge_turns = 0
        self.won = False
        self.lost = False
        self.id = ""
        self.hard_mode = hard_mode

    def hash(self):
        return (
            self.hp,
            self.mana,
            self.boss_hp,
            self.shield_turns,
            self.poison_turns,
            self.recharge_turns,
        )

    def copy(self):
        new = State(
            hp=self.hp,
            mana=self.mana,
            boss_hp=self.boss_hp,
            boss_damage=self.boss_damage,
            hard_mode=self.hard_mode,
        )
        new.turns = self.turns
        new.spent = self.spent
        new.shield_turns = self.shield_turns
        new.poison_turns = self.poison_turns
        new.recharge_turns = self.recharge_turns
        new.won = self.won
        new.lost = self.lost
        new.id = self.id
        return new

    def __lt__(self, other):
        return 0

    def process_poison(self):
        if self.poison_turns > 0:
            self.boss_hp -= 3
            if self.boss_hp <= 0:
                self.won = True
            self.poison_turns -= 1

    def process_recharge(self):
        if self.recharge_turns > 0:
            self.mana += 101
            self.recharge_turns -= 1

    def advance(self):
        if self.won or self.lost:
            return
        self.turns += 1
        # Boss turn
        self.process_poison()
        self.process_recharge()
        if self.won:
            return
        effective_damage = self.boss_damage
        if self.shield_turns > 0:
            effective_damage -= 7
            self.shield_turns -= 1
        self.hp -= effective_damage
        if self.hp <= 0:
            self.lost = True
            return
        # Start of player turn
        if self.hard_mode:
            self.hp -= 1
            if self.hp <= 0:
                self.lost = True
                return
        self.process_poison()
        self.process_recharge()
        if self.won:
            return
        if self.shield_turns > 0:
            self.shield_turns -= 1

    def get_next_mm(self):
        if self.mana >= 53:
            new = self.copy()
            new.mana -= 53
            new.spent += 53
            new.boss_hp -= 4
            if new.boss_hp <= 0:
                new.won = True
            new.id += "M"
            return new
        else:
            return None

    def get_next_drain(self):
        # print("Considering drain",self.id,self.mana)
        if self.mana >= 73:
            new = self.copy()
            new.mana -= 73
            new.spent += 73
            new.boss_hp -= 2
            new.hp += 2
            if new.boss_hp <= 0:
                new.won = True
            new.id += "D"
            # print(new.id)
            return new
        else:
            return None

    def get_next_shield(self):
        if self.mana >= 113 and self.shield_turns == 0:
            new = self.copy()
            new.mana -= 113
            new.spent += 113
            new.shield_turns = 6
            new.id += "S"
            return new
        else:
            return None

    def get_next_poison(self):
        # print("Considering poison",self.id,self.mana,self.poison_turns)
        if self.mana >= 173 and self.poison_turns == 0:
            new = self.copy()
            new.mana -= 173
            new.spent += 173
            new.poison_turns = 6
            new.id += "P"
            # print("id",new.id)
            return new
        else:
            return None

    def get_next_recharge(self):
        if self.mana >= 229 and self.recharge_turns == 0:
            new = self.copy()
            new.mana -= 229
            new.spent += 229
            new.recharge_turns = 5
            new.id += "R"
            return new
        else:
            return None

    def get_next(self):
        functions = [
            self.get_next_mm,
            self.get_next_drain,
            self.get_next_shield,
            self.get_next_poison,
            self.get_next_recharge,
        ]
        nexts = []
        for f in functions:
            nexts.append(f())
        return nexts


def part_a(input, part_b=False):
    generator = input_generator(input)
    boss_hp = int(next(generator).split()[-1])
    boss_damage = int(next(generator).split()[-1])

    start_state = State(
        hp=50, mana=500, boss_hp=boss_hp, boss_damage=boss_damage, hard_mode=part_b
    )

    state_queue = PriorityQueue()
    state_queue.put((start_state.spent, start_state))
    cache = set()
    cache_spent = None
    while not state_queue.empty():
        (spent, state) = state_queue.get()
        print(
            "State at",
            state.spent,
            state.id,
            state.mana,
            state.hp,
            state.boss_hp,
            state.won,
            state.lost,
        )
        if spent != cache_spent:

            cache = set()
            cache_spent = spent
        h = state.hash()
        if h in cache:
            print("cached")
            continue
        cache.add(h)
        if state.won:
            return state.spent
        if state.id != "":
            state.advance()
        else:
            if part_b:
                state.hp -= 1
        # Win during advance
        if state.won:
            return state.spent
        # print("advance to",state.hash(),state.won,state.lost)
        nexts = state.get_next()
        for n in nexts:
            if n and not n.lost:
                # print("add",n.id)
                state_queue.put((n.spent, n))


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2015_22().run_cmdline()
