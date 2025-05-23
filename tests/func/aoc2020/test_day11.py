import pytest
from aoc2020.day11 import Run_2020_11


class Test_2020_11:
    def setup_class(self):
        self.day = Run_2020_11()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 37

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 26

    def test_regression_a(self):
        assert self.day.run_part("a") == 2247

    def test_regression_b(self):
        assert self.day.run_part("b") == 2011
