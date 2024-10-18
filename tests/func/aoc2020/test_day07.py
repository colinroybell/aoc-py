import pytest
from aoc2020.day07 import Run_2020_07


class Test_2020_07:
    def setup_class(self):
        self.day = Run_2020_07()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 4

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test1") == 32

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test2") == 126

    def test_regression_a(self):
        assert self.day.run_part("a") == 355

    def test_regression_b(self):
        assert self.day.run_part("b") == 5312
