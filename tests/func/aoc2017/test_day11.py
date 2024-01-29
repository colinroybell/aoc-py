import pytest
from aoc2017.day11 import Run_2017_11


class Test_2017_11:
    def setup_class(self):
        self.day = Run_2017_11()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", ["ne,ne,ne"]) == 3

    def test_bringup_a_2(self):
        assert self.day.run_part("a", ["ne,ne,sw,sw"]) == 0

    def test_bringup_a_3(self):
        assert self.day.run_part("a", ["ne,ne,s,s"]) == 2

    def test_bringup_a_4(self):
        assert self.day.run_part("a", ["se,sw,se,sw,sw"]) == 3

    def test_regression_a(self):
        assert self.day.run_part("a") == 818

    def test_regression_b(self):
        assert self.day.run_part("b") == 1596
