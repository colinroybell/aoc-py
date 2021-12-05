import pytest
from aoc2021.day05 import Run_2021_05


class Test_2021_05:
    def setup_class(self):
        self.day = Run_2021_05()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 5

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 12

    def test_regression_a(self):
        assert self.day.run_part("a") == 6397

    def test_regression_b(self):
        assert self.day.run_part("b") == 22335
