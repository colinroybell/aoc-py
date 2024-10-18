import pytest
from aoc2020.day19 import Run_2020_19


class Test_2020_19:
    def setup_class(self):
        self.day = Run_2020_19()

    def test_regression_a(self):
        assert self.day.run_part("a") == 144

    def test_regression_b(self):
        assert self.day.run_part("b") == 260
