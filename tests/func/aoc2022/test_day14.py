import pytest
from aoc2022.day14 import Run_2022_14


class Test_2022_14:
    def setup_class(self):
        self.day = Run_2022_14()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 24

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 93

    def test_regression_a(self):
        assert self.day.run_part("a") == 808

    def test_regression_b(self):
        assert self.day.run_part("b") == 26625
