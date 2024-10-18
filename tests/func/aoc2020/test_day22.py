import pytest
from aoc2020.day22 import Run_2020_22


class Test_2020_22:
    def setup_class(self):
        self.day = Run_2020_22()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 306

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 291

    def test_regression_a(self):
        assert self.day.run_part("a") == 34664

    def test_regression_b(self):
        assert self.day.run_part("b") == 32018
