import pytest
from aoc2022.day18 import Run_2022_18


class Test_2022_18:
    def setup_class(self):
        self.day = Run_2022_18()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 64
        assert self.day.run_part("a", "test2") == 10

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 58
        assert self.day.run_part("b", "test2") == 10

    def test_regression_a(self):
        assert self.day.run_part("a") == 3576

    def test_regression_b(self):
        assert self.day.run_part("b") == 2066
