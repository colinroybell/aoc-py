import pytest
from aoc2017.day12 import Run_2017_12


class Test_2017_12:
    def setup_class(self):
        self.day = Run_2017_12()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 6

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 2

    def test_regression_a(self):
        assert self.day.run_part("a") == 288

    def test_regression_b(self):
        assert self.day.run_part("b") == 211
