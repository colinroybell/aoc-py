import pytest
from aoc2020.day10 import Run_2020_10


class Test_2020_10:
    def setup_class(self):
        self.day = Run_2020_10()

    def test_bringup_a_1(self):
        assert self.day.run_part("a", "test1") == 35

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 220

    def test_bringup_b_1(self):
        assert self.day.run_part("b", "test1") == 8

    def test_bringup_b_2(self):
        assert self.day.run_part("b", "test2") == 19208

    def test_regression_a(self):
        assert self.day.run_part("a") == 2170

    def test_regression_b(self):
        assert self.day.run_part("b") == 24803586664192
