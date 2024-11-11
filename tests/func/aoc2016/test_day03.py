import pytest
from aoc2016.day03 import Run_2016_03


class Test_2016_03:
    def setup_class(self):
        self.day = Run_2016_03()

    def test_regression_a(self):
        assert self.day.run_part("a") == 982

    def test_regression_b(self):
        assert self.day.run_part("b") == 1826
