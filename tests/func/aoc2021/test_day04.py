import pytest
from aoc2021.day04 import Run_2021_04


class Test_2021_04:
    def setup_class(self):
        self.day = Run_2021_04()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 4512

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 1924

    def test_regression_a(self):
        assert self.day.run_part("a") == 2496

    def test_regression_b(self):
        assert self.day.run_part("b") == 25925
