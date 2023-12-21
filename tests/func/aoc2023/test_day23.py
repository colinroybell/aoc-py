import pytest
from aoc2023.day23 import Run_2023_23


class Test_2023_23:
    def setup_class(self):
        self.day = Run_2023_23()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 94

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 154

    def test_regression_a(self):
        assert self.day.run_part("a") == 2306

    def test_regression_b(self):
        assert self.day.run_part("b") == 6718
