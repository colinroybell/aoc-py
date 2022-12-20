import pytest
from aoc2022.day04 import Run_2022_04


class Test_2022_04:
    def setup_class(self):
        self.day = Run_2022_04()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 2

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 4

    def test_regression_a(self):
        assert self.day.run_part("a") == 536

    def test_regression_b(self):
        assert self.day.run_part("b") == 845
