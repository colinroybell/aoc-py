import pytest
from aoc2021.day17 import Run_2021_17


class Test_2021_17:
    def setup_class(self):
        self.day = Run_2021_17()

    def test_bringup_a(self):
        assert self.day.run_part("a", ["x=20..30, y=-10..-5"]) == 45

    def test_bringup_b(self):
        assert self.day.run_part("b", ["x=20..30, y=-10..-5"]) == 112

    def test_regression_a(self):
        assert self.day.run_part("a") == 9180

    def test_regression_b(self):
        assert self.day.run_part("b") == 3767
