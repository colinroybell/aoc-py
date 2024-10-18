import pytest
from aoc2020.day12 import Run_2020_12


class Test_2020_12:
    def setup_class(self):
        self.day = Run_2020_12()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 25

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 286

    def test_regression_a(self):
        assert self.day.run_part("a") == 1956

    def test_regression_b(self):
        assert self.day.run_part("b") == 126797
