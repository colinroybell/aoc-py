import pytest
from aoc2015.day16 import Run_2015_16


class Test_2015_16:
    def setup_class(self):
        self.day = Run_2015_16()

    def test_regression_a(self):
        assert self.day.run_part("a") == 213

    def test_regression_b(self):
        assert self.day.run_part("b") == 323
