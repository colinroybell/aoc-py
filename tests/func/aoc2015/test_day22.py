import pytest
from aoc2015.day22 import Run_2015_22


class Test_2015_22:
    def setup_class(self):
        self.day = Run_2015_22()

    def test_regression_a(self):
        assert self.day.run_part("a") == 1269

    def test_regression_b(self):
        assert self.day.run_part("b") == 1309
