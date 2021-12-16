import pytest
from aoc2021.day11 import Run_2021_11


class Test_2021_11:
    def setup_class(self):
        self.day = Run_2021_11()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", days=2) == 9
        assert self.day.run_part("a", "test2", days=10) == 204
        assert self.day.run_part("a", "test2") == 1656

    def test_bringup_b(self):
        assert self.day.run_part("b", "test2") == 195

    def test_regression_a(self):
        assert self.day.run_part("a") == 1673

    def test_regression_b(self):
        assert self.day.run_part("b") == 279
