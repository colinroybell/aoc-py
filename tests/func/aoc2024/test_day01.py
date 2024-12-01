import pytest
from aoc2024.day01 import Run_2024_01


class Test_2024_01:
    def setup_class(self):
        self.day = Run_2024_01()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 11

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 31

    def test_regression_a(self):
        assert self.day.run_part("a") == 2192892

    def test_regression_b(self):
        assert self.day.run_part("b") == 22962826
