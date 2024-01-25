import pytest
from aoc2017.day06 import Run_2017_06


class Test_2017_06:
    def setup_class(self):
        self.day = Run_2017_06()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 5

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 4

    def test_regression_a(self):
        assert self.day.run_part("a") == 14029

    def test_regression_b(self):
        assert self.day.run_part("b") == 2765
