import pytest
from aoc2023.day09 import Run_2023_09


class Test_2023_09:
    def setup_class(self):
        self.day = Run_2023_09()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 114

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 2

    def test_regression_a(self):
        assert self.day.run_part("a") == 2008960228

    def test_regression_b(self):
        assert self.day.run_part("b") == 1097
