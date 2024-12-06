import pytest
from aoc2015.day21 import Run_2015_21


class Test_2015_21:
    def setup_class(self):
        self.day = Run_2015_21()

    def test_regression_a(self):
        assert self.day.run_part("a") == 121

    def test_regression_b(self):
        assert self.day.run_part("b") == 201
