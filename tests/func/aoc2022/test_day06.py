import pytest
from aoc2022.day06 import Run_2022_06


class Test_2022_06:
    def setup_class(self):
        self.day = Run_2022_06()

    def test_bringup_a(self):
        assert self.day.run_part("a", ["bvwbjplbgvbhsrlpgdmjqwftvncz"]) == 5
        assert self.day.run_part("a", ["nppdvjthqldpwncqszvftbrmjlhg"]) == 6
        assert self.day.run_part("a", ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]) == 10
        assert self.day.run_part("a", ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]) == 11

    def test_bringup_b(self):
        assert self.day.run_part("b", ["mjqjpqmgbljsphdztnvjfqwrcgsmlb"]) == 19
        assert self.day.run_part("b", ["bvwbjplbgvbhsrlpgdmjqwftvncz"]) == 23
        assert self.day.run_part("b", ["nppdvjthqldpwncqszvftbrmjlhg"]) == 23
        assert self.day.run_part("b", ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]) == 29
        assert self.day.run_part("b", ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]) == 26

    def test_regression_a(self):
        assert self.day.run_part("a") == 1757

    def test_regression_b(self):
        assert self.day.run_part("b") == 2950
