import pytest
from aoc2015.day06 import Run_2015_06


class Test_2015_06:
    def setup_class(self):
        self.day = Run_2015_06()

    def test_bringup_a(self):
        pass

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 543903

    def test_regression_b(self):
        assert self.day.run_part("b") == 14687245
