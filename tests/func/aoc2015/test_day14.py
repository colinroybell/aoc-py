import pytest
from aoc2015.day14 import Run_2015_14, distance


class Test_2015_14:
    def setup_class(self):
        self.day = Run_2015_14()

    def test_distance(self):
        assert distance(1000, 14, 10, 127) == 1120
        assert distance(1000, 16, 11, 162) == 1056

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", time=1000) == 1120

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1", time=1000) == 689

    def test_regression_a(self):
        assert self.day.run_part("a") == 2696

    def test_regression_b(self):
        assert self.day.run_part("b") == 1084
