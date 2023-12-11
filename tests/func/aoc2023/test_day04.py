import pytest
from aoc2023.day04 import Run_2023_04


class Test_2023_04:
    def setup_class(self):
        self.day = Run_2023_04()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 13

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 30

    def test_regression_a(self):
        assert self.day.run_part("a") == 25651

    def test_regression_b(self):
        assert self.day.run_part("b") == 19499881
