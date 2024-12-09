import pytest
from aoc2016.day10 import Run_2016_10


class Test_2016_10:
    def setup_class(self):
        self.day = Run_2016_10()

    def test_regression_a(self):
        assert self.day.run_part("a") == 118

    def test_regression_b(self):
        assert self.day.run_part("b") == 143153
