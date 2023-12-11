import pytest
from aoc2023.day08 import Run_2023_08


class Test_2023_08:
    def setup_class(self):
        self.day = Run_2023_08()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 2

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 6

    def test_bringup_b(self):
        assert self.day.run_part("b", "test3") == 6

    def test_regression_a(self):
        assert self.day.run_part("a") == 16271

    def test_regression_b(self):
        assert self.day.run_part("b") == 14265111103729
