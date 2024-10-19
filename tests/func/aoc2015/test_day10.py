import pytest
from aoc2015.day10 import Run_2015_10


class Test_2015_10:
    def setup_class(self):
        self.day = Run_2015_10()

    def test_regression_a(self):
        assert self.day.run_part("a") == 360154

    def test_regression_b(self):
        assert self.day.run_part("b") == 5103798
