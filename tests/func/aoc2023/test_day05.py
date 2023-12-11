import pytest
from aoc2023.day05 import Run_2023_05


class Test_2023_05:
    def setup_class(self):
        self.day = Run_2023_05()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 35

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 46

    def test_regression_a(self):
        assert self.day.run_part("a") == 111627841

    def test_regression_b(self):
        assert self.day.run_part("b") == 69323688
