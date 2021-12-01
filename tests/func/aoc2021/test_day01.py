import pytest
from aoc2021.day01 import Run_2021_01


class Test_2021_01:
    def setup_class(self):
        self.day = Run_2021_01()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 7

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 5

    def test_regression_a(self):
        assert self.day.run_part("a") == 1655

    def test_regression_b(self):
        assert self.day.run_part("b") == 1683
