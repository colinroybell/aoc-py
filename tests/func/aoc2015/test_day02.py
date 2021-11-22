import pytest
from aoc2015.day02 import Run_2015_02


class Test_2015_02:
    def setup_class(self):
        self.day = Run_2015_02()

    def test_bringup_a(self):
        assert self.day.run_part("a", ["2x3x4"]) == 58
        assert self.day.run_part("a", ["1x1x10"]) == 43

    def test_bringup_b(self):
        assert self.day.run_part("b", ["2x3x4"]) == 34
        assert self.day.run_part("b", ["1x1x10"]) == 14

    def test_regression_a(self):
        assert self.day.run_part("a") == 1606483

    def test_regression_b(self):
        assert self.day.run_part("b") == 3842356
