import pytest
from aoc2020.day16 import Run_2020_16


class Test_2020_16:
    def setup_class(self):
        self.day = Run_2020_16()

    def test_regression_a(self):
        assert self.day.run_part("a") == 28884

    def test_regression_b(self):
        assert self.day.run_part("b") == 1001849322119
