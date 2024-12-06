import pytest
from aoc2015.day18 import Run_2015_18


class Test_2015_18:
    def setup_class(self):
        self.day = Run_2015_18()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 4

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1", steps=5) == 17

    def test_regression_a(self):
        assert self.day.run_part("a") == 768

    def test_regression_b(self):
        assert self.day.run_part("b") == 781
