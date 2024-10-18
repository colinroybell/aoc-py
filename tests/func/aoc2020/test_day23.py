import pytest
from aoc2020.day23 import Run_2020_23


class Test_2020_23:
    def setup_class(self):
        self.day = Run_2020_23()

    def test_regression_a(self):
        assert self.day.run_part("a") == 27956483

    def test_regression_b(self):
        assert self.day.run_part("b") == 18930983775
