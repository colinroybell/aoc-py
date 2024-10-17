import pytest
from aoc2020.day09 import Run_2020_09


class Test_2020_09:
    def setup_class(self):
        self.day = Run_2020_09()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", count=5) == 127

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1", count=5) == 62

    def test_regression_a(self):
        assert self.day.run_part("a") == 57195069

    def test_regression_b(self):
        assert self.day.run_part("b") == 7409241
