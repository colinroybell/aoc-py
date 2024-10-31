import pytest
from aoc2015.day15 import Run_2015_15


class Test_2015_15:
    def setup_class(self):
        self.day = Run_2015_15()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 62842880

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 57600000

    def test_regression_a(self):
        assert self.day.run_part("a") == 13882464

    def test_regression_b(self):
        assert self.day.run_part("b") == 11171160
