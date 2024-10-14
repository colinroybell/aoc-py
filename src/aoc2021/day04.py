from typing import ValuesView
from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2021_04(DayBase):
    YEAR = "2021"
    DAY = "04"


class Board:
    # assume square
    board_size = 5

    def __init__(self, lines):
        self.entries = []
        self.col_hit = []
        self.row_hit = []
        self.unhit_total = 0
        self.done = False
        for line in lines:
            words = line.split()
            entry = []
            for word in words:
                val = int(word)
                entry.append(val)
                self.unhit_total += val
            self.entries.append(entry)
            self.col_hit.append(0)
            self.row_hit.append(0)

    def call(self, N):
        """Returns (hit, score)"""
        if self.done:
            # Don't continue once won: needed for part B
            return (False, 0)
        for col in range(0, Board.board_size):
            for row in range(0, Board.board_size):
                if self.entries[col][row] == N:
                    self.col_hit[col] += 1
                    self.row_hit[row] += 1
                    self.unhit_total -= N
                    if (
                        self.col_hit[col] == Board.board_size
                        or self.row_hit[row] == Board.board_size
                    ):
                        self.done = True
                        return (True, self.unhit_total * N)
        return (False, 0)


def part_a(input, part_b=False):
    generator = input_generator(input)
    numbers = next(generator)
    _ = next(generator)  # blank
    boards = []
    lines = []
    for line in generator:
        lines.append(line)
        if len(lines) == 5:
            boards.append(Board(lines))
            lines = []
            # No blank line at end
            try:
                _ = next(generator)  # blank
            except StopIteration:
                break
    words = numbers.split(",")
    boards_done = 0
    for word in words:
        N = int(word)
        for board in boards:
            (result, score) = board.call(N)
            if result:
                boards_done += 1
                if part_b == False:
                    if boards_done == 1:
                        return score
                else:
                    if boards_done == len(boards):
                        return score
    assert 0, "no bingo"


def part_b(input):
    return part_a(input, True)


if __name__ == "__main__":
    Run_2021_04().run_cmdline()
