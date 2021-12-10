import pytest
from aoc2021.day10 import Run_2021_10


class Test_2021_10:
    def setup_class(self):
        self.day = Run_2021_10()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 26397

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 288957

    def test_regression_a(self):
        assert self.day.run_part("a") == 392043

    def test_regression_b(self):
        assert self.day.run_part("b") == 1605968119
