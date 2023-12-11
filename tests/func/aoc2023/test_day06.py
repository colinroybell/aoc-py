import pytest
from aoc2023.day06 import Run_2023_06


class Test_2023_06:
    def setup_class(self):
        self.day = Run_2023_06()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 288

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 71503

    def test_regression_a(self):
        assert self.day.run_part("a") == 1312850

    def test_regression_b(self):
        assert self.day.run_part("b") == 36749103
