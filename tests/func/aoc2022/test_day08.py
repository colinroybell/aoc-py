import pytest
from aoc2022.day08 import Run_2022_08


class Test_2022_08:
    def setup_class(self):
        self.day = Run_2022_08()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 21

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 8

    def test_regression_a(self):
        assert self.day.run_part("a") == 1812

    def test_regression_b(self):
        assert self.day.run_part("b") == 315495
