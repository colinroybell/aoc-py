import pytest
from aoc2025.day04 import Run_2025_04


class Test_2025_04:
    def setup_class(self):
        self.day = Run_2025_04()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 13

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 43

    def test_regression_a(self):
        assert self.day.run_part("a") == 1508

    def test_regression_b(self):
        assert self.day.run_part("b") == 8538
