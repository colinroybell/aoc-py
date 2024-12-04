import pytest
from aoc2024.day04 import Run_2024_04


class Test_2024_04:
    def setup_class(self):
        self.day = Run_2024_04()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 4

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 18

    def test_bringup_b(self):
        assert self.day.run_part("b", "test2") == 9

    def test_regression_a(self):
        assert self.day.run_part("a") == 2406

    def test_regression_b(self):
        assert self.day.run_part("b") == 1807
