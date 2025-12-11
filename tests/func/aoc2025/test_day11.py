import pytest
from aoc2025.day11 import Run_2025_11


class Test_2025_11:
    def setup_class(self):
        self.day = Run_2025_11()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 5

    def test_bringup_b(self):
        assert self.day.run_part("b", "test2") == 2

    def test_regression_a(self):
        assert self.day.run_part("a") == 506

    def test_regression_b(self):
        assert self.day.run_part("b") == 385912350172800
