import pytest
from aoc2016.day01 import Run_2016_01


class Test_2016_01:
    def setup_class(self):
        self.day = Run_2016_01()

    def test_bringup_a(self):
        assert self.day.run_part("a", ["R2, L3"]) == 5
        assert self.day.run_part("a", ["R2, R2, R2"]) == 2
        assert self.day.run_part("a", ["R5, L5, R5, R3"]) == 12

    def test_bringup_b(self):
        assert self.day.run_part("b", ["R8, R4, R4, R8"]) == 4

    def test_regression_a(self):
        assert self.day.run_part("a") == 234

    def test_regression_b(self):
        assert self.day.run_part("b") == 113
