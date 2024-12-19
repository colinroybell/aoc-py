import pytest
from aoc2024.day18 import Run_2024_18


class Test_2024_18:
    def setup_class(self):
        self.day = Run_2024_18()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", size=6, count=12) == 22

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1", size=6) == "6,1"

    def test_regression_a(self):
        assert self.day.run_part("a") == 416

    def test_regression_b(self):
        assert self.day.run_part("b") == "50,23"
