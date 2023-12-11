import pytest
from aoc2023.day03 import Run_2023_03

class Test_2023_03:
    def setup_class(self):
        self.day = Run_2023_03()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 4361

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 467835

    def test_regression_a(self):
        assert(self.day.run_part('a') == 540212)

    def test_regression_b(self):
        assert(self.day.run_part('b') == 87605697)

