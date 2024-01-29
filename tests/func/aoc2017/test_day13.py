import pytest
from aoc2017.day13 import Run_2017_13


class Test_2017_13:
    def setup_class(self):
        self.day = Run_2017_13()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 24

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 10

    def test_regression_a(self):
        assert self.day.run_part("a") == 1904

    def test_regression_b(self):
        assert self.day.run_part("b") == 3833504
