import pytest
from aoc2020.day13 import Run_2020_13


class Test_2020_13:
    def setup_class(self):
        self.day = Run_2020_13()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 295

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test1") == 1068781

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test2") == 3417

    def test_regression_a(self):
        assert self.day.run_part("a") == 1835

    def test_regression_b(self):
        assert self.day.run_part("b") == 247086664214628
