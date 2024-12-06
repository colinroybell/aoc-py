import pytest
from aoc2015.day23 import Run_2015_23


class Test_2015_23:
    def setup_class(self):
        self.day = Run_2015_23()

    def test_regression_a(self):
        assert self.day.run_part("a") == 170

    def test_regression_b(self):
        assert self.day.run_part("b") == 247
