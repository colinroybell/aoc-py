import pytest
from aoc2023.day02 import Run_2023_02

class Test_2023_02:
    def setup_class(self):
        self.day = Run_2023_02()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 8

    def test_bringup_b(self):
         assert self.day.run_part("b", "test1") == 2286

    def test_regression_a(self):
        assert(self.day.run_part('a') == 2776)

    def test_regression_b(self):
        assert(self.day.run_part('b') == 68638)

