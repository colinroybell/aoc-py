import pytest
from aoc2015.day17 import Run_2015_17


class Test_2015_17:
    def setup_class(self):
        self.day = Run_2015_17()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", target=25) == 4

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1", target=25) == 3

    def test_regression_a(self):
        assert self.day.run_part("a") == 4372

    def test_regression_b(self):
        assert self.day.run_part("b") == 4
