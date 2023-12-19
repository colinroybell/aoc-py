import pytest
from aoc2022.day24 import Run_2022_24


class Test_2022_24:
    def setup_class(self):
        self.day = Run_2022_24()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 18

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 54

    def test_regression_a(self):
        assert self.day.run_part("a") == 288

    def test_regression_b(self):
        assert self.day.run_part("b") == 861
