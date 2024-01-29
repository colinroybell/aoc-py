import pytest
from aoc2017.day08 import Run_2017_08


class Test_2017_08:
    def setup_class(self):
        self.day = Run_2017_08()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 1

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 10

    def test_regression_a(self):
        assert self.day.run_part("a") == 4832

    def test_regression_b(self):
        assert self.day.run_part("b") == 5443
