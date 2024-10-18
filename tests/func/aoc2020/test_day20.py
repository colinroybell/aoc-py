import pytest
from aoc2020.day20 import Run_2020_20


class Test_2020_20:
    def setup_class(self):
        self.day = Run_2020_20()

    def test_regression_a(self):
        assert self.day.run_part("a") == 23386616781851

    def test_regression_b(self):
        assert self.day.run_part("b") == 2376
