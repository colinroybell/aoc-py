import pytest
from aoc2017.day10 import Run_2017_10


class Test_2017_10:
    def setup_class(self):
        self.day = Run_2017_10()

    def test_bringup_a(self):
        assert self.day.run_part("a", ["3, 4, 1, 5"], length=5) == 12

    def test_bringup_b_1(self):
        assert self.day.run_part("b", [""]) == "a2582a3a0e66e6e86e3812dcb672a272"

    def test_bringup_b_2(self):
        assert (
            self.day.run_part("b", ["AoC 2017"]) == "33efeb34ea91902bb2f59c9920caa6cd"
        )

    def test_bringup_b_3(self):
        assert self.day.run_part("b", ["1,2,3"]) == "3efbe78a8d82f29979031a4aa0b16a9d"

    def test_bringup_b_4(self):
        assert self.day.run_part("b", ["1,2,4"]) == "63960835bcdc130f0b66d7ff4f6a5a8e"

    def test_regression_a(self):
        assert self.day.run_part("a") == 19591

    def test_regression_b(self):
        assert self.day.run_part("b") == "62e2204d2ca4f4924f6e7a80f1288786"
