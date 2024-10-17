import pytest
from aoc2020.day06 import Run_2020_06


class Test_2020_06:
    def setup_class(self):
        self.day = Run_2020_06()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 11

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 6

    def test_regression_a(self):
        assert self.day.run_part("a") == 6763

    def test_regression_b(self):
        assert self.day.run_part("b") == 3512
