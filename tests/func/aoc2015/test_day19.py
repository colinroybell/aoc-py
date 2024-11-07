import pytest
from aoc2015.day19 import Run_2015_19


class Test_2015_19:
    def setup_class(self):
        self.day = Run_2015_19()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 4

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 7

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test1") == 3

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test2") == 6

    def test_regression_a(self):
        assert self.day.run_part("a") == 535

    def test_regression_b(self):
        assert self.day.run_part("b") == 212
