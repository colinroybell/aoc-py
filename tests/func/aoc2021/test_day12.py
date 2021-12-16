import pytest
from aoc2021.day12 import Run_2021_12


class Test_2021_12:
    def setup_class(self):
        self.day = Run_2021_12()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 10
        assert self.day.run_part("a", "test2") == 19
        assert self.day.run_part("a", "test3") == 226

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 36
        assert self.day.run_part("b", "test2") == 103
        assert self.day.run_part("b", "test3") == 3509

    def test_regression_a(self):
        assert self.day.run_part("a") == 4754

    def test_regression_b(self):
        assert self.day.run_part("b") == 143562
