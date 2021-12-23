import pytest
from aoc2021.day23 import Run_2021_23


class Test_2021_23:
    def setup_class(self):
        self.day = Run_2021_23()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 12521

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 44169

    def test_regression_a(self):
        assert self.day.run_part("a") == 13558

    def test_regression_b(self):
        assert self.day.run_part("b") == 56982
