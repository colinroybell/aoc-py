import pytest
from aoc2023.day01 import Run_2023_01


class Test_2023_01:
    def setup_class(self):
        self.day = Run_2023_01()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 142

    def test_bringup_b(self):
        assert self.day.run_part("b", "test2") == 281

    def test_regression_a(self):
        assert self.day.run_part("a") == 55123

    def test_regression_b(self):
        assert self.day.run_part("b") == 55260
