import pytest
from aoc2021.day14 import Run_2021_14


class Test_2021_14:
    def setup_class(self):
        self.day = Run_2021_14()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 1588

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 2188189693529

    def test_regression_a(self):
        assert self.day.run_part("a") == 3906

    def test_regression_b(self):
        assert self.day.run_part("b") == 4441317262452
