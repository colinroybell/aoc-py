import pytest
from aoc2023.day14 import Run_2023_14


class Test_2023_14:
    def setup_class(self):
        self.day = Run_2023_14()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 136

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 64

    def test_regression_a(self):
        assert self.day.run_part("a") == 108889

    def test_regression_b(self):
        assert self.day.run_part("b") == 104671
