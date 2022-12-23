import pytest
from aoc2022.day23 import Run_2022_23


class Test_2022_23:
    def setup_class(self):
        self.day = Run_2022_23()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 110
        assert self.day.run_part("a", "test2") == 25

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 20
        assert self.day.run_part("b", "test2") == 4

    def test_regression_a(self):
        assert self.day.run_part("a") == 4302

    def test_regression_b(self):
        assert self.day.run_part("b") == 1025
