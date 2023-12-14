from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2023_07(DayBase):
    YEAR = "2023"
    DAY = "07"


class Hand:

    ordering = "23456789TJQKA"

    def __init__(self, cards, bid):
        counts = [0] * 13
        self.cards = []
        self.cards_in = cards
        for i in range(5):
            print(__class__.__name__, __class__.ordering)
            rank = __class__.ordering.find(cards[i])
            self.cards.append(rank)
            counts[rank] += 1
        self.set_counts(counts)
        self.bid = bid

    def set_counts(self, counts):
        self.counts = sorted(counts, reverse=True)[:5]

    def __lt__(self, other):
        for i in range(5):
            if self.counts[i] < other.counts[i]:
                return True
            if self.counts[i] > other.counts[i]:
                return False
        for i in range(5):
            if self.cards[i] < other.cards[i]:
                return True
            if self.cards[i] > other.cards[i]:
                return False

    def __repr__(self):
        return f"{self.cards_in} {self.counts} {self.bid}"


# TODO: try and fix this so we don't need to redefine init


class HandB(Hand):
    ordering = "J23456789TQKA"

    def __init__(self, cards, bid):
        counts = [0] * 13
        self.cards = []
        self.cards_in = cards
        for i in range(5):
            print(__class__.__name__, __class__.ordering)
            rank = __class__.ordering.find(cards[i])
            self.cards.append(rank)
            counts[rank] += 1
        self.set_counts(counts)
        self.bid = bid

    def set_counts(self, counts):
        jokers = counts[0]
        counts[0] = 0
        self.counts = sorted(counts, reverse=True)[:5]
        self.counts[0] += jokers


def part_a(input, part_b=False):
    part_a = not part_b
    hands = []
    for line in input_generator(input):
        (cards, bid) = line.split()
        if part_a:
            hands.append(Hand(cards, int(bid)))
        else:
            hands.append(HandB(cards, int(bid)))
    hands.sort()
    print(hands)
    total = 0
    for i, hand in enumerate(hands):
        total += (i + 1) * hand.bid
    return total


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2023_07().run_cmdline()
