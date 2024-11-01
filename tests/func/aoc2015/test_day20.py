import pytest
from aoc2015.day20 import Run_2015_20


class Test_2015_20:
    def setup_class(self):
        self.day = Run_2015_20()

    def test_regression_a(self):
        assert self.day.run_part("a") == 665280

    def test_regression_b(self):
        assert self.day.run_part("b") == 705600
