import pytest
from aoc2020.day08 import Run_2020_08


class Test_2020_08:
    def setup_class(self):
        self.day = Run_2020_08()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 5

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 8

    def test_regression_a(self):
        assert self.day.run_part("a") == 1594

    def test_regression_b(self):
        assert self.day.run_part("b") == 758
