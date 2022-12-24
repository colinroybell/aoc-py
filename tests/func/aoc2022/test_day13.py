import pytest
from aoc2022.day13 import Run_2022_13


class Test_2022_13:
    def setup_class(self):
        self.day = Run_2022_13()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 13

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 140

    def test_regression_a(self):
        assert self.day.run_part("a") == 6395

    def test_regression_b(self):
        assert self.day.run_part("b") == 24921
