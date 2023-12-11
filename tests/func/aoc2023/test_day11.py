import pytest
from aoc2023.day11 import Run_2023_11


class Test_2023_11:
    def setup_class(self):
        self.day = Run_2023_11()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 374

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test1", expansion_factor=10) == 1030

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test1", expansion_factor=100) == 8410

    def test_regression_a(self):
        assert self.day.run_part("a") == 9965032

    def test_regression_b(self):
        assert self.day.run_part("b") == 550358864332
